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
