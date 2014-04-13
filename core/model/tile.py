from argparse import ArgumentError


class Tile(object):
    already_merged = False

    def __init__(self, value):
        self.value = value
        self.already_merged = False

    def merge(self, tile):
        if tile.value != self.value:
            raise ArgumentError(tile, "Source must have equal value as target")
        self.value = self.value + tile.value
