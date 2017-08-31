import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title='Titulo')
        self.overlay = Gtk.Overlay()
        self.add(self.overlay)
        self.background = Gtk.Image.new_from_file('./Images/Fondo1.jpg')
        self.overlay.add(self.background)

        #grid
        self.grid=Gtk.Grid(row_spacing=70)


        #Label
        self.label=Gtk.Label()
        self.label.set_markup('<b><span size="50000" face="verdana" color="#7D2DD7">¡Ingresa tu envase!</span></b>' )
        self.label.set_halign(Gtk.Align.END)
        self.grid.attach(self.label,0,0,6,1)


        #boton1
        self.button=Gtk.Button(label='Empezar')
        self.button.get_child().set_markup('<span size="20000" face="verdana" color="#7D2DD7">¡Comenzar!</span>')
        #self.button.override_background_color()

        self.button.connect("clicked",self.button_clicked)
        self.button.set_size_request(200, 100)
        self.grid.attach(self.button,2,2,1,1)

        self.overlay.add_overlay(self.grid)
        self.grid.set_valign(Gtk.Align.CENTER)
        self.grid.set_halign(Gtk.Align.CENTER)


    def button_clicked(self,widget):
        print("hola")


window=MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
