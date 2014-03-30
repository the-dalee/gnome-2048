from core.engine import GameEngine
from model.direction import Direction

def main_func():
    engine = GameEngine()
    engine.spawn()
    engine.spawn()
    
    command = ""
    while command != "exit":
        print_board(engine.board)
        if command == "left":
            engine.move(Direction.Left)
            engine.spawn()
        if command == "right":
            engine.move(Direction.Right)
            engine.spawn()
        if command == "up":
            engine.move(Direction.Up)
            engine.spawn()
        if command == "down":
            engine.move(Direction.Down)
            engine.spawn()
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
