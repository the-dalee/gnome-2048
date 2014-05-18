from gi.repository import Gtk, GObject, Notify
from core.engine import GameEngine
from gui.controllers import GameController


def main_func(resources_path):
    engine = GameEngine()
    GObject.threads_init()
    main_window_controller = GameController(engine, resources_path)
    main_window_controller.show()
    Gtk.main()