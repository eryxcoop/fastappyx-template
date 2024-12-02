from abc import ABC, abstractmethod


class BaseTask(ABC):
    @classmethod
    @abstractmethod
    def is_async(cls): ...

    def __init__(self, application, task_queue, create_new_session=True):
        self._application = application
        self._task_queue = task_queue
        self._create_new_session = create_new_session
        if create_new_session:
            self._storage_session = self._application.storage().start_session()
            self._business = self._application.get_new_business(self._storage_session)
        else:
            self._business = self._application.current_business()
        self._arguments = {}
        self._user = None

    def _current_user(self):
        return self._user

    def task_queue(self):
        return self._task_queue
