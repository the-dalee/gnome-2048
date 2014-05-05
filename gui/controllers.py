from core.engine import GameEngine
from core.model.direction import Direction


class GameController(object):
    def __init__(self):
        self.engine = GameEngine()

    def move_left_clicked(self):
        self.engine.move(Direction.Left)

    def move_right_clicked(self):
        self.engine.move(Direction.Right)

    def move_up_clicked(self):
        self.engine.move(Direction.Up)

    def move_down_clicked(self):
        self.engine.move(Direction.Down)

    def move_undo_clicked(self):
        self.engine.undo()

    def redo_clicked(self):
        self.engine.redo()

    def reset_clicked(self):
        self.engine.restart()
