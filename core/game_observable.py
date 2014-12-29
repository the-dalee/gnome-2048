class GameObservable(object):
    def __init__(self):
        self.command_observers = list()
        self.job_observers = list()
        self.undo_observers = list()
        self.redo_observers = list()

    def register_for_commands(self, observer):
        self.command_observers.append(observer)

    def register_for_jobs(self, observer):
        self.job_observers.append(observer)

    def register_for_undos(self, observer):
        self.undo_observers.append(observer)

    def register_for_redos(self, observer):
        self.redo_observers.append(observer)

    def notify_command_observers(self, command):
        for observer in self.command_observers:
            observer.notify_command(command)

    def notify_job_observers(self, job):
        for observer in self.job_observers:
            observer.notify_job(job)

    def notify_undo_observers(self, job):
        for observer in self.undo_observers:
            observer.notify_undo(job)

    def notify_redo_observers(self, job):
        for observer in self.redo_observers:
            observer.notify_redo(job)
