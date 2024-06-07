import uuid
import re
import json
from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager
from src.utils.IOUtils import IOUtils
from src.utils.EnctryptUtils import encrypt_password
from prettytable import PrettyTable
from src.option.service.OptionService import ROLES_CONFIG_FILEPATH
from src.user.model.User import User


class M01_CU01(AbstractOption):
    """
    Descripción: Un ColaboradorRRHH puede crear una cuenta de empleado (Usuario) en el sistema.
    """

    def get_id(self):
        return "M01_CU01"

    def get_description(self):
        return "Crear Cuenta"
    
    def execute_option_use_case(self):
        self.manual_execute_option_use_case()

    def manual_execute_option_use_case(self, name = None, lastname = None, position = None):
        Logging.clear()
        Logging.print(self.get_option_name())
        Logging.print("Se procederá a crear una cuenta de empleado.")
        if name != None or lastname != None or position != None:
            Logging.print("ATENCIÓN: Algunos campos ya se encuentran predefinidos. Los verá entre corchetes []. Podrá elegirlos ingresando Enter, de otra forma puede ingresar el valor correcto.")

        new_email = None
        new_password = encrypt_password("12345")
        new_name = None
        new_lastname = None
        new_position = None
        new_role = None
        new_employee_id = uuid.uuid4()
        new_daily_start_time = {
            "monday": "09:00:00",
            "tuesday": "09:00:00",
            "wednesday": "09:00:00",
            "thursday": "09:00:00",
            "friday": "09:00:00"
        }

        email_regex = r'^.*@hrconnect\.com$'
        while new_email == None:
            new_email = IOUtils.input_string("> Ingrese el email del empleado: (*@hrconnect.com)")
            if new_email == "" or re.match(email_regex, new_email) is None:
                new_email = None
                Logging.print("ERROR: Revise el email ingresado")

        while new_name == None:
            new_name = IOUtils.input_string("> Ingrese el nombre del empleado: " + ("[" + name + "]" if name != None else ""))
            if new_name == "":
                if name != None:
                    new_name = name
                else:
                    new_name = None
                    Logging.print("ERROR: Revise el nombre ingresado")

        while new_lastname == None:
            new_lastname = IOUtils.input_string("> Ingrese el apellido del empleado: " + ("[" + lastname + "]" if lastname != None else ""))
            if new_lastname == "":
                if lastname != None:
                    new_lastname = lastname
                else:
                    new_lastname = None
                    Logging.print("ERROR: Revise el apellido ingresado")

        while new_position == None:
            new_position = IOUtils.input_string("> Ingrese el cargo del empleado: " + ("[" + position + "]" if position != None else ""))
            if new_position == "":
                if position != None:
                    new_position = position
                else:
                    new_position = None
                    Logging.print("ERROR: Revise la posición ingresada")


        with open(ROLES_CONFIG_FILEPATH, 'r') as file:
            actual_roles = list(json.load(file)['cu_by_role'].keys())

        while new_role == None:
            new_role = IOUtils.input_string("> Ingrese el rol del empleado entre las opciones " + actual_roles + ": ")
            
            if new_role == "" or new_role not in actual_roles:
                new_role = None
                Logging.print("ERROR: Revise el rol ingresado")

        user_dao = BeanManager.get_UserDAO()
        new_user = User(new_email, new_password, new_name, new_lastname, new_position, new_role, new_employee_id, new_daily_start_time)
        user_dao.create(new_user)

        Logging.print("ATENCIÓN: Cuenta de empleado creada correctamente.")
        Logging.print("Comunique al empleado sus accesos:")
        Logging.print("- Email: " + new_email)
        Logging.print("- Contraseña: 12345")

        IOUtils.input_string("Presione Enter para continuar...")
        Logging.clear()
