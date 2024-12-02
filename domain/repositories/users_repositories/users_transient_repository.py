from domain.user import User
from domain.repositories.base_transient_repository import BaseTransientRepository


class UsersTransientRepository(BaseTransientRepository):
    def _domain_class(self):
        return User

    def has_user_with_email(self, email):
        return self.exists_by_condition(lambda user: user.has_email(email))
