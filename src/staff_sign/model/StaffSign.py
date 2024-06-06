class StaffSign:
    def __init__(self, _employee_id, _date, _time_in, _time_out = None):
        # type: (str, str, str, str) -> None
        self._employee_id = _employee_id
        self._date = _date
        self._time_in = _time_in
        self._time_out = _time_out

    # toString
    def __str__(self):
        return (f"StaffSign(employee_id={self._employee_id}, date={self._date}, time_in={self._time_in}, time_out={self._time_out})")

    # Getters
    def get_employee_id(self):
        return self._employee_id
    
    def get_date(self):
        return self._date
    
    def get_time_in(self):
        return self._time_in
    
    def get_time_out(self):
        return self._time_out
    
    # Setters
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_date(self, date):
        self._date = date

    def set_time_in(self, time_in):
        self._time_in = time_in

    def set_time_out(self, time_out):
        self._time_out = time_out