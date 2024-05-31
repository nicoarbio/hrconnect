import uuid
import json

from abc import ABC, abstractmethod
from src.utils.interfaces.DAO import DAO


class InMemoryDAO(DAO, ABC):

    def __init__(self, DB_FILEPATH, TYPE):
        self._DB_FILEPATH = DB_FILEPATH
        try:    
            with open(DB_FILEPATH, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self._data = [TYPE(**each_entity_data) for each_entity_data in data]
        except FileNotFoundError:
            self._data = []
    
    def backup_data(self):
        with open(self._DB_FILEPATH, 'w', encoding='utf-8') as file:
            json.dump([entity.__dict__ for entity in self._data], file, indent=4, ensure_ascii=False)

    @abstractmethod
    def resolveKey(self, entity):
        pass

    def get_next_id(self):
        return uuid.uuid4()    
    
    def create(self, entity):
        entity._id = self.get_next_id()
        self._data.append(entity)
        return entity
    
    def get_all(self):
        return self._data
    
    def get_by_id(self, id):
        for entity in self.get_all():
            if self.resolveKey(entity) == id:
                return entity
        return None
    
    def update(self, updated_entity):
        for i, entity in enumerate(self._data):
            if self.resolveKey(entity) == self.resolveKey(updated_entity):
                self._data[i] = updated_entity
                return updated_entity
        return None

    def delete(self, entity):
        return self.delete_by_id(self.resolveKey(entity))
    
    def delete_by_id(self, id):
        for index, entity in enumerate(self.get_all()):
            if self.resolveKey(entity) == id:
                return self._data.pop(index)
        return None
