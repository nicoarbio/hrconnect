from src.user.dao.AbstractUserDAO import AbstractUserDAO
from src.user.dao.UserInMemoryDAO import UserInMemoryDAO
from src.open_position.dao.AbstractOpenPositionDAO import AbstractOpenPositionDAO
from src.open_position.dao.OpenPositionInMemoryDAO import OpenPositionInMemoryDAO
from src.staff_sign.dao.AbstractStaffSignDAO import AbstractStaffSignDAO
from src.staff_sign.dao.StaffSignInMemoryDAO import StaffSignInMemoryDAO
from src.notifications.dao.AbstractNotificationDAO import AbstractNotificationDAO
from src.notifications.dao.NotificationInMemoryDAO import NotificationInMemoryDAO
from src.option.service.OptionService import OptionService
from src.user.service.AuthenticationService import AuthenticationService
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.office_services_check.service.OfficeServicesCheckService import OfficeServicesCheckService


class BeanManager:
    _instances = {}

    @classmethod
    def get_instance(cls, bean_name, factory, *bean_dependencies):
        """This method support dependency injection"""
        if bean_name not in cls._instances:
            cls._instances[bean_name] = factory(*bean_dependencies)
        return cls._instances[bean_name]
    
    @classmethod
    def get_UserDAO(cls) -> AbstractUserDAO:
        return cls.get_instance('user_dao', UserInMemoryDAO)
    
    @classmethod
    def get_OpenPositionDAO(cls) -> AbstractOpenPositionDAO:
        return cls.get_instance('open_position_dao', OpenPositionInMemoryDAO)
    
    @classmethod
    def get_OptionService(cls) -> OptionService:
        return cls.get_instance('option_service', OptionService)
    
    @classmethod
    def get_AuthenticationService(cls, user_dao) -> AuthenticationService:
        return cls.get_instance('authentication_service', AuthenticationService, user_dao)
    
    @classmethod
    def get_OfficeServicesCheckService(cls) -> OfficeServicesCheckService:
        return cls.get_instance('office_services_check_service', OfficeServicesCheckService)
    
    @classmethod
    def get_StaffSignDAO(cls) -> AbstractStaffSignDAO:
        return cls.get_instance('staff_sign_dao', StaffSignInMemoryDAO)
    
    @classmethod
    def get_NotificationDAO(cls) -> AbstractNotificationDAO:
        return cls.get_instance('notifications_dao', NotificationInMemoryDAO)
    
    @classmethod
    def get_InMemoryDataAccessObjects(cls) -> list[InMemoryDAO]:
        in_memory_data_access_objects = []
        
        for instance in cls._instances.values():
            if hasattr(instance, 'backup_data'):
                in_memory_data_access_objects.append(instance)

        return in_memory_data_access_objects