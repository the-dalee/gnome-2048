from os import path


class Properties:
    NAME = "Gnome 2048"
    PACKAGE_NAME = "gnome-2048"
    VERSION = "0.8.0"
    COPYRIGHT = "Copyright © 2014 Damian Lippok"


class Directories:
    APPLICATION = path.dirname(path.realpath(__file__))

    APP_GLADES = path.join(APPLICATION, "gui", "views", "")
    APP_RESOURCES = path.join(APPLICATION, "resources", "")
    APP_LOCALES = path.join(APPLICATION, "locales", "")

    APP_THEMES = path.join(APP_RESOURCES, "themes", "")

    USER_CONFIG_DIR = path.join(path.expanduser("~"),
                                ".config",
                                Properties.PACKAGE_NAME, "")
    USER_THEMES = path.join(USER_CONFIG_DIR, "themes", "")
