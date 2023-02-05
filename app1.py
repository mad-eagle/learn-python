#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Hello, Linux!')
        self.button = Gtk.Button(label='Click Me')
        self.button.connect('clicked', self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print('Hello, Linux!')

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()