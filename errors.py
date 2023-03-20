

class InvalidCommand(Exception):
    def __init__(self, valid_commands):
        self.valid_commands=valid_commands
        
    def check(self, command):
        if (command not in self.valid_commands):
            return (f'El comando {command} no se reconoce como valido')
        else:
            return None