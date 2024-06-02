from abc import ABC, abstractmethod

from src.utils.interfaces.DAO import DAO
from src.user.model.User import User


class AbstractUserDAO(DAO, ABC):

    @abstractmethod
    def get_by_email(self, email) -> User:
        pass

    def refresh_last_login(self, user: User):
        user.refresh_last_login()
        self.update(user)
