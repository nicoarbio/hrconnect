from abc import ABC, abstractmethod


class AbstractOption(ABC):

    @abstractmethod
    def get_option_name(self):
        pass

    @abstractmethod
    def execute_option_use_case(self):
        pass

    # toString
    def __str__(self):
        return self.get_option_name()


