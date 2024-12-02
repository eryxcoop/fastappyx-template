class TyperCliInterfaceAdapter:
    def __init__(self, typer_cli_server, cli_interface):
        self._typer_cli_server = typer_cli_server
        self._cli_interface = cli_interface

    def adapt_commands(self):
        for command_definition in self._cli_interface.command_definitions():
            self._adapt_command_definition(command_definition)

    def _adapt_command_definition(self, command_definition):
        command = command_definition.command()
        self._typer_cli_server.command(command_definition.name())(command.execute)
