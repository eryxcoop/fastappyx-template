from abc import abstractmethod

from interface.fastappyx.tasks.base_task import BaseTask


class AsyncTask(BaseTask):
    @classmethod
    def is_async(cls):
        return True

    @abstractmethod
    async def _execute_when_validation_succeeded(self, *args, **kwargs): ...

    async def execute(self, *args, **kwargs):
        await self._execute_when_validation_succeeded(*args, **kwargs)
        if self._create_new_session:
            self._storage_session.close()
