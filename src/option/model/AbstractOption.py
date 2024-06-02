from abc import ABC, abstractmethod


class AbstractOption(ABC):

    @abstractmethod
    def get_id(self):
        """Set the USE CASE ID. Example: `M04_CU16`"""
        pass

    @abstractmethod
    def get_description(self):
        """Set the description to be shown for the user in menu. Example: `Crear usuario`"""
        pass

    @abstractmethod
    def execute_option_use_case(self):
        """Step by step of the use case"""
        pass

    def get_option_name(self):
        return self.get_id() + ": " + self.get_description()
    
    # toString
    def __str__(self):
        return self.get_option_name()
