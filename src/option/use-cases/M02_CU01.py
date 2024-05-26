from src.option.model.AbstractOption import AbstractOption


class M02_CU01(AbstractOption):

    def get_id(self):
        return "M02_CU01"

    def get_description(self):
        return "M prueba"

    def get_option_name(self):
        return self.get_id() + ": " + self.get_description()

    def execute_option_use_case(self):
        print("Ejecutando caso de uso " + self.get_id() + "...")
