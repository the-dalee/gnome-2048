import gettext
import locale
from argparse import ArgumentError
import os

locale.setlocale(locale.LC_ALL, '')
current_locale, encoding = locale.getlocale()
locale.bindtextdomain('gnome-2048', 'locales')

exec_path = os.path.realpath(__file__)
exec_dir = os.path.dirname(exec_path)
locales_dir = os.path.join(exec_dir, "locales", "")
        
t = gettext.translation('gnome-2048', locales_dir, 
                        [current_locale], fallback=True)

t.install()
_ = t.gettext
__ = t.ngettext

