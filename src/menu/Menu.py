from src.utils.IOUtils import IOUtils
from src.utils.EnctryptUtils import encrypt_password
from src.user.service.AuthenticationService import AuthenticationService
from src.option.service.OptionService import OptionService
from src.utils.Logging import Logging

class Menu:
    def __init__(self, user_dao):
        self._keepRunningMenu = True
        self._loggedIn = False
        self._menuOptions = []
        self._authenticatedUser = None

        self._option_service = OptionService()
        self._authService = AuthenticationService(user_dao)

    def start(self):
        print("Bienvenido al sistema de gestión de Recursos Humanos HR Connect")
        self._login()
        self._run_menu()

    def _login(self):
        while self._authenticatedUser == None:
            username = IOUtils.input_string("Usuario: ")
            password = encrypt_password(IOUtils.input_password("Contraseña: "))
            self._authenticatedUser = self._authService.authenticate(username, password)
            if self._authenticatedUser is not None:
                print("Autenticación Correcta!")
                Logging.debug(self._authenticatedUser)
            else:
                print("Usuario o contraseña incorrectos. Intente nuevamente.")

    def _run_menu(self):
        while self._keepRunningMenu and self._authenticatedUser != None:
            print("Menú:")
            user_options = self._option_service.get_options_for_role(self._authenticatedUser.get_role())
            for i, option in enumerate(user_options):
                print(f"{i+1}. {option.get_option_name()}")
            print("q. Terminar programa")
            
            opcion = IOUtils.input_string("Seleccione una opción: ")
            print("Usted ha ingresado ", opcion)
            if opcion == "q":
                self._shutdown()
            else:
                selected_option = user_options[int(opcion)-1]
                selected_option.execute_option_use_case()

    def _shutdown(self):
        self._keepRunningMenu = False
        print("Programa terminado.")
