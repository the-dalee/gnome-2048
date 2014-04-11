from model.board import Board
from model.game_state import GameState
from model.direction import Direction
from random import Random
from model.tile import Tile
from model.commands.board import AddTile, MoveTile, MergeTile
from model.jobs.job import Job


class GameEngine(object):
    undo_stack = []
    redo_stack = []

    def __init__(self):
        self.restart()
        self.undo_stack = list()
        self.redo_stack = list()

    def execute(self, job):
        self.undo_stack.append(job)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            job = self.undo_stack.pop()
            job.undo()
            self.redo_stack.append(job)
        else:
            print("Undo stack empty")

    def redo(self):
        if self.redo_stack:
            job = self.redo_stack.pop()
            job.execute()
            self.undo_stack.append(job)
        else:
            print("Redo stack empty")

    def restart(self):
        self.board = Board()
        self.state = GameState.Pending
        self.points = 0

    def is_game_over(self):
        if not self.board.is_full():
            return False
        for x in range(self.board.width):
            for y in range(self.board.height):
                tile = self.board.tiles[(x, y)]
                next_coord = self.board.next_full((x, y), Direction.Right)
                if next_coord is not None:
                    if self.board.tiles[next_coord].value == tile.value:
                        return False
                next_coord = self.board.next_full((x, y), Direction.Left)
                if next_coord is not None:
                    if self.board.tiles[next_coord].value == tile.value:
                        return False
                next_coord = self.board.next_full((x, y), Direction.Up)
                if next_coord is not None:
                    if self.board.tiles[next_coord].value == tile.value:
                        return False
                next_coord = self.board.next_full((x, y), Direction.Down)
                if next_coord is not None:
                    if self.board.tiles[next_coord].value == tile.value:
                        return False
        return True

    def move(self, direction):
        coords = []
        w = self.board.width
        h = self.board.height
        if direction == Direction.Right:
            coords = [(x, y) for x in range(w - 1, -1, -1) for y in range(h)]
        if direction == Direction.Left:
            coords = [(x, y) for x in range(w) for y in range(h)]
        if direction == Direction.Up:
            coords = [(x, y) for x in range(w) for y in range(h)]
        if direction == Direction.Down:
            coords = [(x, y) for x in range(w) for y in range(h - 1, -1, -1)]

        job = Job()
        for coord in coords:
            tile = self.board.tiles[coord]
            if tile is not None:
                next_full = self.board.next_full(coord, direction)
                if (next_full is not None) and (self.board.tiles[next_full].value == tile.value): 
                    merge_command = MergeTile(self.board, coord, next_full)
                    merge_command.execute()
                    job.add_commmand(merge_command)
                else:
                    next_empty = self.board.next_free(coord, direction)
                    if next_empty is not None:
                        move_command = MoveTile(self.board, coord, next_empty)
                        move_command.execute()
                        job.add_commmand(move_command)

        empty_tiles = self.board.get_empty_tiles() 
        if empty_tiles:
            random = Random()
            first_empty = random.choice(empty_tiles)
            add_cmd = AddTile(self.board, first_empty, Tile(2))
            add_cmd.execute()
            job.add_commmand(add_cmd)

        self.execute(job)

    def start(self):
        job = Job()
        random = Random()
        empty_tiles = self.board.get_empty_tiles()
        if empty_tiles:
            first_empty = random.choice(empty_tiles)
            add_first = AddTile(self.board, first_empty, Tile(2))
            add_first.execute()
            job.add_commmand(add_first)
            empty_tiles.remove(first_empty)
        if empty_tiles:
            second_empty = random.choice(empty_tiles)
            add_second = AddTile(self.board, second_empty, Tile(2))
            add_second.execute()
            job.add_commmand(add_second)
        self.execute(job)
