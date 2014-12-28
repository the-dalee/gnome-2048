from gi.overrides.Gtk import Gtk
from os import path
from properties import Directories, Properties


class BoardController(object):
    def __init__(self, game_engine):
        self._builder = Gtk.Builder()
        glade_file = path.join(Directories.APP_GLADES, "board.glade")
        self._builder.set_translation_domain(Properties.PACKAGE_NAME)
        self._builder.add_from_file(glade_file)

        self.engine = game_engine
        self.engine.register(self)

        self.widget = self._builder.get_object("board")

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
        self.display_tiles()