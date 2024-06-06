from abc import ABC, abstractmethod

from src.utils.interfaces.DAO import DAO
from src.notifications.model.Notification import Notification


class AbstractNotificationDAO(DAO, ABC):

    @abstractmethod
    def get_new_notifications_by_employee_id(self, employee_id) -> list[Notification]:
        pass

    @abstractmethod
    def get_notifications_by_employee_id(self, employee_id) -> list[Notification]:
        pass
