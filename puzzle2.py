import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class CustomWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="RFID Reader")
        
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path("/home/pi/Desktop/PBE/css_style.css")
        styleContext = Gtk.StyleContext()
        styleContext.add_provider(cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
                                             cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)
        
        
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)
        
        label = Gtk.Label()
        label.set_text("Please, login with your university card")
        label.set_justify(Gtk.Justification.LEFT)
        
        
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)
        
        row = Gtk.ListBoxRow()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        vbox.pack_start(label, True, True, 0)
        vbox.set_child_packing(label, 0, 0, 50, 0)
        row.add(vbox)
        listbox.add(row)
        
        row2 = Gtk.ListBoxRow()
        self.button = Gtk.Button("Clear")
        self.button.connect("clicked", self.on_button_clicked)
        row2.add(self.button)
        listbox.add(row2)
        
    def on_button_clicked(self, widget):
        print("Hello World")
        

        

win = CustomWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()