from kivymd.uix.screen import MDScreen

from View.Panel.panel import Panel

class ListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.panel = Panel()

    def open_menu(self, menu_button):
        self.panel.open_menu(menu_button)