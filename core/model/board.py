from core.model.direction import Direction


class Board(object):
    tiles = {}

    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[(x, y)] = None

    def unmark_merged_all(self):
        for coord in self.tiles:
            if self.tiles[coord] is not None:
                self.tiles[coord].already_merged = False

    def is_full(self):
        for coords in self.tiles:
            if self.tiles[coords] == None:
                return False
        return True

    def add(self, position, tile):
        if self.tiles[position] != None:
            message = _("Slot with position %(pos)s already contains a tile")
            raise Exception(message % {"pos": str(position)})
        self.tiles[position] = tile

    def remove(self, position):
        if self.tiles[position] == None:
            message = _("The slot with this position %(pos)s is already empty")
            raise Exception(message % {"pos": str(position)})
        self.tiles[position] = None

    def move(self, old_position, new_position):
        tile = self.tiles[old_position]
        self.remove(old_position)
        self.add(new_position, tile)

    def next_by_predicate(self, position, direction, predicate):
        candidate = None
        if direction == Direction.Right:
            for i in range(position[0] + 1, self.width):
                if predicate((i, position[1])):
                    return (i, position[1])

        if direction == Direction.Left:
            for i in range(position[0] - 1, -1, -1):
                if predicate((i, position[1])):
                    return (i, position[1])

        if direction == Direction.Up:
            for i in range(position[1] - 1, -1, -1):
                if predicate((position[0], i)):
                    return (position[0], i)

        if direction == Direction.Down:
            for i in range(position[1] + 1, self.height):
                if predicate((position[0], i)):
                    return (position[0], i)

        return candidate

    def last_by_predicate(self, position, direction, predicate):
        candidate = None
        if direction == Direction.Right:
            for i in range(self.width - 1, position[0], -1):
                if predicate((i, position[1])):
                    return (i, position[1])

        if direction == Direction.Left:
            for i in range(0, position[0]):
                if predicate((i, position[1])):
                    return (i, position[1])

        if direction == Direction.Up:
            for i in range(0, position[1]):
                if predicate((position[0], i)):
                    return (position[0], i)

        if direction == Direction.Down:
            for i in range(self.height - 1, position[1], -1):
                if predicate((position[0], i)):
                    return (position[0], i)

        return candidate

    def next_free(self, position, direction):
        return self.last_by_predicate(position, direction, lambda x: self.tiles[x] == None)

    def next_full(self, position, direction):
        return self.next_by_predicate(position, direction, lambda x: self.tiles[x] != None)

    def get_empty_tiles(self):
        w = self.width
        h = self.height
        coords = [(x, y) for x in range(w) for y in range(h)]
        possible_cords = list()
        for coord in coords:
            if self.tiles[coord] is None:
                possible_cords.append(coord)
        return possible_cords
