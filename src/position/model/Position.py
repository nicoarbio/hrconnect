from src.utils.DateUtils import DateUtils

class Position:
    def __init__(self, _id, _department, _manager_user_id, _title, _description, _created_at = None, _updated_at = None):
        # type: (str, str, str, str, str, str, str) -> None
        self._id = _id
        self._department = _department
        self._manager_user_id = _manager_user_id
        self._title = _title
        self._description = _description
        if _created_at is None:
            self._created_at = DateUtils.get_formatted_current_date_time()
        else:
            self._created_at = _created_at
        if _updated_at is None:
            self._updated_at = DateUtils.get_formatted_current_date_time()
        else:
            self._updated_at = _updated_at

    # toString
    def __str__(self):
        return (f"Position(id={self._id}, title={self._title}, department={self._manager_user_id}, description={self._description}, created_at={self._created_at}, updated_at={self._updated_at})\n")

    # Getters
    def get_id(self):
        return self._id
    
    def get_department(self):
        return self._department
    
    def get_manager_user_id(self):
        return self._manager_user_id
    
    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
    

    # Patrón With (inmutable)
    def with_department(self, department):
        return Position(self._id, department, self._manager_user_id, self._title, self._description, self._created_at, self._updated_at)
    
    def with_department(self, manager_user_id):
        return Position(self._id, self._department, manager_user_id, self._title, self._description, self._created_at, self._updated_at)
    
    def with_department(self, title):
        return Position(self._id, self._department, self._manager_user_id, title, self._description, self._created_at, self._updated_at)
    
    def with_department(self, description):
        return Position(self._id, self._department, self._manager_user_id, self._title, description, self._created_at, self._updated_at)

