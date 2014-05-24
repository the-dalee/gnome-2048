from gi.repository import Gtk
import os
from gi.overrides.GObject import GObject
from gi.overrides import Gdk


class ThemeSelectionController(object):
    def __init__(self, data_dir, user_config_dir):
        self._builder = Gtk.Builder() 
        glade_file = os.path.join(data_dir, "gui", "theme_selection.glade")

        self._builder.add_from_file(glade_file)
        self.window = self._builder.get_object("theme_selection_window")
        self.theme_store = self._builder.get_object("theme_selection_store")
        self.data_dir = data_dir
        self.user_config_dir = user_config_dir

        self.themes = self.get_theme_dictionary()
        self.theme_changed_observers = list()

    def get_theme_dictionary(self):
        global_themes_dir = os.path.join(self.data_dir, "themes", "")
        global_themes_dir = os.path.expanduser(global_themes_dir)
        
        user_themes_dir = os.path.join(self.user_config_dir, "themes", "")
        user_themes_dir = os.path.expanduser(user_themes_dir)
        
        global_themes = list()
        user_themes = list()

        try:
            global_themes = [(name, os.path.join(global_themes_dir, name))
                             for name in os.listdir(global_themes_dir)
                             if os.path.isdir(os.path.join(global_themes_dir, name))]
        except:
            global_themes = list()

        try:
            user_themes = [(name, os.path.join(user_themes_dir, name))
                           for name in os.listdir(user_themes_dir)
                           if os.path.isdir(os.path.join(user_themes_dir, name))]
        except:
            user_themes = list()

        return global_themes + user_themes

    def show(self):
        self.theme_store.clear()
        for theme in self.themes:
            self.theme_store.append((theme[0],))
        self.window.show()

    def register_theme_changed(self, observer):
        self.theme_changed_observers.append(observer)

    def notify_theme_changed(self, file):
        for o in self.theme_changed_observers:
            o.style_changed(file)
