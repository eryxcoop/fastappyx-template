import asyncio
from abc import abstractmethod, ABC

from pydantic import ValidationError

from errors.authentication_error import AuthenticationError
from interface.fastappyx.http_request import HttpRequest
from interface.fastappyx.http_response import HttpResponse
from interface.fastappyx.presenters.base_presenter import BasePresenter
from interface.fastappyx.presenters.result_presenter import ResultPresenter
from interface.fastappyx.result import Result


class BaseSyncHandler(ABC):
    def __init__(self, application, authenticator, task_queue, interface):
        self._application = application
        self._task_queue = task_queue
        self._storage_session = self._application.storage().start_session()
        self._business = self._application.get_new_business(self._storage_session)
        self._interface = interface
        self._authenticator = authenticator
        self._arguments = {}
        self._user = None

    @abstractmethod
    def _execute_when_validation_succeeded(self, result): ...

    def _parameters(self):
        return []

    def _converters(self):
        return []

    def _status_code_for_error(self, error):
        if error.code() == "argument_error":
            return 400
        if error.code() == "authentication_error":
            return 401
        if error.code() == "not_found_error":
            return 404
        return 422

    def _status_code_for(self, result):
        if result.has_errors():
            return self._status_code_for_error(result.get_errors()[0])
        return 200

    def handle(self, request: HttpRequest) -> HttpResponse:
        result = Result()
        self._validate_user_is_authenticated(request, result)

        if not result.has_errors():
            self._validate_parameters(request, result)
            self._convert_arguments(result)

            if not result.has_errors():
                self._execute_when_validation_succeeded(result)

        presented_content = self._presented_result(result)

        self._storage_session.close()

        return HttpResponse(status_code=self._status_code_for(result), content=presented_content)

    def _presented_result(self, result):
        return ResultPresenter(result=result, object_presenter=self.object_presenter(result.get_object())).present()

    def object_presenter(self, result_object):
        return BasePresenter(result_object, self._interface, self._business)

    def _validate_user_is_authenticated(self, request, result):
        try:
            self._user = asyncio.run(self._authenticator.authenticate(request=request, gatekeeper=self._business.gatekeeper()))
        except AuthenticationError as authentication_error:
            result.add_authentication_error(str(authentication_error))

    def _validate_parameters(self, request, result):
        for parameter in self._parameters():
            try:
                # argument_value = parameter.get_argument_from_sync_request(request)
                argument_value = asyncio.run(parameter.get_argument_from_request(request))
                self._arguments[parameter.name()] = argument_value
            except ValidationError as validation_error:
                result.add_field_errors(validation_error)

    def _current_user(self):
        return self._user

    def _get_argument_named(self, name, default=None):
        return self._arguments.get(name, default)

    def _convert_arguments(self, result):
        for converter in self._converters():
            converter.convert(self._arguments, result)

    @classmethod
    def is_async(cls) -> bool:
        return False
