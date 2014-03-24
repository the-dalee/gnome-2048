from argparse import ArgumentError


class Tile(object):
    def __init__(self, value):
        self.value = value

    def merge(self, tile):
        if tile.value != self.value:
            raise ArgumentError(tile, "Source must have equal value as target")
        self.value = self.value + tile.value
