from abc import ABC, abstractmethod

class DAO(ABC):

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def update(self, updated_entity):
        pass
    
    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass
