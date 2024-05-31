from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager


# ATENCION: CASO DE USO DE EJEMPLO!
class M03_CU01(AbstractOption):

    def get_id(self):
        return "M03_CU01"

    def get_description(self):
        return "Mostrar todas las posiciones y usuarios en el sistema"

    def execute_option_use_case(self):
        # TODO agregar toda la logica y la información necesarias
        str_items = map(str, BeanManager.get_OpenPositionDAO().get_all())
        for item in str_items:
            Logging.print("-> " + str(item))
        str_items = map(str, BeanManager.get_UserDAO().get_all())
        for item in str_items:
            Logging.print("-> " + str(item))

        input("Presione una tecla para continuar...")
        Logging.clear()

