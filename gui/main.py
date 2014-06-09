from gi.repository import Gtk, GObject, Gio
from core.engine import GameEngine
from gui.controllers.main_window_controller import MainWindowController
from gui.controllers.theme_selection_controller import ThemeSelectionController
import os
from gui.controllers import gmenu_controller
from gui.controllers.gmenu_controller import GmenuController


class Gnome2048Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

        exec_path = os.path.realpath(__file__)
        exec_dir = os.path.dirname(exec_path)
        resources_path = os.path.join(exec_dir, "../resources", "")
        user_resources_path = "~/.config/gnome-2048"

        engine = GameEngine()

        #self.theme_selection_controler = ThemeSelectionController(resources_path,
        #                                                 user_resources_path)
        #theme_selection_controller.window.set_transient_for(self.window)

        self.main_window_controller = MainWindowController(engine,
                                                  resources_path)

        self.gmenu_controller = GmenuController(self)


    def do_activate(self):
        self.set_app_menu(self.gmenu_controller.menu)
        self.main_window_controller.window.set_application(self)
        self.main_window_controller.show()

    def do_startup (self):
        Gtk.Application.do_startup(self)

    def show_about(self):
        pass
