from src.user.dao.UserInMemoryDAO import UserInMemoryDAO
from src.position.dao.PositionInMemoryDAO import PositionInMemoryDAO
from src.option.service.OptionService import OptionService
from src.user.service.AuthenticationService import AuthenticationService

class BeanManager:
    _instances = {}

    @classmethod
    def get_instance(cls, bean_name, factory, *bean_dependencies):
        if bean_name not in cls._instances:
            cls._instances[bean_name] = factory(*bean_dependencies)
        return cls._instances[bean_name]
    
    @classmethod
    def get_UserDAO(cls) -> UserInMemoryDAO:
        return cls.get_instance('user_dao', UserInMemoryDAO)
    
    @classmethod
    def get_PositionDAO(cls) -> PositionInMemoryDAO:
        return cls.get_instance('position_dao', PositionInMemoryDAO)
    
    @classmethod
    def get_OptionService(cls) -> OptionService:
        return cls.get_instance('option_service', OptionService)
    
    @classmethod
    def get_AuthenticationService(cls, user_dao) -> AuthenticationService:
        return cls.get_instance('authentication_service', AuthenticationService, user_dao)
    
    
    @classmethod
    def get_InMemoryDataAccessObjects(cls):
        in_memory_data_access_objects = []
        
        user_dao = cls.get_UserDAO()
        if hasattr(user_dao, 'backup_data'):
            in_memory_data_access_objects.append(user_dao)
        
        position_dao = cls.get_PositionDAO()
        if hasattr(position_dao, 'backup_data'):
            in_memory_data_access_objects.append(position_dao)
        
        return in_memory_data_access_objects