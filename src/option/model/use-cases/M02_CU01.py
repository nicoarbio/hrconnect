from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging


# ATENCION: CASO DE USO DE EJEMPLO! - BORRAR
class M02_CU01(AbstractOption):

    def get_id(self):
        return "M02_CU01"

    def get_description(self):
        return "Caso de uso con actor Recuiter"

    def execute_option_use_case(self):
        # TODO agregar toda la logica con los bucles necesarios y la información necesaria
        Logging.clear()
        Logging.print("Mensaje de estado final al ejecutar el caso de uso " + self.get_option_name())
