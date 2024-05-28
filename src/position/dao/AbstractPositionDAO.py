from abc import ABC, abstractmethod

from src.position.model.Position import Position

class AbstractPositionDAO(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, position_id):
        pass

    @abstractmethod
    def delete(self, position: Position):
        pass

    @abstractmethod
    def delete_by_id(self, position_id):
        pass

    @abstractmethod
    def create(self, position: Position):
        pass

    @abstractmethod
    def update(self, position_id, updated_position: Position):
        pass