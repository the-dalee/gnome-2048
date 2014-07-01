Gnome 2048
==================
Gnome 2048 is a Python port of the 2048 game by Gabriele Cirulli for GNOME and 
other GTK+ 3 compatible desktop environments. 

The source code of the application is licensed under the MIT License. You can 
use, modify or redistribute this software for both private and 
commercial purpose. For further information regarding the licensing, please 
see the COPYING file.

Requirements
==================
In order to run this application, you need a Linux machine with installed 
Python 3 interpreter, GNOME 3.8 and GTK+ and Python3-GI libraries.

Installation
==================
You can install Gnome 2048 by cloning or downloading the source code an running 
following commands in the source code directory:

```
sudo make
sudo make install
```

The starter icon will be automatically added to the Activities menu. The
application can be removed by executing ```sudo make uninstall``` in the source
directory root.

The packages for common Linux distributions will be available soon.

How to contribute?
==================

Coding
------------------
Currently there is no official roadmap for the Gnome 2048 project. Anyway if 
you have any ideas how to make it better, please feel free to send me a pull 
request with your changes. Just make sure to keep commits small and verbose. 
If you would like to modify the source code in some significant way, please send
me a short info before. 

Design
------------------
As I am not so good at design, there is still a lot to do in this field. The 
classic theme can still be improved to match the original one. Alternatively you
can create a new one. Just edit the resources/themes/classic/main.css file and
save the directory classic under new name. Please change the style of the game
board only and respect the user configured system theme for windows and widgets. 

The program icon also need some improvement. If you have any idea, how 
to make it better, just send me your suggestion as a .svg file.

Translations
-------------------
If you speak other languages than English, German or Polish, you can help
me translating the game. All improvements in the already available translations
are also appreciated.

If you are familiar with the gettext files, you can send me a pull request with 
translated po file based on the existing directory structure:

```locales/{LANG_CODE}/LC_MESSAGES/gnome-2048.po```


Contact
==================
If you have any questions, problems or ideas, you can contact me using my e-mail
address: mail.dalee@gmail.com. 