import signal
import sys

from src.utils.Logging import Logging
from src.user.dao.UserInMemoryDAO import UserInMemoryDAO
from src.option.service.OptionService import OptionService
from src.user.service.AuthenticationService import AuthenticationService
from src.menu.Menu import Menu

option_service = None

def startApp():
    global option_service
    user_dao = UserInMemoryDAO()
    option_service = OptionService()
    authentication_service = AuthenticationService(user_dao)
    menu = Menu(option_service, authentication_service)
    # TODO possible menu configuration before start. Ej DB connection
    menu.start(signal_handler)

def signal_handler(sig, frame):
    Logging.print("\nATENCIÓN: Programa terminado por el usuario. Finalizando tareas pendientes en segundo plano...")
    for uc in option_service.get_schedule_options():
        Logging.print("Finalizando caso de uso programado: " + uc.get_option_name())
        uc.cancelThread()
    sys.exit(0)

if __name__ == '__main__':
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Termination signal
    startApp()