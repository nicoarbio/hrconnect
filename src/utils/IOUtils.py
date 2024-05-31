import sys
from getpass import getpass


class IOUtils:

    @staticmethod
    def input_string(message):
        return input(message)

    @staticmethod
    def input_password(message):
        try:
            return getpass(message)
        except KeyboardInterrupt as e:
            sys.exit(0)