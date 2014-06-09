#!/usr/bin/python3
from gui import main
import os
from gui.main import Gnome2048Application
import sys

application = Gnome2048Application()
exit_status = application.run(sys.argv)
sys.exit(exit_status)   
