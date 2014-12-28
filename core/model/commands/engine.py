import i18n


class EngineCommand(object):
    type = "Engine"
    description = "Do nothing with engine"

    def execute(self):
        pass

    def undo(self):
        pass


class AddScore(EngineCommand):
    def __init__(self, engine, score):
        self.engine = engine
        self.last_score = engine.score
        self.new_score = engine.score + score
        
        self.description = _("Add %(score)i points" %
            {
                "score": score,
            })

    def execute(self):
        self.engine.score = self.new_score

    def undo(self):
        self.engine.score = self.last_score


class SetState(EngineCommand):
    last_state = None
    new_state = None
    engine = None

    def __init__(self, engine, new_state):
        self.engine = engine
        self.last_state = engine.state
        self.new_state = new_state

        self.description = _("Set game state to %(state)s" %
                    {
                        "state": str(new_state),
                    })

    def execute(self):
        self.engine.state = self.new_state

    def undo(self):
        self.engine.state = self.last_state
