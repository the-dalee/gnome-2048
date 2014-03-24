from model.Direction import Direction


class Board(object):
    tiles = {}

    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        for x in self.width:
            for y in self.height:
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

    def next_by_condition(self, position, direction, condition):
        candidate = None
        if direction == Direction.Right:
            for i in range(position[0], self.width):
                if condition([(i, position[1])]):
                    candidate = (i, position[1])

        if direction == Direction.Left:
            for i in range(self.width, position[0], -1):
                if condition([(i, position[1])]):
                    candidate = (i, position[1])

        if direction == Direction.Bottom:
            for i in range(position[1], self.height):
                if condition(self.tiles[(position[0], i)]):
                    candidate = (position[0, i])

        if direction == Direction.Top:
            for i in range(self.height, position[1], -1):
                if condition(self.tiles[(position[0], i)]):
                    candidate = (position[0, i])

        return candidate

    def next_free(self, position, direction):
        return self.next_by_condition(position, direction, lambda x: x == None)

    def next_full(self, position, direction):
        return self.next_by_condition(position, direction, lambda x: x != None)
