import json
from .AbstractUserDAO import AbstractUserDAO
from ..model.User import User

PATH_TO_MOCK_FILE = "src/hrconnect/users/dao/mock_users_db.json"


class UserInMemoryDAO(AbstractUserDAO):
    def __init__(self):
        with open(PATH_TO_MOCK_FILE) as file:
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
