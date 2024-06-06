from src.user.dao.AbstractUserDAO import AbstractUserDAO
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.user.model.User import User


USERS_DB_FILEPATH = "src/config/in_memory_users_db.json"

class UserInMemoryDAO(InMemoryDAO, AbstractUserDAO):

    def __init__(self):
        super().__init__(USERS_DB_FILEPATH, User)

    def resolveKey(self, entity: User):
        return entity.get_employee_id()

    def get_by_email(self, email) -> User:
        for user in self.get_all():
            if user.get_email() == email:
                return user
        return None
    
    def get_today_start(self):
        return [
            {"_employee_id": user.get_employee_id(), "_daily_start": user.get_today_daily_start()}
            for user in self.get_all() if user.get_daily_start() is not None ]
    
    def convert_ids_to_entities(self):
        return
    
    def convert_entities_to_ids(self):
        return
