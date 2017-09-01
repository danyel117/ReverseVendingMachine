#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Titulo')
        self.overlay = Gtk.Overlay()
        self.add(self.overlay)
        self.background = Gtk.Image.new_from_file('./Images/Fondo1.jpg')
        self.overlay.add(self.background)

        self.grid = Gtk.Grid(row_spacing=70)

        # Label
        self.label = Gtk.Label()
        self.label.set_markup('<b><span size="50000" face="verdana" color="#7D2DD7">¡Ingresa tu envase!</span></b>')
        self.label.set_halign(Gtk.Align.END)
        self.grid.attach(self.label, 0, 0, 6, 1)

        # boton1
        self.button = Gtk.Button(label='Empezar')
        #self.button.get_child().set_markup('<span size="20000" face="verdana" color="#7D2DD7">¡Comenzar!</span>')
        #self.button.override_background_color()

        self.button.connect("clicked", self.button_clicked)
        #self.button.set_size_request(200, 100)
        self.grid.attach(self.button, 2, 2, 1, 1)

        self.overlay.add_overlay(self.grid)
        self.grid.set_valign(Gtk.Align.CENTER)
        self.grid.set_halign(Gtk.Align.CENTER)

    def button_clicked(self, widget):
        print("Hello")


def main(argv):

    def gtk_style():
        css = b"""
* {
    transition-property: color, background-color, border-color, background-image, padding, border-width;
    transition-duration: 1s;
    font: Cantarell 20px;
}
GtkWindow {

}
.button {
    color: #7D2DD7;
    background-color: #bbb;
    border-style: solid;
    border-width: 5px 0 5px 5px;
    border-color: #bbb;
    padding: 12px 4px;
}
.button:first-child {
    border-radius: 10px 0 0 10px;
}
.button:last-child {
    border-radius: 0 5px 5px 0;
    border-width: 5px;
}
.button:hover {
    padding: 12px 48px;
    background-color: #4870bc;
}
.button *:hover {
    color: white;
}
.button:hover:active,
.button:active {
    background-color: #993401;
}
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    gtk_style()
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main(sys.argv)