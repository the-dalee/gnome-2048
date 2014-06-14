#!/usr/bin/python3
from gui import main
import os
from gui.main import Gnome2048Application
import sys
import i18n
from properties import Properties

if "--version" in sys.argv:
    print(Properties.NAME, Properties.VERSION)

else:
    application = Gnome2048Application()
    exit_status = application.run(sys.argv)
    sys.exit(exit_status)   
