from src.hrconnect.menu.Menu import Menu
from src.hrconnect.users.dao.UserInMemoryDAO import UserInMemoryDAO

if __name__ == "__main__":
    userDao = UserInMemoryDAO()
    menu = Menu(userDao)
    # TODO possible menu configuration before start. Ej DB connection

    menu.start()
