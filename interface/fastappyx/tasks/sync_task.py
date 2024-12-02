from abc import abstractmethod

from interface.fastappyx.tasks.base_task import BaseTask


class SyncTask(BaseTask):
    @classmethod
    def is_async(cls):
        return False

    @abstractmethod
    def _execute_when_validation_succeeded(self, *args, **kwargs): ...

    def execute(self, *args, **kwargs):
        self._execute_when_validation_succeeded(*args, **kwargs)
        if self._create_new_session:
            self._storage_session.close()
