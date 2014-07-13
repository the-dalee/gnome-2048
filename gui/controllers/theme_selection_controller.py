from gi.repository import Gtk
import os
from properties import Directories, Properties


class ThemeSelectionController(object):
    def __init__(self):
        self._builder = Gtk.Builder()
        glade_file = os.path.join(Directories.APP_GLADES,
                                  "theme_selection.glade")

        self._builder.add_from_file(glade_file)
        self._builder.set_translation_domain(Properties.PACKAGE_NAME)
        self.window = self._builder.get_object("theme_selection_window")
        self.theme_store = self._builder.get_object("theme_selection_store")

        self.themes = self.get_theme_dictionary()
        self.theme_changed_observers = list()

    def get_theme_dictionary(self):
        global_themes = list()
        user_themes = list()

        try:
            global_themes = [(name, os.path.join(Directories.APP_THEMES, name))
                             for name in os.listdir(Directories.APP_THEMES)
                             if os.path.isdir(
                                        os.path.join(Directories.APP_THEMES, name))]
        except:
            global_themes = list()

        try:
            user_themes = [(name, os.path.join(Directories.USER_THEMES, name))
                           for name in os.listdir(Directories.USER_THEMES)
                           if os.path.isdir(
                                        os.path.join(Directories.USER_THEMES, name))]
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
