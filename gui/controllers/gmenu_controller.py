from gi.overrides.Gio import Gio

class GmenuController(object):
    def __init__(self, app):
        self.app = app

        self.menu = Gio.Menu()
        self.menu.append(_("About Gnome 2048"), "app.about")
        self.menu.append(_("Quit"), "app.quit")

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.about_cb)
        self.app.add_action(about_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.app.add_action(quit_action)

    def about_cb(self, action, parameter):
        self.app.show_about()

    def quit_cb(self, action, parameter):
        self.app.quit()

    def about_clicked(self):
        pass
