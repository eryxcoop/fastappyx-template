from database_mapping.mappers import CompositeMapper
from domain.repositories.users_repositories.users_persistent_repository import UsersPersistentRepository


class MasterPersistentRepository:
    @classmethod
    def database_mapper(cls):
        return CompositeMapper(mappers=[repository.database_mapper() for repository in cls.all_repositories()])

    @classmethod
    def all_repositories(cls):
        return [UsersPersistentRepository]

    @classmethod
    def new_with(cls, session):
        return cls(session)

    def __init__(self, session):
        self._session = session
        self._users_repository = UsersPersistentRepository(session)

    def users_repository(self):
        return self._users_repository
