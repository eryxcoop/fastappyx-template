class CommandDefinition:
    def __init__(self, name: str, command, application):
        self._name = name
        self._command = command
        self._application = application

    def command(self):
        return self._command(self._application)

    def name(self):
        return self._name


class CommandInterface:
    def __init__(self, application):
        self._application = application

    def new_command_definition(self, command, name):
        return CommandDefinition(
            application=self._application,
            command=command,
            name=name,
        )

    def command_definitions(self) -> list: ...
