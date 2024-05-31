from src.position.dao.AbstractPositionDAO import AbstractPositionDAO
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.position.model.Position import Position


POSITIONS_DB_FILEPATH = "src/config/in_memory_positions_db.json"

class PositionInMemoryDAO(InMemoryDAO, AbstractPositionDAO):

    def __init__(self):
        super().__init__(POSITIONS_DB_FILEPATH, Position)

    def resolveKey(self, entity: Position):
        return entity.get_id()
