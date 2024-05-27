from src.user.dao.UserInMemoryDAO import UserInMemoryDAO
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
    def get_UserInMemoryDAO(cls) -> UserInMemoryDAO:
        return cls.get_instance('user_dao', UserInMemoryDAO)
    
    @classmethod
    def get_OptionService(cls) -> OptionService:
        return cls.get_instance('option_service', OptionService)
    
    @classmethod
    def get_AuthenticationService(cls, user_dao) -> AuthenticationService:
        return cls.get_instance('authentication_service', AuthenticationService, user_dao)
    