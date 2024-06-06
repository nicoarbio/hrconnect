from abc import ABC, abstractmethod

from src.utils.interfaces.DAO import DAO
from src.staff_sign.model.StaffSign import StaffSign


class AbstractStaffSignDAO(DAO, ABC):

    @abstractmethod
    def get_by_employeeid_and_date(self, employee_id, date) -> StaffSign:
        pass

    @abstractmethod
    def get_by_employeeid(self, employee_id) -> list[StaffSign]:
        pass

    @abstractmethod
    def get_by_date(self, date) -> list[StaffSign]:
        pass
