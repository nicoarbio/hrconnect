from src.user.dao.UserInMemoryDAO import UserInMemoryDAO
from src.open_position.dao.OpenPositionInMemoryDAO import OpenPositionInMemoryDAO
from src.option.service.OptionService import OptionService
from src.user.service.AuthenticationService import AuthenticationService
from src.utils.interfaces.InMemoryDAO import InMemoryDAO


class BeanManager:
    _instances = {}

    @classmethod
    def get_instance(cls, bean_name, factory, *bean_dependencies):
        """This method support dependency injection"""
        if bean_name not in cls._instances:
            cls._instances[bean_name] = factory(*bean_dependencies)
        return cls._instances[bean_name]
    
    @classmethod
    def get_UserDAO(cls) -> UserInMemoryDAO:
        return cls.get_instance('user_dao', UserInMemoryDAO)
    
    @classmethod
    def get_OpenPositionDAO(cls) -> OpenPositionInMemoryDAO:
        return cls.get_instance('open_position_dao', OpenPositionInMemoryDAO)
    
    @classmethod
    def get_OptionService(cls) -> OptionService:
        return cls.get_instance('option_service', OptionService)
    
    @classmethod
    def get_AuthenticationService(cls, user_dao) -> AuthenticationService:
        return cls.get_instance('authentication_service', AuthenticationService, user_dao)
    
    
    @classmethod
    def get_InMemoryDataAccessObjects(cls) -> list[InMemoryDAO]:
        in_memory_data_access_objects = []
        
        for instance in cls._instances.values():
            if hasattr(instance, 'backup_data'):
                in_memory_data_access_objects.append(instance)

        return in_memory_data_access_objects