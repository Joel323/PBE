import gi, threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class CustomWindow(Gtk.Window):
    uid = ""
    
    def __init__(self):
        super().__init__(title="RFID Reader")
        
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path("/home/pi/Desktop/PBE/css_style.css")
        styleContext = Gtk.StyleContext()
        styleContext.add_provider(cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
                                             cssProvider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)
        
        
        self.label = Gtk.Label()
        self.label.set_name("label1")
        self.label.set_text("Please, login with your university card")
        self.label.set_justify(Gtk.Justification.LEFT)
        
        

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box.pack_start(self.label, True, True, 0)
        #box_outer.pack_start(self.box, True, True, 0)
        
        outer_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        self.eventBox = Gtk.EventBox()
        self.button = Gtk.Button("Clear")
        self.button.connect("clicked", self.on_button_clicked)
        self.eventBox.add(self.button)
        self.box.pack_start(self.eventBox, True, True, 0)
        self.button.set_can_focus(False)

        self.connect("key_press_event", self.my_keypress_function)


    def on_button_clicked(self, widget):
        self.box.set_name("box")
        self.label.set_text("Please, login with your university card")
        self.uid = ""
    def my_keypress_function(self,widget, event):
        self.set_default(None)
        if(Gdk.keyval_name(event.keyval) == "Return"):
            self.box.set_name("box2")
            self.label.set_text("UID: " + self.uid)
        else:
            self.uid = self.uid + Gdk.keyval_name(event.keyval)
        
    	
        

win = CustomWindow()
win.connect("destroy", Gtk.main_quit)



win.show_all()
Gtk.main()
