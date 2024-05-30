from abc import ABC, abstractmethod
import threading

from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging

class AbstractScheduledOption(AbstractOption, ABC):

    @abstractmethod
    def get_period_in_seconds(self):
        """Set the period in seconds for the scheduled option"""
        pass

    def __init__(self):
        self.timer = None
        self.schedule_next_execution()

    def thread_function(self):
        self.execute_option_use_case()
        self.schedule_next_execution()

    def schedule_next_execution(self):
        try:
            self.timer = threading.Timer(self.get_period_in_seconds(), self.thread_function)
            self.timer.start()
        except Exception as e:
            Logging.debug("El caso de uso de actor tiempo " + self.get_id() + ": no se pudo programar")
            Logging.debug(e)

    def cancelThread(self):
        # Cancel the timer on shutdown
        if self.timer:
            self.timer.cancel()