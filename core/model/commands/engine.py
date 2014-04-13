class EngineCommand(object):
    type = "Engine"
    description = "Do nothing with engine"

    def execute(self):
        pass

    def undo(self):
        pass


class SetState(EngineCommand):
    last_state = None
    new_state = None
    engine = None

    def __init__(self, engine, new_state):
        self.engine = engine
        self.last_state = engine.state
        self.new_state = new_state

        self.description = "Set game state to " + str(new_state)

    def execute(self):
        self.engine.state = self.new_state

    def undo(self):
        self.engine.state = self.last_state
