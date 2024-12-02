from domain.user import User


class Business:
    def __init__(self, master_repository, authentication_method, clock):
        self._master_repository = master_repository
        self._authentication_method = authentication_method
        self._clock = clock

    def create_user(self, name, email):
        user = User.new_with(name=name, email=email)

        self._master_repository.users_repository().add(user)

        return user

    def has_user_with_email(self, email):
        return self._master_repository.users_repository().has_user_with_email(email)

    def has_n_users(self, n):
        return self._master_repository.users_repository().count() == n
