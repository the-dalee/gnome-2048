from core.model.direction import Direction
from gi.repository import Gtk
from gi.overrides import Gdk
from core.model.commands.engine import SetState
from core.model.game_state import GameState
from os import path
from properties import Directories, Properties
from gui.controllers.board_controller import BoardController
from gui.controllers.sidebar_controller import SidebarController


class MainWindowController(object):
    def __init__(self, game_engine, css_provider):
        self._builder = Gtk.Builder()

        glade_file = path.join(Directories.APP_GLADES, "main.glade")
        self._builder.set_translation_domain(Properties.PACKAGE_NAME)
        self._builder.add_from_file(glade_file)
        self.window = self._builder.get_object("main_window")

        context = Gtk.StyleContext()
        context.add_provider_for_screen(self.window.get_screen(),
                                        css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_USER)

        self.window.connect("destroy", self.destroy)
        
        self.board = BoardController(game_engine)
        self.sidebar = SidebarController(game_engine)
        
        self.tgl_show_sidebar = self._builder.get_object("toggle_show_sidebar")
        self.tgl_show_sidebar.set_active(self.sidebar.visible)
        
        self.msgOverlay = self._builder.get_object("board_overlay")
        self.msgOverlayLabel = Gtk.Label()
        self.msgOverlayLabel.set_halign(Gtk.Align.FILL)
        self.msgOverlayLabel.set_valign(Gtk.Align.FILL)
        self.msgOverlayLabel.get_style_context().add_class("message_overlay")
        self.msgOverlayLabel.size_request()
        self.msgOverlay.add_overlay(self.msgOverlayLabel)#
        
        self.button_undo = self._builder.get_object("button_undo")
        self.button_redo = self._builder.get_object("button_redo")
        
        self.board_box = self._builder.get_object("board_box")
        self.board_box.add(self.board.widget)
        self.board_box.add(self.sidebar.widget)

        handlers = {
            "undo_clicked": self.undo_clicked,
            "redo_clicked": self.redo_clicked,
            "reset_clicked": self.reset_clicked,
            "exit_clicked": self.exit_clicked,
            "window_state_changed": self.window_state_changed,
            "key_released": self.key_released,
            "get_overlay_child_position": self.get_overlay_child_position,
            "show_sidebar_toggled": self.show_sidebar_toggled,
            }
        self._builder.connect_signals(handlers)

        self.engine = game_engine
        self.engine.register_for_commands(self)
        self.engine.register_for_undos(self)
        self.engine.register_for_redos(self)
        self.engine.register_for_reset(self)
        self.engine.register_for_jobs(self)

    def destroy(self, e):
        self.engine.quit()
        Gtk.main_quit()

    def undo_clicked(self, args):
        self.engine.undo()
        self.board.display_tiles()
        self.show_hide_message()

    def redo_clicked(self, args):
        self.engine.redo()
        self.board.display_tiles()
        self.show_hide_message()

    def reset_clicked(self, args):
        self.engine.restart()
        self.engine.start()
        self.board.display_tiles()
        self.show_hide_message()

    def exit_clicked(self, args):
        self.window.close()

    def show_sidebar_toggled(self, sender):
        self.sidebar.set_visible(sender.get_active())
        self.window.queue_resize()

    def notify_command(self, command):
        print(command.description)
        if isinstance(command, SetState):
            self.show_hide_message()

    def show_hide_message(self):
        if self.engine.state == GameState.Lost:
            self.msgOverlayLabel.set_text(_("Game over"))
            self.msgOverlayLabel.show_all()
        elif self.engine.state == GameState.Won:
            self.msgOverlayLabel.set_text(_("You won"))
            self.msgOverlayLabel.show_all()
        else:
            self.msgOverlayLabel.hide()

    def show(self):
        self.window.show()
        self.engine.start()

    def toggle_maximize(self):
        if self.maximized:
            self.window.unmaximize()
        else:
            self.window.maximize()

    def window_state_changed(self, window, args):
        new_state = args.new_window_state
        if new_state & Gdk.Gdk.WindowState.MAXIMIZED:
            self.maximized = True
        else:
            self.maximized = False

    def key_released(self, window, args):
        keycode = args.get_keycode()[1]
        if keycode == 111:
            self.move(Direction.Up)
        if keycode == 113:
            self.move(Direction.Left)
        if keycode == 114:
            self.move(Direction.Right)
        if keycode == 116:
            self.move(Direction.Down)

    def move(self, direction):
        if (self.engine.state == GameState.InProgress or
            self.engine.state == GameState.Pending):
            self.engine.move(direction)

    def get_overlay_child_position(self, widget, rectangle, data):
        width = self.msgOverlay.get_allocated_width()
        height = self.msgOverlay.get_allocated_height()
        data.width = width
        data.height = height
        return True

    def set_undo_redo_buttons_sensitivity(self):
        if(self.engine.undo_stack):
            self.button_undo.set_sensitive(True)
        else:
            self.button_undo.set_sensitive(False)

        if(self.engine.redo_stack):
            self.button_redo.set_sensitive(True)
        else:
            self.button_redo.set_sensitive(False)

    def notify_job(self, job):
        self.set_undo_redo_buttons_sensitivity()

    def notify_undo(self, job):
        self.set_undo_redo_buttons_sensitivity()

    def notify_redo(self, job):
        self.set_undo_redo_buttons_sensitivity()

    def notify_reset(self):
        self.set_undo_redo_buttons_sensitivity()
