import json
from src.position.dao.AbstractPositionDAO import AbstractPositionDAO
from src.position.model.Position import Position

POSITIONS_DB_FILEPATH = "src/config/in_memory_positions_db.json"


class PositionInMemoryDAO(AbstractPositionDAO):
    def __init__(self):
        with open(POSITIONS_DB_FILEPATH) as file:
            data = json.load(file)
            self._data = [Position(**position_data) for position_data in data]

    def get_all(self):
        return self._data

    def get_by_id(self, position_id):
        for position in self._data:
            if position.id == position_id:
                return position
        return None
    
    def delete(self, position: Position):
        return self.delete_by_id(position.get_id())

    def delete_by_id(self, position_id):
        for index, position in enumerate(self._data):
            if position.id == position_id:
                return self._data.pop(index)
        return None
    
    def create(self, position: Position):
        self._data.append(position)

    def update(self, position_id, updated_position: Position):
        for i, position in enumerate(self._data):
            if position.id == position_id:
                self._data[i] = updated_position
                return updated_position
        return None
    
    def backup_data(self):
        with open(POSITIONS_DB_FILEPATH, 'w') as file:
            json.dump([position.__dict__ for position in self._data], file, indent=4)
