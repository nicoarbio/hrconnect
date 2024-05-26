import configparser

CONFIG_FILE_PATH = 'config.properties'

class AppConfig:
    @staticmethod
    def get_properties():
        config = configparser.ConfigParser()
        config.read("src/config/config.properties")
        return config['DEFAULT']
    
    @staticmethod
    def get_property(key):
        return AppConfig.get_properties().get(key)
    
    @staticmethod
    def get_property_and_compare_value(key, value):
        return AppConfig.get_property(key).lower() == value.lower()