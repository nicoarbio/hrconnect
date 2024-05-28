from abc import ABC, abstractmethod

from src.user.model.User import User

class AbstractUserDAO(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_username(self, username):
        pass

    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def update(self, username, updated_user: User):
        pass

    @abstractmethod
    def delete_by_username(self, username):
        pass

    @abstractmethod
    def delete(self, user: User):
        pass

    @abstractmethod
    def refresh_last_login(self, user: User):
        pass