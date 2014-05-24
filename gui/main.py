from gi.repository import Gtk, GObject, Notify
from core.engine import GameEngine
from gui.controllers import GameController
from gui.theme_selection_controller import ThemeSelectionController


def main_func(resources_path):
    engine = GameEngine()
    GObject.threads_init()
    
    theme_selection_controler = ThemeSelectionController(resources_path, "~/.config/gnome-2048")
    main_window_controller = GameController(engine, resources_path, theme_selection_controler)
    main_window_controller.show()
    Gtk.main()