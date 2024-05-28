class Position:
    def __init__(self, _id, _department, _manager_user_id, _title, _description):
        # type: (str, str, str, str, str) -> None
        self._id = _id
        self._department = _department
        self._manager_user_id = _manager_user_id
        self._title = _title
        self._description = _description

    # toString
    def __str__(self):
        return (f"---------------------------------\n"
                f"Información de la posición:\n"
                f"Title: {self._id}\n"
                f"Description: {self._department}\n"
                f"Departamento/Área: {self._manager_user_id}\n"
                f"Manager Name: {self._title}\n"
                f"ID: {self._description}\n"
                f"---------------------------------\n")

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
        return Position(self._id, department, self._manager_user_id, self._title, self._description)
    
    def with_department(self, manager_user_id):
        return Position(self._id, self._department, manager_user_id, self._title, self._description)
    
    def with_department(self, title):
        return Position(self._id, self._department, self._manager_user_id, title, self._description)
    
    def with_department(self, description):
        return Position(self._id, self._department, self._manager_user_id, self._title, description)

