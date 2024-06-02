import signal

from src.utils.Logging import Logging
from src.user.service.AuthenticationService import AuthenticationService
from src.option.service.OptionService import OptionService
from src.utils.IOUtils import IOUtils
from src.utils.EnctryptUtils import encrypt_password
from src.utils.DateUtils import DateUtils


class Menu:
    def __init__(self, option_service: OptionService, authentication_service: AuthenticationService):
        self._keep_running_menu = True
        self._menu_options = None
        self._authenticated_user = None

        self._option_service = option_service
        self._authentication_service = authentication_service

    def start(self, signal_handler):
        self.signal_handler = signal_handler
        Logging.clear()
        Logging.print("Bienvenido al sistema de gestión de Recursos Humanos HR Connect")
        self._login()
        self._run_menu()

    def _login(self):
        while self._authenticated_user == None:
            username = IOUtils.input_string("Usuario: ")
            password = encrypt_password(IOUtils.input_password("Contraseña: "))
            self._authenticated_user = self._authentication_service.authenticate(username, password)
            if self._authenticated_user is not None:
                Logging.clear()
                Logging.print("Autenticación Correcta!")
                Logging.debug(self._authenticated_user)
                self._option_service.load_options()
                self._menu_options = self._option_service.get_options_for_role(self._authenticated_user.get_role())
            else:
                Logging.print("Usuario o contraseña incorrectos. Intente nuevamente.")

    def _run_menu(self):
        while self._keep_running_menu and self._authenticated_user != None:
            Logging.print("Bienvenido " + self._authenticated_user.get_full_name() + "! (" + DateUtils.get_formatted_current_date_time() + ")")
            Logging.print("Menú:")
            for i, option in enumerate(self._menu_options):
                Logging.print(f"{i+1}. {option.get_option_name()}")
            Logging.print("q. Terminar programa")
            
            opcion = IOUtils.input_string("> Seleccione una opción: ")
            Logging.print("Usted ha ingresado " + opcion)
            if opcion.lower() == "q":
                self._shutdown()
            elif not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(self._menu_options):
                Logging.clear()
                Logging.print("Opción inválida. Intente nuevamente.")
            else:
                selected_option = self._menu_options[int(opcion)-1]
                selected_option.execute_option_use_case()

    def _shutdown(self):
        self._keep_running_menu = False
        self.signal_handler(signal.SIGINT, None)

