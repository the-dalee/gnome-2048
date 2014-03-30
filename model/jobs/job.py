class Job(object):
    commands = []

    def __init__(self, commands):
        self.commands = list(commands)

    def add_commmand(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()
