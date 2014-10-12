NAME = gnome-2048
BINDIR = $(DESTDIR)/usr/games
TARGET = $(DESTDIR)/usr/share/games/$(NAME)

GLADES = $(TARGET)/resources/gui
THEMES = $(TARGET)/resources/themes

LOCALES = $(TARGET)/locales

PIXMAPS = $(DESTDIR)/usr/share/pixmaps
ICONS = $(DESTDIR)/usr/share/icons/hicolor
APPLICATIONS = $(DESTDIR)/usr/share/applications
APPDATA = $(DESTDIR)/usr/share/appdata

all: build-translations


%.mo: %.po
	msgfmt -cv -o $@ $< 
	
build-translations: ./locales/de_DE/LC_MESSAGES/gnome-2048.mo

install: all
	mkdir -p $(BINDIR)
	mkdir -p $(TARGET)
	
	mkdir -p $(GLADES)
	mkdir -p $(THEMES)
	
	mkdir -p $(ICONS)/scalable/apps
	mkdir -p $(APPLICATIONS)
	
	mkdir -p $(LOCALES)/de_DE/LC_MESSAGES/
	
	mkdir -p $(THEMES)/classic/
	
	rsync -rupE core $(TARGET)
	rsync -rupE gui $(TARGET)
	rsync -rupE model $(TARGET)
	rsync -rupE resources $(DESTDIR)/resources/
	
	install --mode=755 gnome-2048.py $(TARGET)
	install --mode=755 i18n.py $(TARGET)
	install --mode=755 properties.py $(TARGET)
		
	install --mode=744 locales/de_DE/LC_MESSAGES/*.mo $(LOCALES)/de_DE/LC_MESSAGES/
	
	install --mode=744 resources/themes/classic/* $(THEMES)/classic/
	
	install --mode=744 environment/gnome-2048.desktop $(APPLICATIONS)
	install --mode=744 environment/gnome-2048.appdata.xml $(APPDATA)
	install --mode=744 environment/icons/hicolor/scalable/apps/gnome-2048.svg $(ICONS)/scalable/apps
	ln -s $(TARGET)/$(NAME).py $(BINDIR)/$(NAME)

	
clean:
	find .  -iregex "^.+\.mo" | xargs rm -f
	find .  -iregex "^.+\~" | xargs rm -f
	rm -fr .temp 
	
uninstall:
	rm -rf $(TARGET)
	rm $(BINDIR)/$(NAME)
	rm $(ICONS)/scalable/apps/gnome-2048.svg
	rm $(APPLICATIONS)/gnome-2048.desktop
	rm $(APPDATA)/gnome-2048.appdata.xml
	
	
.PHONY: install
.PHONY: uninstall
.PHONY: clean
.PHONY: build-translations
