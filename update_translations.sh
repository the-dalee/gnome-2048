#!/bin/sh
find .  -iregex "^.+\(.py\|.glade\)$" | xargs xgettext \
	-d gnome-2048 \
	-o locales/gnome-2048.pot \
	--package-name="gnome-2048" \
	--copyright-holder="Damian Lippok"
	
for file in `find .  -iregex "^.+\(.po\)$"` 
	do msgmerge -U $file locales/gnome-2048.pot
done
