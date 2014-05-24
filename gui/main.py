from gi.repository import Gtk, GObject
from core.engine import GameEngine
from gui.controllers.main_window_controller import MainWindowController
from gui.controllers.theme_selection_controller import ThemeSelectionController


def main_func(resources_path):
    user_resources_path = "~/.config/gnome-2048"

    engine = GameEngine()
    GObject.threads_init()

    theme_selection_controler = ThemeSelectionController(resources_path,
                                                         user_resources_path)
    main_window_controller = MainWindowController(engine,
                                                  resources_path,
                                                  theme_selection_controler)
    main_window_controller.show()
    Gtk.main()
