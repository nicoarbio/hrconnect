from src.option.model.AbstractScheduledOption import AbstractScheduledOption
from src.utils.Logging import Logging


# ATENCION: CASO DE USO DE EJEMPLO! - BORRAR
class M05_CU01(AbstractScheduledOption):

    def get_period_in_seconds(self):
        return 10

    def get_id(self):
        return "M05_CU01"

    def get_description(self):
        return "Caso de uso con actor tiempo"

    def execute_option_use_case(self):
        # TODO agregar toda la logica con los bucles necesarios y la información necesaria
        # Los casos de uso que implementan la clase "AbstractScheduledOption", NO DEBERIAN, utilizar ningún print o input (Ni usar la clase Logging)
        # Logging.debug("Ejecutando en segundo plano: " + self.get_option_name())
        pass
