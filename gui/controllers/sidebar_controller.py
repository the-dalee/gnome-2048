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
        self.time_label = self._builder.get_object("time-label")
        self.engine = game_engine

        self.visible = True

        self.engine.register_for_commands(self)
        self.engine.register_for_undos(self)
        self.engine.register_for_redos(self)
        self.engine.register_for_reset(self)
        self.engine.register_for_timer(self)

    def set_visible(self, value):
        self.widget.set_visible(value)
        self._visible = value

    def get_visible(self):
        return self._visible

    visible = property(get_visible, set_visible)


    def update_score(self, score):
        self.score_label.set_text(str(score))

    def update_time(self, time):
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        self.time_label.set_text("%d:%02d:%02d" % (h, m, s))

    def notify_command(self, command):
        self.update_score(self.engine.score)

    def notify_undo(self, job):
        self.update_score(self.engine.score)

    def notify_redo(self, job):
        self.update_score(self.engine.score)

    def notify_reset(self):
        self.update_time(0)
        self.update_score(self.engine.score)

    def notify_timer(self, time):
        self.update_time(time)
