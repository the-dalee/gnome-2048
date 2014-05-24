import gettext

t = gettext.translation('gnome-2048-1.0', 'locales/', fallback=True)

_ = t.gettext
__ = t.ngettext
