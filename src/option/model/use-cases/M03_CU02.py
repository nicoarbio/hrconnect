from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging


# ATENCION: CASO DE USO DE EJEMPLO!
class M03_CU02(AbstractOption):

    def get_id(self):
        return "M03_CU02"

    def get_description(self):
        return "Caso de uso con actor Colaborador de RRHH"

    def execute_option_use_case(self):
        # TODO agregar toda la logica con los bucles necesarios y la información necesaria
        Logging.clear()
        Logging.print("Mensaje de estado final al ejecutar el caso de uso " + self.get_option_name())
