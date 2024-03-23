from src.utils.IOUtils import IOUtils
from src.utils.EnctryptUtils import encrypt_password
from src.hrconnect.users.service.AuthenticationService import AuthenticationService


class Menu:
    def __init__(self, userDao):
        self._keepRunningMenu = True
        self._loggedIn = False
        self._menuOptions = []
        self._authenticatedUser = None

        self._userDao = userDao
        self._authService = AuthenticationService(userDao)

    def start(self):
        print("Bienvenido al sistema de gestión de Recursos Humanos HR Connect")
        self._login()
        self._run_menu()

    def _login(self):
        while not self._loggedIn:
            username = IOUtils.input_string("Usuario: ")
            password = encrypt_password(IOUtils.input_password("Contraseña: "))
            self._authenticatedUser = self._authService.authenticate(username, password)
            if self._authenticatedUser is not None:
                self._loggedIn = True
                print("Autenticación Correcta!")
                print(self._authenticatedUser)
            else:
                print("Usuario o contraseña incorrectos. Intente nuevamente.")

    def _run_menu(self):
        while self._keepRunningMenu and self._loggedIn:
            opcion = self._showOptions()
            if opcion == "q":
                self._shutdown()

    def _shutdown(self):
        self._keepRunningMenu = False
        print("Programa terminado.")

    def _showOptions(self):
        print("Menú:")
        print("q. Terminar programa")
        opcion = IOUtils.input_string("Seleccione una opción: ")
        print("Usted ha ingresado ", opcion)
        return opcion

