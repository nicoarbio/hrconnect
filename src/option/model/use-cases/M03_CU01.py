from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager


# ATENCION: CASO DE USO DE EJEMPLO!
class M03_CU01(AbstractOption):

    def get_id(self):
        return "M03_CU01"

    def get_description(self):
        return "M prueba"

    def execute_option_use_case(self):
        # TODO agregar toda la logica con los bucles necesarios y la información necesaria
        Logging.clear()
        str_items = map(str, BeanManager.get_PositionDAO().get_all())
        for item in str_items:
            Logging.print(item)
        str_items = map(str, BeanManager.get_UserDAO().get_all())
        for item in str_items:
            Logging.print(item)

        Logging.print("Mensaje de estado final al ejecutar el caso de uso " + self.get_option_name())
