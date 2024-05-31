from src.utils.DateUtils import DateUtils


class OpenPosition:
    def __init__(self, _id, _department, _manager_user, _title, _description, _created_at = None, _updated_at = None):
        # type: (str, str, str, str, str, str, str) -> None
        self._id = _id
        self._department = _department
        self._manager_user = _manager_user
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
        return (f"OpenPosition(id={self._id}, title={self._title}, manager_user={self._manager_user}, description={self._description}, created_at={self._created_at}, updated_at={self._updated_at})")

    # Getters
    def get_id(self):
        return self._id
    
    def get_department(self):
        return self._department
    
    def get_manager_user(self):
        return self._manager_user
    
    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
    
    # Setters
    #def set_id(self, id):
    #    self._id = id
    
    def set_department(self, department):
        self._department = department

    def set_manager_user(self, manager_user):
        self._manager_user = manager_user

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description
