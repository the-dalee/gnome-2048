import gettext
import locale
from properties import Properties, Directories


current_locale, encoding = locale.getlocale()
locale.bindtextdomain(Properties.PACKAGE_NAME, Directories.APP_LOCALES)

t = gettext.translation(Properties.PACKAGE_NAME, Directories.APP_LOCALES,
                        [current_locale], fallback=True)

t.install()
_ = t.gettext
__ = t.ngettext
