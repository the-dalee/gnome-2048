from gi.overrides.Gio import Gio


class GmenuController(object):
    def __init__(self, app):
        self.app = app
        theme_section = Gio.Menu()
        theme_section.append(_("Select theme"), "app.select_theme")
        
        app_section = Gio.Menu()
        app_section.append(_("About Gnome 2048"), "app.about")
        app_section.append(_("Quit"), "app.quit")

        self.menu =  Gio.Menu()
        self.menu.append_section(None, theme_section)
        self.menu.append_section(None, app_section)
        
        select_theme_action = Gio.SimpleAction.new("select_theme", None)
        select_theme_action.connect("activate", self.select_theme_cb)
        self.app.add_action(select_theme_action)
        
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.about_cb)
        self.app.add_action(about_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.app.add_action(quit_action)

    def select_theme_cb(self, action, parameter):
        self.app.show_theme_selection()
        
    def about_cb(self, action, parameter):
        self.app.show_about()

    def quit_cb(self, action, parameter):
        self.app.quit()

    def about_clicked(self):
        pass
