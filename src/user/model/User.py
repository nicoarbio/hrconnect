class User:
    def __init__(self, email, password, position, role, employee_id, last_login, is_blocked):
        # type: (str, str, str, str, str, str, bool) -> None
        self._email = email
        self._password = password
        self._position = position
        self._role = role
        self._employee_id = employee_id
        self._last_login = last_login
        self._is_blocked = is_blocked

    # toString
    def __str__(self):
        return (f"---------------------------------\n"
                f"Información del usuario:\n"
                f"Email: {self._email}\n"
                f"Cargo: {self._position}\n"
                f"Rol: {self._role}\n"
                f"ID de empleado: {self._employee_id}\n"
                f"Último login: {self._last_login}\n"
                f"Bloqueado? {self._is_blocked}\n"
                f"---------------------------------\n")

    # Getters
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

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
        return User(email, self._password, self._position, self._role, self._employee_id, self._last_login, self._is_blocked)

    def with_password(self, password):
        return User(self._email, password, self._position, self._role, self._employee_id, self._last_login, self._is_blocked)

    def with_position(self, position):
        return User(self._email, self._password, position, self._role, self._employee_id, self._last_login, self._is_blocked)
    
    def with_role(self, role):
        return User(self._email, self._password, self._position, role, self._employee_id, self._last_login, self._is_blocked)

    def with_employee_id(self, employee_id):
        return User(self._email, self._password, self._position, self._role, employee_id, self._last_login, self._is_blocked)

    def with_last_login(self, last_login):
        return User(self._email, self._password, self._position, self._role, self._employee_id, last_login, self._is_blocked)

    def with_is_blocked(self, is_blocked):
        return User(self._email, self._password, self._position, self._role, self._employee_id, self._last_login, is_blocked)
