class BaseCommand:
    def __init__(self, application):
        self._application = application

    def business(self):
        return self._application.current_business()

    def execute(self, *args, **kwargs): ...
