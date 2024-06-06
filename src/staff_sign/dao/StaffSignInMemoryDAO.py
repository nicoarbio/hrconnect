from src.staff_sign.dao.AbstractStaffSignDAO import AbstractStaffSignDAO
from src.utils.interfaces.InMemoryDAO import InMemoryDAO
from src.staff_sign.model.StaffSign import StaffSign


DB_FILEPATH = "src/config/in_memory_daily_staff_sign_db.json"

class StaffSignInMemoryDAO(InMemoryDAO, AbstractStaffSignDAO):

    def __init__(self):
        super().__init__(DB_FILEPATH, StaffSign)

    def resolveKey(self, entity: StaffSign):
        return entity.get_employee_id() + "|" + entity.get_date()

    def get_by_employeeid_and_date(self, employee_id, date) -> StaffSign:
        for entry in self.get_all():
            if entry.get_employee_id() == employee_id and entry.get_date() == date:
                return entry
    
    def get_by_employeeid(self, employee_id) -> list[StaffSign]:
        staffSigns = []
        for entry in self.get_all():
            if entry.get_employee_id() == employee_id:
                staffSigns.append(entry)
        return staffSigns

    def get_by_date(self, date) -> list[StaffSign]:
        staffSigns = []
        for entry in self.get_all():
            if entry.get_date() == date:
                staffSigns.append(entry)
        return staffSigns

    def convert_ids_to_entities(self):
        return
    
    def convert_entities_to_ids(self):
        return
