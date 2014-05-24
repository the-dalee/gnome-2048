import gettext
import locale

current_locale, encoding = locale.getdefaultlocale()
locale.bindtextdomain('gnome-2048', 'locales')
t = gettext.translation('gnome-2048', 'locales/', 
                        [current_locale], fallback=True)
t.install()
_ = t.gettext
__ = t.ngettext

