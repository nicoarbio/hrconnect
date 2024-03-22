from abc import ABC, abstractmethod


class AbstractUserDAO(ABC):
    @abstractmethod
    def get_by_username(self, username):
        pass

