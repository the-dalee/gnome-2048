from model.direction import Direction


class Board(object):
    tiles = {}

    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[(x, y)] = None

    def is_full(self):
        for x in self.width:
            for y in self.height:
                if self.tiles[(x, y)] == None:
                    return False
        return True

    def add(self, position, tile):
        if self.tiles[position] != None:
            raise Exception("The slot with this position "
                            + "contains already a tile")
        self.tiles[position] = tile

    def remove(self, position):
        if self.tiles[position] == None:
            raise Exception("The slot with this position "
                            + "is already empty")
        self.tiles[position] = None

    def move(self, old_position, new_position):
        tile = self.tiles[old_position]
        self.remove(old_position)
        self.add(new_position, tile)

    def next_by_predicate(self, position, direction, predicate):
        candidate = None
        if direction == Direction.Right:
            for i in range(position[0], self.width):
                if predicate((i, position[1])):
                    candidate = (i, position[1])

        if direction == Direction.Left:
            for i in range(self.width - 1, position[0] - 2, -1):
                if predicate((i, position[1] - 1)):
                    candidate = (i, position[1])

        if direction == Direction.Up:
            for i in range(position[1] - 1, self.height):
                if predicate((position[0], i)):
                    candidate = (position[0], i)

        if direction == Direction.Down:
            for i in range(self.height - 1, position[1] - 2, -1):
                if predicate((position[0], i)):
                    candidate = (position[0], i)

        return candidate
    
    def last_by_predicate(self, position, direction, predicate):
        candidate = None
        if direction == Direction.Right:
            for i in range(self.width - 1, position[0], -1):
                if predicate((i, position[1])):
                    candidate = (i, position[1])

        if direction == Direction.Left:
            for i in range(0, position[0] - 2):
                if predicate((i, position[1] - 1)):
                    candidate = (i, position[1])

        if direction == Direction.Up:
            for i in range(0, position[1] - 1):
                if predicate((position[0], i)):
                    candidate = (position[0], i)

        if direction == Direction.Down:
            for i in range(self.height - 1, position[1] - 2, -1):
                if predicate((position[0], i)):
                    candidate = (position[0], i)

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
