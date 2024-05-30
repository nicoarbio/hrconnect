from getpass import getpass

class IOUtils:

    @staticmethod
    def input_string(message):
        return input(message)

    @staticmethod
    def input_password(message):
        return getpass(message)
