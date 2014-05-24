#!/bin/sh
find .  -iregex "^.+\(.py\|.glade\)$" | xargs xgettext \
	-d gnome-2048-1.0 \
	-o locales/gnome-2048.pot \
	--package-name="gnome-2048" \
	--copyright-holder="Damian Lippok"
