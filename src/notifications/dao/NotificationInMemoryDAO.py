from src.notifications.dao.AbstractNotificationDAO import AbstractNotificationDAO
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.notifications.model.Notification import Notification


DB_FILEPATH = "src/config/in_memory_notifications_db.json"

class NotificationInMemoryDAO(InMemoryDAO, AbstractNotificationDAO):

    def __init__(self):
        super().__init__(DB_FILEPATH, Notification)

    def resolveKey(self, entity: Notification):
        return entity.get_employee_id()

    def get_new_notifications_by_employee_id(self, employee_id) -> list[Notification]:
        new_notifications = []
        for notif in self.get_all():
            if notif.get_employee_id() == employee_id and notif.get_is_new():
                new_notifications.append(notif)
        return new_notifications
    
    def get_notifications_by_employee_id(self, employee_id) -> list[Notification]:
        new_notifications = []
        for notif in self.get_all():
            if notif.get_employee_id() == employee_id:
                new_notifications.append(notif)
        return new_notifications

    def convert_ids_to_entities(self):
        return
    
    def convert_entities_to_ids(self):
        return
