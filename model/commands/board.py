class BoardTile(object):
    type = "Board"
    description = "Do nothing with board"

    def execute(self):
        pass

    def undo(self):
        pass


class MoveTile(BoardTile):
    source = None
    destination = None
    board = None
    description = "Move tile"

    def __init__(self, board, source, destination):
        self.source = source
        self.destination = destination
        self.board = board

        descriptionText = "Move tile from (%(sx)i, %(sy)i) to (%(dx)i, %(dy)i)"
        self.description = descriptionText % {
                    "sx": source[0],
                    "sy": source[1],
                    "dx": destination[0],
                    "dy": destination[1]
                }

    def execute(self):
        self.board.move(self, self.source, self.destination)

    def undo(self):
        self.board.move(self, self.destination, self.source)


class MergeTile(BoardTile):
    source = None
    destination = None
    sourceTile = None
    destinationTile = None
    board = None

    def __init__(self, board, source, destination):
        self.source = source
        self.destination = destination
        self.sourceTile = board.tiles[source]
        self.destinationTile = board.tiles[destination]
        self.board = board

        descriptionText = "Merge tile at (%(x)i, %(y)i) with (%(dx)i, %(dy)i)"
        self.description = descriptionText % {
                    "x": source[0],
                    "y": source[1],
                    "dx": destination[0],
                    "dy": destination[1]
                }

    def execute(self):
        self.destinationTile.merge(self.sourceTile)
        self.board.remove(self.source)

    def undo(self):
        self.destinationTile.value = self.destinationTile.value / 2
        self.board.add(self.source, self.sourceTile)


class AddTile(BoardTile):
    position = None
    tile = None
    board = None

    def __init__(self, board, position, tile):
        self.position = position
        self.tile = tile
        self.board = board

        descriptionText = "Add tile %(val)i at (%(x)i, %(y)i)"
        self.description = descriptionText % {
                    "x": position[0],
                    "y": position[1],
                    "val": tile.value
                }

    def execute(self):
        self.board.add(self.position, self.tile)

    def undo(self):
        self.board.remove(self.position)


class RemoveTile(BoardTile):
    position = None
    tile = None
    board = None

    def __init__(self, board, position):
        self.position = position
        self.tile = self.board.tiles[position]
        self.board = board

        descriptionText = "Remove tile at (%(x)i, %(y)i)"
        self.description = descriptionText % {
                    "x": position[0],
                    "y": position[1]
                }

    def execute(self):
        self.board.remove(self.position)

    def undo(self):
        self.board.add(self.position, self.tile)
