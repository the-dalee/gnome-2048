class Job(object):
    commands = []

    def __init__(self, commands=None):
        if commands is None:
            self.commands = list()
        else:
            self.commands = list(commands)

    def add_commmand(self, command):
        if command is not None:
            self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()
