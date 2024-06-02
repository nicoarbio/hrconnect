import os

from src.config.AppConfig import AppConfig


class Logging:
    @staticmethod
    def debug(message):
        if (AppConfig.get_property_and_compare_value('logger.level', 'debug')):
            print("DEBUG: " + str(message))

    @staticmethod
    def print(message):
        print(str(message))

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
