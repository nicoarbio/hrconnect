class User:
    def __init__(self, email, password, last_login, is_blocked, employee_id):
        # type: (str, str, str, bool, int) -> None
        self._email = email
        self._password = password
        self._last_login = last_login
        self._is_blocked = is_blocked
        self._employee_id = employee_id

    # toString
    def __str__(self):
        return (f"Usuario("
                f"email={self._email}, "
                f"last_login={self._last_login}, "
                f"is_blocked={self._is_blocked}, "
                f"employee_id={self._employee_id}"
                f")")

    # Getters
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_last_login(self):
        return self._last_login

    def get_is_blocked(self):
        return self._is_blocked

    def get_employee_id(self):
        return self._employee_id

    # Patrón With (inmutable)
    def with_email(self, email):
        return User(email, self._password, self._last_login, self._is_blocked, self._employee_id)

    def with_password(self, password):
        return User(self._email, password, self._last_login, self._is_blocked, self._employee_id)

    def with_last_login(self, last_login):
        return User(self._email, self._password, last_login, self._is_blocked, self._employee_id)

    def with_is_blocked(self, is_blocked):
        return User(self._email, self._password, self._last_login, is_blocked, self._employee_id)

    def with_employee_id(self, employee_id):
        return User(self._email, self._password, self._last_login, self._is_blocked, employee_id)
