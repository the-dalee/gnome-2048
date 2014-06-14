from gi.repository import Gtk
import os
from propeties import Properties


class AboutController(object):
    def __init__(self, data_dir):
        self._builder = Gtk.Builder()
        self._builder.set_translation_domain("gnome-2048")

        glade_file = os.path.join(data_dir, "gui", "about.glade")
        self._builder.add_from_file(glade_file)
        self.window = self._builder.get_object("about_window")
        self.window.set_decorated(True)
        self.window.set_version(Properties.VERSION)
        self.window.set_name(Properties.NAME)
        self.window.set_copyright(Properties.COPYRIGHT)
        
    def show(self):
        self.window.run()
        self.window.hide()
