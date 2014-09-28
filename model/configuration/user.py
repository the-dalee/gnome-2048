from properties import Directories


class UserConfig(object):
    theme = None

    def __init__(self):
        self.load_defaults()

    def load_defaults(self):
        self.theme = Directories.APP_DEFAULT_THEME
