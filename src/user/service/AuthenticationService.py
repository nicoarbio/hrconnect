from src.user.dao.AbstractUserDAO import AbstractUserDAO

class AuthenticationService:

    def __init__(self, user_dao: AbstractUserDAO):
        self._user_dao = user_dao

    def authenticate(self, username, password):
        user = self._user_dao.get_by_username(username)
        if user is None or user.get_password() != password:
            return None
        self._user_dao.refresh_last_login(user)
        return user
