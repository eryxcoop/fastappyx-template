class Business:
    def __init__(self, master_repository, authentication_method, clock):
        self._master_repository = master_repository
        self._authentication_method = authentication_method
        self._clock = clock

    def do_something(self):
        self._something_done = True

    def is_something_done(self):
        return self._something_done
