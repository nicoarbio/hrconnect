from src.utils.DateUtils import DateUtils


class Notification:
    def __init__(self, _employee_id, _message, _status = None, _created_at = None):
        # type: (str, str, str, str) -> None
        self._employee_id = _employee_id
        self._status = _status
        self._message = _message
        if _status is None:
            self._status = "new"
        else:
            self._status = _status
        if _created_at is None:
            self._created_at = DateUtils.get_formatted_current_date_time()
        else:
            self._created_at = _created_at

    # toString
    def __str__(self):
        return (f"Notification(employee_id={self._employee_id}, status={self._status}, message={self._message}, created_at={self._created_at})")
    def is_new(self):
        return self._status.lower() == "new"
    
    def is_read(self):
        return self._status.lower() == "read"

    # Getters
    def get_employee_id(self):
        return self._employee_id
    
    def get_status(self):
        return self._status
    
    def get_message(self):
        return self._message
    
    def get_created_at(self):
        return self._created_at
    
    # Setters
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_status(self, status):
        self._status = status
    
    def set_message(self, message):
        self._message = message
    
    def set_created_at(self, created_at):
        self._created_at = created_at