
class Console:
    def __init__(self):
        self._func_list = {}
        self.cursor = '>>'
        self.exit_command = 'exit'
        self.help_command = 'help'

    def register_function(self, command, func, description=''):
        """
        This method register a function in console, user can call that function by {command}
        func parameter is a function that returns None and have a single parameter (a list of strings, that represents user parameters)
        :type command: str
        :type func: function(params: list)
        :type description:  str
        """
        self._func_list[command] = {'func': func, 'description': description}

    def _render_help(self):
        """
        This function print in console all available commands
        Return: None
        """
        print('List of available commands')
        print('help - list all commands')
        print('exit - close the program')
        for command in self._func_list:
            print(f'{command} - {self._func_list[command]["description"]}')

    @staticmethod
    def _render_not_found(command):
        """
        This function warn user that he try to use a command that not exist
        Required: name of not found command
        Return: None
        """
        print(f'command "{command}" not found')

    @staticmethod
    def _render_welcome():
        print('Fundamentele Programarii UBB -> Lab4-6')

    def _read_commands(self):
        """
        This function read next command from terminal
        Return: command: str, params: list of str
        """
        # aux = input(self.cursor).split(' ')
        # return aux[0], aux[1:]

        commands = input(self.cursor).split(';')
        return commands

    def _parse_command(self, command_sting):
        command_sting = command_sting.lstrip(' ')
        aux = command_sting.split(' ')
        command = aux[0]
        params = aux[1:]
        params = list(filter(lambda x: x != '', params)) # remove extra spaces
        return command, params

    def start(self):
        """
        This function start the console
        """
        self._render_welcome()
        while True:
            commands = self._read_commands()
            for c in commands:
                command, params = self._parse_command(c)
                if command == self.exit_command:
                    exit()
                elif command == self.help_command:
                    self._render_help()
                elif command in self._func_list:
                    try:
                        self._func_list[command]['func'](params)
                    except Exception as e:
                        print(str(e))
                else:
                    self._render_not_found(command)
