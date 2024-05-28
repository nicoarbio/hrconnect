import json
from datetime import datetime

from src.user.dao.AbstractUserDAO import AbstractUserDAO
from src.user.model.User import User

USERS_DB_FILEPATH = "src/config/in_memory_users_db.json"


class UserInMemoryDAO(AbstractUserDAO):
    def __init__(self):
        with open(USERS_DB_FILEPATH) as file:
            data = json.load(file)
            self._data = [User(**user_data) for user_data in data]

    def get_all(self):
        return self._data

    def get_by_username(self, username):
        for user in self._data:
            if user._email == username:
                return user
        return None
    
    def create(self, user: User):
        self._data.append(user)

    def update(self, username, updated_user: User):
        for i, user in enumerate(self._data):
            if user._email == username:
                self._data[i] = updated_user
                return updated_user
        return None

    def delete_by_username(self, username):
        for i, user in enumerate(self._data):
            if user._email == username:
                return self._data.pop(i)
        return None

    def delete(self, user: User):
        return self.delete_by_username(user._email)
    
    def backup_data(self):
        with open(USERS_DB_FILEPATH, 'w') as file:
            json.dump([user.__dict__ for user in self._data], file, indent=4)

    def refresh_last_login(self, user: User):
        user._last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update(user._email, user)
