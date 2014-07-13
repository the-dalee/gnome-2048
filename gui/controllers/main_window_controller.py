from core.model.direction import Direction
from gi.repository import Gtk
from gi.overrides import Gdk
from core.model.commands.engine import SetState
from core.model.game_state import GameState
from os import path
from properties import Directories, Properties


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

        self.window.connect("destroy", Gtk.main_quit)

        self.tile_00 = self._builder.get_object("tile00")
        self.tile_01 = self._builder.get_object("tile01")
        self.tile_02 = self._builder.get_object("tile02")
        self.tile_03 = self._builder.get_object("tile03")
        self.tile_10 = self._builder.get_object("tile10")
        self.tile_11 = self._builder.get_object("tile11")
        self.tile_12 = self._builder.get_object("tile12")
        self.tile_13 = self._builder.get_object("tile13")
        self.tile_20 = self._builder.get_object("tile20")
        self.tile_21 = self._builder.get_object("tile21")
        self.tile_22 = self._builder.get_object("tile22")
        self.tile_23 = self._builder.get_object("tile23")
        self.tile_30 = self._builder.get_object("tile30")
        self.tile_31 = self._builder.get_object("tile31")
        self.tile_32 = self._builder.get_object("tile32")
        self.tile_33 = self._builder.get_object("tile33")

        self.keyboard_box = self._builder.get_object("keyboard_box")

        self.msgOverlay = self._builder.get_object("board_overlay")
        self.msgOverlayLabel = Gtk.Label()
        self.msgOverlayLabel.set_halign(Gtk.Align.FILL)
        self.msgOverlayLabel.set_valign(Gtk.Align.FILL)
        self.msgOverlayLabel.get_style_context().add_class("message_overlay")
        self.msgOverlayLabel.size_request()
        self.msgOverlay.add_overlay(self.msgOverlayLabel)

        handlers = {
            "move_up_clicked": self.move_up_clicked,
            "move_down_clicked": self.move_down_clicked,
            "move_left_clicked": self.move_left_clicked,
            "move_right_clicked": self.move_right_clicked,
            "undo_clicked": self.undo_clicked,
            "redo_clicked": self.redo_clicked,
            "reset_clicked": self.reset_clicked,
            "exit_clicked": self.exit_clicked,
            "window_state_changed": self.window_state_changed,
            "key_released": self.key_released,
            "get_overlay_child_position": self.get_overlay_child_position,
            }
        self._builder.connect_signals(handlers)

        self.engine = game_engine
        self.engine.register(self)

        self.set_keyboard_visibility(False)

    def move_left_clicked(self, args):
        self.engine.move(Direction.Left)

    def move_right_clicked(self, args):
        self.engine.move(Direction.Right)

    def move_up_clicked(self, args):
        self.engine.move(Direction.Up)

    def move_down_clicked(self, args):
        self.engine.move(Direction.Down)

    def undo_clicked(self, args):
        self.engine.undo()
        self.display_tiles()
        self.show_hide_message()

    def redo_clicked(self, args):
        self.engine.redo()
        self.display_tiles()
        self.show_hide_message()

    def reset_clicked(self, args):
        self.engine.restart()
        self.engine.start()
        self.display_tiles()
        self.show_hide_message()

    def exit_clicked(self, args):
        self.window.close()
 
    def display_tiles(self):
        self.set_tile(self.tile_00, self.engine.board.tiles[0, 0])
        self.set_tile(self.tile_01, self.engine.board.tiles[0, 1])
        self.set_tile(self.tile_02, self.engine.board.tiles[0, 2])
        self.set_tile(self.tile_03, self.engine.board.tiles[0, 3])
        self.set_tile(self.tile_10, self.engine.board.tiles[1, 0])
        self.set_tile(self.tile_11, self.engine.board.tiles[1, 1])
        self.set_tile(self.tile_12, self.engine.board.tiles[1, 2])
        self.set_tile(self.tile_13, self.engine.board.tiles[1, 3])
        self.set_tile(self.tile_20, self.engine.board.tiles[2, 0])
        self.set_tile(self.tile_21, self.engine.board.tiles[2, 1])
        self.set_tile(self.tile_22, self.engine.board.tiles[2, 2])
        self.set_tile(self.tile_23, self.engine.board.tiles[2, 3])
        self.set_tile(self.tile_30, self.engine.board.tiles[3, 0])
        self.set_tile(self.tile_31, self.engine.board.tiles[3, 1])
        self.set_tile(self.tile_32, self.engine.board.tiles[3, 2])
        self.set_tile(self.tile_33, self.engine.board.tiles[3, 3])
        pass

    def set_tile(self, label, tile):
        label.get_style_context().remove_class("tile-2")
        label.get_style_context().remove_class("tile-4")
        label.get_style_context().remove_class("tile-8")
        label.get_style_context().remove_class("tile-16")
        label.get_style_context().remove_class("tile-32")
        label.get_style_context().remove_class("tile-64")
        label.get_style_context().remove_class("tile-128")
        label.get_style_context().remove_class("tile-256")
        label.get_style_context().remove_class("tile-512")
        label.get_style_context().remove_class("tile-1024")
        label.get_style_context().remove_class("tile-2048")  
        if tile is not None:
            if tile.value == 2:
                label.get_style_context().add_class("tile-2")
            elif tile.value == 4:
                label.get_style_context().add_class("tile-4")
            elif tile.value == 8:
                label.get_style_context().add_class("tile-8")
            elif tile.value == 16:
                label.get_style_context().add_class("tile-16")
            elif tile.value == 32:
                label.get_style_context().add_class("tile-32")
            elif tile.value == 64:
                label.get_style_context().add_class("tile-64")
            elif tile.value == 128:
                label.get_style_context().add_class("tile-128")
            elif tile.value == 256:
                label.get_style_context().add_class("tile-256")
            elif tile.value == 512:
                label.get_style_context().add_class("tile-512")
            elif tile.value == 1024:
                label.get_style_context().add_class("tile-1024")
            elif tile.value == 2048:
                label.get_style_context().add_class("tile-2048")

            label.set_text(str(tile.value))
        else:
            label.set_text("")

    def notify_command(self, command):
        print(command.description)
        self.display_tiles()

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

    def set_keyboard_visibility(self, visible):
        if visible:
            self.keyboard_box.show_all()
        else:
            self.keyboard_box.hide()

    def get_overlay_child_position(self, widget, rectangle, data):
        width = self.msgOverlay.get_allocated_width()
        height = self.msgOverlay.get_allocated_height()
        data.width = width
        data.height = height
        return True
