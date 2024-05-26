import json
from src.user.dao.AbstractUserDAO import AbstractUserDAO
from src.user.model.User import User

INTIAL_USERS_DB_FILEPATH = "src/user/dao/mock_users_db.json"


class UserInMemoryDAO(AbstractUserDAO):
    def __init__(self):
        with open(INTIAL_USERS_DB_FILEPATH) as file:
            data = json.load(file)
            self._data = {username: User(**user_data) for username, user_data in data.items()}

    def get_by_username(self, username):
        return self._data.get(username)

    # def create(self, item):
    #     self._data.append(item)
    #
    # def read(self, index):
    #     return self._data[index]
    #
    # def update(self, index, item):
    #     self._data[index] = item
    #
    # def delete(self, index):
    #     del self._data[index]
