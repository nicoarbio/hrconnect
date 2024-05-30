from src.utils.DateUtils import DateUtils

class User:
    def __init__(self, _email, _password, _name, _lastname, _position, _role, _employee_id, _last_login, _is_blocked, _created_at = None, _updated_at = None):
        # type: (str, str, str, str, str, str, str, str, bool, str, str) -> None
        self._email = _email
        self._password = _password
        self._name = _name
        self._lastname = _lastname
        self._position = _position
        self._role = _role
        self._employee_id = _employee_id
        self._last_login = _last_login
        self._is_blocked = _is_blocked
        #self._notification_ids = _notification_ids
        #self._building_card_id = _building_card_id
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
        return (f"User(fullname={self.get_full_name()}, email={self._email}, position={self._position}, role={self._role}, employee_id={self._employee_id}, last_login={self._last_login}, is_blocked?={self._is_blocked}, created_at={self._created_at}, updated_at={self._updated_at})\n")

    def refresh_last_login(self):
        self._last_login = DateUtils.get_formatted_current_date_time()

    def get_full_name(self):
        return f"{self._lastname}, {self._name}"

    # Getters
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password
    
    def get_name(self):
        return self._name
    
    def get_lastname(self):
        return self._lastname

    def get_position(self):
        return self._position
    
    def get_role(self):
        return self._role

    def get_employee_id(self):
        return self._employee_id

    def get_last_login(self):
        return self._last_login

    def get_is_blocked(self):
        return self._is_blocked

    # Patrón With (inmutable)
    def with_email(self, email):
        return User(email, self._password, self._name, self._lastname, self._position, self._role, self._employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)

    def with_password(self, password):
        return User(self._email, password, self._name, self._lastname, self._position, self._role, self._employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)
    
    def with_name(self, name):
        return User(self._email, self._password, name, self._lastname, self._position, self._role, self._employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)
    
    def with_lastname(self, lastname):
        return User(self._email, self._password, self._name, lastname, self._position, self._role, self._employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)

    def with_position(self, position):
        return User(self._email, self._password, self._name, self._lastname, position, self._role, self._employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)
    
    def with_role(self, role):
        return User(self._email, self._password, self._name, self._lastname, self._position, role, self._employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)

    def with_employee_id(self, employee_id):
        return User(self._email, self._password, self._name, self._lastname, self._position, self._role, employee_id, self._last_login, self._is_blocked, self._created_at, self._updated_at)

    def with_last_login(self, last_login):
        return User(self._email, self._password, self._name, self._lastname, self._position, self._role, self._employee_id, last_login, self._is_blocked, self._created_at, self._updated_at)

    def with_is_blocked(self, is_blocked):
        return User(self._email, self._password, self._name, self._lastname, self._position, self._role, self._employee_id, self._last_login, is_blocked, self._created_at, self._updated_at)
