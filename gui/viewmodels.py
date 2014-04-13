class GameViewModel(object):
    move_left_observers = []
    move_right_observers = []
    move_up_observers = []
    move_down_observers = []
    reset_observers = []
    undo_observers = []
    redo_observers = []

    def __init__(self):
        self.move_left_observers = list()
        self.move_right_observers = list()
        self.move_up_observers = list()
        self.move_down_observers = list()
        self.reset_observers = list()
        self.undo_observers = list()
        self.redo_observers = list()
        pass

    def notify_all(self, observers):
        for observer in observers:
            observer.notify()

    def notify_move_left(self):
        self.notify_all(self.move_left_observers)

    def notify_move_right(self):
        self.notify_all(self.move_right_observers)

    def notify_move_up(self):
        self.notify_all(self.move_up_observers)

    def notify_move_down(self):
        self.notify_all(self.move_down_observers)

    def notify_undo(self):
        self.notify_all(self.undo_observers)

    def notify_redo(self):
        self.notify_all(self.redo_observers)

    def notify_reset(self):
        self.notify_all(self.reset_observers)