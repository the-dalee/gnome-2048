import gettext
import locale
from argparse import ArgumentError
import os
exec_path = os.path.realpath(__file__)
exec_dir = os.path.dirname(exec_path)
locale.setlocale(locale.LC_ALL, '')
locales_dir = os.path.join(exec_dir, "locales", "")

current_locale, encoding = locale.getlocale()

locale.bindtextdomain('gnome-2048', locales_dir)

t = gettext.translation('gnome-2048', locales_dir, 
                        [current_locale], fallback=True)

t.install()
_ = t.gettext
__ = t.ngettext

