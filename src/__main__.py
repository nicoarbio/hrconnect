from src.menu.Menu import Menu
from src.user.dao.UserInMemoryDAO import UserInMemoryDAO

if __name__ == '__main__':
    userDao = UserInMemoryDAO()
    #optionDao = OptionInMemoryDAO()
    menu = Menu(userDao)
    # TODO possible menu configuration before start. Ej DB connection

    menu.start()
