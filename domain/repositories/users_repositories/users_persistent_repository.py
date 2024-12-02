from sqlalchemy import Column, String, Integer

from database_mapping.mappers import TableMapper
from domain.repositories.base_persistent_repository import BasePersistentRepository
from domain.user import User


class UsersPersistentRepository(BasePersistentRepository):
    @classmethod
    def database_mapper(cls):
        return TableMapper(
            klass=User,
            table_name="user",
            columns=[
                Column("_id", Integer, primary_key=True),
                Column("_name", String(100)),
                Column("_email", String(100), unique=True),
            ],
        )

    def _domain_class(self):
        return User

    def has_user_with_email(self, email):
        return self.exists_by(_email=email)
