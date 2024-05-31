from src.open_position.dao.AbstractOpenPositionDAO import AbstractOpenPositionDAO
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.open_position.model.OpenPosition import OpenPosition


OPEN_POSITIONS_DB_FILEPATH = "src/config/in_memory_open_positions_db.json"

class OpenPositionInMemoryDAO(InMemoryDAO, AbstractOpenPositionDAO):

    def __init__(self):
        super().__init__(OPEN_POSITIONS_DB_FILEPATH, OpenPosition)

    def resolveKey(self, entity: OpenPosition):
        return entity.get_id()
    
    def convert_ids_to_entities(self):
        from src.config.BeanManager import BeanManager

        user_dao = BeanManager.get_UserDAO()
        for open_position in self.get_all():
            manager_user = user_dao.get_by_id(open_position.get_manager_user())
            open_position = open_position.set_manager_user(manager_user)
    
    def convert_entities_to_ids(self):
        from src.config.BeanManager import BeanManager
        
        user_dao = BeanManager.get_UserDAO()
        for open_position in self.get_all():
            open_position = open_position.set_manager_user(user_dao.resolveKey(open_position.get_manager_user()))
