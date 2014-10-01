#!/usr/bin/env python3
import sys
from gi.repository import Gtk, GObject, Gio
try:
    from gi.repository import AppIndicator3 as indicator
except:
    from gi.repository import AppIndicator as indicator
#import pymadisonmetro

class MadisonMetroIndicator:
    def __init__(self):
        self.ind = indicator.Indicator.new(
                "indicator-madisonmetro",
                "indicator-madisonmetro",
                indicator.IndicatorCategory.OTHER)
        self.ind.set_status(indicator.IndicatorStatus.ACTIVE)
        self.ind.set_icon("/home/fourwood/src/metro/indicator-madisonmetro/indicator-madisonmetro.png")

        self.UPDATE_INTERVAL = 1 * 60 * 1000 # min * s * ms

    def quit(self, widget):
        #print("Quit.")
        sys.exit(0)

    def add_menu_item(self, menu, label, callback=None):
        item = Gtk.MenuItem(label)
        if callback is not None:
            item.connect("activate", callback)
        item.show()
        menu.append(item)
        return item

    def menu_setup(self):
        #print("Menu setup.")
        self.menu = Gtk.Menu()

        separator = Gtk.SeparatorMenuItem()
        separator.show()
        self.menu.append(separator)

        self.quit_item = self.add_menu_item(self.menu, "Quit", self.quit)

        self.menu.show()
        self.ind.set_menu(self.menu)

    def main(self):
        self.timer = GObject.timeout_add(self.UPDATE_INTERVAL, self.menu_setup)
        self.menu_setup()
        Gtk.main()

if __name__ == "__main__":
    ind = MadisonMetroIndicator()
    ind.main()
