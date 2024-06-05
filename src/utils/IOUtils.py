from getpass import getpass


class IOUtils:

    @staticmethod
    def input_string(message):
        return input(message)

    @staticmethod
    def input_password(message):
        try:
            return getpass(message)
        except KeyboardInterrupt:
            import signal
            from src import __main__
            __main__.signal_handler(signal.SIGINT, None)