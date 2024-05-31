from src.position.dao.AbstractPositionDAO import AbstractPositionDAO
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.position.model.Position import Position


POSITIONS_DB_FILEPATH = "src/config/in_memory_positions_db.json"

class PositionInMemoryDAO(InMemoryDAO, AbstractPositionDAO):

    def __init__(self):
        super().__init__(POSITIONS_DB_FILEPATH, Position)

    def resolveKey(self, entity: Position):
        return entity.get_id()
    
    def convert_ids_to_entities(self):
        from src.config.BeanManager import BeanManager

        user_dao = BeanManager.get_UserDAO()
        for position in self.get_all():
            manager_user = user_dao.get_by_id(position.get_manager_user())
            position = position.set_manager_user(manager_user)
    
    def convert_entities_to_ids(self):
        from src.config.BeanManager import BeanManager
        
        user_dao = BeanManager.get_UserDAO()
        for position in self.get_all():
            position = position.set_manager_user(user_dao.resolveKey(position.get_manager_user()))
