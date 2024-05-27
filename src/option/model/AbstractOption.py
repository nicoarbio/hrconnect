from abc import ABC, abstractmethod


class AbstractOption(ABC):

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def execute_option_use_case(self):
        pass

    def get_option_name(self):
        return self.get_id() + ": " + self.get_description()
    
    # toString
    def __str__(self):
        return self.get_option_name()
