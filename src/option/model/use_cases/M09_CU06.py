from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager
from src.utils.IOUtils import IOUtils
from prettytable import PrettyTable
from src.option.model.use_cases.M01_CU01 import M01_CU01


class M09_CU06(AbstractOption):
    """
    Descripción: El Recruiter modifica el estado de un postulante a ACEPTADO y refleja los cambios en el sistema.
    """

    def get_id(self):
        return "M09_CU06"

    def get_description(self):
        return "Aceptar Postulante"
    
    def execute_option_use_case(self):
        Logging.clear()
        open_position_dao = BeanManager.get_OpenPositionDAO()
        positions_with_applicants = open_position_dao.get_positions_with_applicants()
        
        if len(positions_with_applicants) == 0:
            Logging.print(self.get_option_name())
            Logging.print("No hay postulantes a aceptar.")
            input("Presione Enter para continuar...")
            Logging.clear()
            return
        
        positions_table = PrettyTable()
        positions_table.align = "l"
        positions_table.field_names = ["Índice", "Posición", "Departamento", "Postulantes aceptables"]
        positions_table.align["Índice"] = "c"
        for index, position in enumerate(positions_with_applicants):
            positions_table.add_row([index + 1, position.get_title(), position.get_department(), len(position.get_acceptable_applicants())])

        quit_flag = False
        while not quit_flag:
            Logging.print(self.get_option_name())
            Logging.print("\nSeleccione una posición con candidatos a aceptar: ('q' para salir)")
            Logging.print(positions_table) 

            opcion = IOUtils.input_string("\n> Seleccione una opción: ")
            if opcion.lower() == "q":
                quit_flag = True
                Logging.clear()
            elif not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(positions_with_applicants):
                Logging.clear()
                Logging.print("ATENCION: Opción inválida. Intente nuevamente.")
            else:
                quit_flag = True
                chosen_position = positions_with_applicants[int(opcion) - 1]
                acceptable_applicants = chosen_position.get_acceptable_applicants()

                applicants_table = PrettyTable()
                applicants_table.align = "l"
                applicants_table.field_names = ["Índice", "Nombre Completo", "Email", "Estado actual", "Comentarios"]
                applicants_table.align["Índice"] = "c"
                for index, applicant in enumerate(acceptable_applicants):
                    applicants_table.add_row([index + 1, applicant["lastname"] + ", " + applicant["name"], applicant["email"], applicant["status"], '\n'.join(f"- {comment}" for comment in applicant["comments"]) if len(applicant["comments"]) > 0 else "Sin comentarios"])

                quit_flag = False
                while not quit_flag:
                    Logging.print("\nSeleccione el postulante a aceptar para la posición '" + chosen_position.get_title() + "': ('q' para salir)")
                    Logging.print(applicants_table) 

                    opcion = IOUtils.input_string("\n> Seleccione una opción: ")
                    if opcion.lower() == "q":
                        quit_flag = True
                        Logging.clear()
                    elif not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(acceptable_applicants):
                        Logging.clear()
                        Logging.print("ATENCION: Opción inválida. Intente nuevamente.")
                    else:
                        quit_flag = True
                        chosen_applicant = acceptable_applicants[int(opcion) - 1]
                        chosen_applicant["status"] = "ACEPTADO"
                        chosen_applicant["comments"].append("Postulante aceptado.")
                        open_position_dao.update(chosen_position)

                        Logging.print("Postulante " + chosen_applicant["lastname"] + ", " + chosen_applicant["name"] + " aceptado correctamente para la posición " + chosen_position.get_title())
                        Logging.print("Se procederá a actualizar o crear la cuenta de empleado del postulante.")

                        create_account = True
                        if chosen_applicant["works_here"]:
                            user_dao = BeanManager.get_UserDAO()

                            user_email = IOUtils.input_string("Se marcó que el postulante ya trabaja en la empresa. Ingrese su email para buscarlo y actualizar su posición: (Si es un error y se debe crear una nueva cuenta presione Enter)")
                            if user_email != None or user_email != "":
                                existing_user = user_dao.get_by_email(user_email)
                                if existing_user != None:
                                    create_account = False
                                    existing_user["position"] = chosen_position.get_title()
                                    user_dao.update(existing_user)
                            
                        if create_account:
                            IOUtils.input_string("Presione Enter para continuar con la creación de la cuenta de empleado...")
                            Logging.clear()
                            M01_CU01().manual_execute_option_use_case(name = chosen_applicant["name"], lastname = chosen_applicant["lastname"], position = chosen_position.get_title())
                        else:
                            Logging.clear()
                            Logging.print("La cuenta fue actualizada correctamente.")