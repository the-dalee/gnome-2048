NAME = gnome-2048
BINDIR = $(DESTDIR)/usr/game
TARGET = $(DESTDIR)/usr/share/games/$(NAME)

RESOURCE = $(DESTDIR)/usr/share/$(NAME)/resources
GLADES = $(TARGET)/resources/gui
THEMES = $(TARGET)/resources/themes

LOCALES = $(TARGET)/locales

PIXMAPS = $(DESTDIR)/usr/share/pixmaps
APPLICATIONS = $(DESTDIR)/usr/share/applications

%.mo: %.po
	msgfmt -cv -o $@ $< 

build-translations:
	#find .  -iregex "^.+\(.py\|.glade\)$$" | xargs xgettext \
	#	-d gnome-2048 \
	#	-o locales/gnome-2048.pot \
	#	--package-name="gnome-2048" \
	#	--copyright-holder="Damian Lippok"
	#
	#for file in `find .  -iregex "^.+\(.po\)$$"` do \
	#	msgmerge -U $$file locales/gnome-2048.pot \
	#	done 

all: build-translations

install: all
	mkdir -p $(BINDIR)
	mkdir -p $(TARGET)
	
	mkdir -p $(RESOURCE)
	mkdir -p $(GLADES)
	mkdir -p $(THEMES)
	
	mkdir -p $(PIXMAPS)
	mkdir -p $(APPLICATIONS)
	
	mkdir -p $(LOCALES)/de_DE/LC_MESSAGES/
	
	mkdir -p $(THEMES)/classic/
	
	rsync -rupE core $(TARGET)
	rsync -rupE gui $(TARGET)
	rsync -rupE resources $(DESTDIR)/resources/
	install --mode=755 gnome-2048.py $(TARGET)
	install --mode=755 i18n.py $(TARGET)
	
	install --mode=744 locales/de_DE/LC_MESSAGES/*.mo $(LOCALES)/de_DE/LC_MESSAGES/
	

	install --mode=744 resources/gui/*.glade $(GLADES) 
	
	install --mode=744 resources/themes/classic/*.css $(THEMES)/classic/
	
	#install --mode=744 environment/Pyhello.desktop $(APPLICATIONS)
	#install --mode=744 environment/pyhello.png $(PIXMAPS)
	ln -s $(TARGET)/$(NAME).py $(BINDIR)/$(NAME)

clean:
	rm -fr .temp
	
uninstall:
	rm -rf $(TARGET)
	rm -rf $(RESOURCE)
	rm $(BINDIR)/$(NAME)
	#rm $(PIXMAPS)/pyhello.png
	#rm $(APPLICATIONS)/Pyhello.desktop
	
.PHONY: install
.PHONY: uninstall
.PHONY: clean
.PHONY: build-translations
