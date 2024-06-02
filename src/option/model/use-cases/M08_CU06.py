from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager
from src.open_position.model.OpenPosition import OpenPosition
from src.utils.IOUtils import IOUtils


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
        
        quit_flag = False
        while not quit_flag:
            Logging.print(self.get_option_name())
            Logging.print("\nPosiciones que no se pueden eliminar:")
            for position in positions_not_to_delete:
                Logging.print(f"- {position._title} - {position._department}")

            Logging.print("\nSeleccione la posición a eliminar: ('q' para salir)")
            for index, position in enumerate(positions_to_delete):
                Logging.print(f"{index + 1}. {position._title} - {position._department}")
            Logging.print("q. Volver al menú principal")

            opcion = IOUtils.input_string("\nSu opción: ")
            if opcion.lower() == "q":
                quit_flag = True
                Logging.clear()
            elif not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(positions_to_delete):
                Logging.clear()
                Logging.print("Opción inválida. Intente nuevamente.")
            else:
                quit_flag = True
                open_position_dao.delete(positions_to_delete[int(opcion) - 1])
                Logging.print("Posición abierta (opción " + str(opcion) + ") eliminada correctamente.")
                input("Presione Enter para continuar...")
                Logging.clear()

