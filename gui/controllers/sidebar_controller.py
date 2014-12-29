from gi.overrides.Gtk import Gtk
from os import path
from properties import Directories, Properties


class SidebarController(object):
    def __init__(self, game_engine):
        self._builder = Gtk.Builder()
        glade_file = path.join(Directories.APP_GLADES, "sidebar.glade")
        self._builder.set_translation_domain(Properties.PACKAGE_NAME)
        self._builder.add_from_file(glade_file)
        self.widget = self._builder.get_object("sidebar")
        self.score_label = self._builder.get_object("score-label")
        self.engine = game_engine
        self.engine.register_for_commands(self)
        self.engine.register_for_undos(self)
        self.engine.register_for_redos(self)

    def update_score(self, score):
        self.score_label.set_text(str(score))

    def notify_command(self, command):
        self.update_score(self.engine.score)

    def notify_undo(self, job):
        self.update_score(self.engine.score)

    def notify_redo(self, job):
        self.update_score(self.engine.score)
