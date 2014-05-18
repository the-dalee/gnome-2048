#!/usr/bin/python3
from gui import main
import os

exec_path = os.path.realpath(__file__)
exec_dir = os.path.dirname(exec_path)
resources_path = os.path.join(exec_dir, "resources", "")
main.main_func(resources_path)

if __name__ == '__main__':
    pass