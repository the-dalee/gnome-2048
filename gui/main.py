from gi.repository import Gtk, GObject, Gio
from core.engine import GameEngine
from gui.controllers.main_window_controller import MainWindowController
from gui.controllers.theme_selection_controller import ThemeSelectionController
from os import path
from gui.controllers import gmenu_controller, about_controller
from gui.controllers.gmenu_controller import GmenuController
from gui.controllers.about_controller import AboutController
from properties import Directories


class Gnome2048Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
        engine = GameEngine()

        current_theme = "classic"
        style_file = path.join(Directories.APP_THEMES, current_theme, "main.css")
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(style_file)

        self.main_window_controller = MainWindowController(engine, css_provider)

        self.theme_selection_controller = ThemeSelectionController()
        self.theme_selection_controller.window.set_transient_for(self.main_window_controller.window)

        self.gmenu_controller = GmenuController(self)
        self.about_controller = AboutController()
        about_win = self.about_controller.window
        main_win = self.main_window_controller.window
        about_win.set_transient_for(main_win)

    def do_activate(self):
        self.set_app_menu(self.gmenu_controller.menu)
        self.main_window_controller.window.set_application(self)
        self.main_window_controller.show()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        
    def show_theme_selection(self):
        self.theme_selection_controller.show()

    def show_about(self):
        self.about_controller.show()
