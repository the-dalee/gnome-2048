from core.engine import GameEngine
from model.direction import Direction

def main_func():
    engine = GameEngine()
    engine.start()
    command = ""
    while command != "exit":
        if command == "left":
            engine.move(Direction.Left)
        if command == "right":
            engine.move(Direction.Right)
        if command == "up":
            engine.move(Direction.Up)
        if command == "down":
            engine.move(Direction.Down)
        if command == "undo":
            engine.undo()
        if command == "redo":
            engine.redo()
        print_board(engine.board)
        command = input("> ")


def print_board(board):
    for y in range(board.height):
        for x in range(board.width):
            if board.tiles[(x, y)] is None:
                print("----", end="|")
            else:
                value = board.tiles[(x, y)].value
                if value < 10:
                    print("--" + str(value) + "-", end="|")
                elif value < 100:
                    print("-" + str(value) + "-", end="|")
                elif value < 1000:
                    print("-" + str(value), end="|")
                else:
                    print(str(value), end="|")
        print("")
        
if __name__ == '__main__':
    main_func()
