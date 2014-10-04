#!/usr/bin/env python3
import sys
from gi.repository import Gtk, GObject, Gio
try:
    from gi.repository import AppIndicator3 as indicator
except:
    from gi.repository import AppIndicator as indicator
import pymadisonmetro

keyfile = open('/home/fourwood/src/metro/indicator-madisonmetro/api.key', 'r')
API_KEY = keyfile.readline().strip()
keyfile.close()

_SECONDS = 1000
_MINUTES = 60 * _SECONDS
_HOURS = 60 * _MINUTES

class MadisonMetroIndicator:
    def __init__(self):
        self.ind = indicator.Indicator.new(
                "indicator-madisonmetro",
                "indicator-madisonmetro",
                indicator.IndicatorCategory.OTHER)
        self.ind.set_status(indicator.IndicatorStatus.ACTIVE)
        self.ind.set_icon("/home/fourwood/src/metro/indicator-madisonmetro/indicator-madisonmetro.png")

        self.UPDATE_INTERVAL = 1 * 60 * 1000 # min * s * ms

    def refresh(self, widget):
        pass

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

        stop_name_item = self.add_menu_item(self.menu, "Stop name.")

        arrival1 = self.add_menu_item(self.menu, "  Arrival 1.")
        arrival2 = self.add_menu_item(self.menu, "  Arrival 2.")
        arrival3 = self.add_menu_item(self.menu, "  Arrival 3.")

        separator = Gtk.SeparatorMenuItem()
        separator.show()
        self.menu.append(separator)

        self.refresh_item = self.add_menu_item(self.menu, "Refresh", self.refresh)
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
