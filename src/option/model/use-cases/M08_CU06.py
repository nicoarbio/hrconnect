from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager
from src.open_position.model.OpenPosition import OpenPosition
from src.utils.IOUtils import IOUtils
from prettytable import PrettyTable


class M08_CU06(AbstractOption):
    """
    Descripción: Un Jefe puede borrar una posición creada por el mismo. En caso de tener postulantes asociados, solo se borrará la posición en caso de que estos estén en estado RECHAZADO.
    """

    def get_id(self):
        return "M08_CU06"

    def get_description(self):
        return "Borrar una posición"

    def execute_option_use_case(self):
        Logging.clear()
        open_position_dao = BeanManager.get_OpenPositionDAO()
        positions_to_delete, positions_not_to_delete = open_position_dao.filter_open_positions()
        if len(positions_to_delete) == 0:
            Logging.print(self.get_option_name())
            Logging.print("No hay posiciones abiertas que se puedan eliminar.")
            input("Presione Enter para continuar...")
            Logging.clear()
            return
        
        able_to_delete_table = PrettyTable()
        able_to_delete_table.align = "l"
        able_to_delete_table.field_names = ["Índice", "Posición", "Departamento"]
        able_to_delete_table.align["Índice"] = "c"
        for index, position in enumerate(positions_to_delete):
            able_to_delete_table.add_row([index + 1, position.get_title(), position.get_department()])

        unable_to_delete_table = PrettyTable()
        unable_to_delete_table.align = "l"
        unable_to_delete_table.field_names = ["Posición", "Departamento"]
        for position in positions_not_to_delete:
            unable_to_delete_table.add_row([position.get_title(), position.get_department()])


        quit_flag = False
        while not quit_flag:
            Logging.print(self.get_option_name())
            Logging.print("\nPosiciones que no se pueden eliminar:")
            Logging.print(unable_to_delete_table) 

            Logging.print("\nSeleccione la posición a eliminar: ('q' para salir)")
            Logging.print(able_to_delete_table) 

            opcion = IOUtils.input_string("\n> Seleccione una opción: ")
            if opcion.lower() == "q":
                quit_flag = True
                Logging.clear()
            elif not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(positions_to_delete):
                Logging.clear()
                Logging.print("Opción inválida. Intente nuevamente.")
            else:
                quit_flag = True
                position_to_delete = positions_to_delete[int(opcion) - 1]
                open_position_dao.delete(position_to_delete)
                Logging.clear()
                Logging.print("Posición abierta eliminada correctamente. (" + position_to_delete.get_title() + ")")

