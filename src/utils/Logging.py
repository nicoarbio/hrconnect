from src.config.AppConfig import AppConfig

class Logging:
    # static method debug
    @staticmethod
    def debug(message):
        if (AppConfig.get_property_and_compare_value('logger.level', 'debug')):
            print("DEBUG: " + str(message))
