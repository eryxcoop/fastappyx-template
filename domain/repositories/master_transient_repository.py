from domain.repositories.users_repositories.users_transient_repository import UsersTransientRepository


class MasterTransientRepository:
    def __init__(self):
        self._users_repository = UsersTransientRepository()

    def users_repository(self):
        return self._users_repository
