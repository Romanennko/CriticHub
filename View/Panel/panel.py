from kivymd.uix.menu import MDDropdownMenu

from kivy.app import App


class Panel:
    def __init__(self, app):
        self.app = app
        self.menu: MDDropdownMenu = None

    def open_menu(self, menu_button):
        menu_items = []
        for item, method in {
            "Profile": lambda: self.open_screen_profile(),
            "View lists": lambda: self.open_screen_lists(),
            "Create new element": lambda: self.create_element(),
            "Switch theme style": lambda: self.switch_theme_style(),
            "Exit the program": lambda: self.exit_program(),
        }.items():
            menu_items.append(
                {
                    "text": item,
                    "on_release": method,
                }
            )
        self.menu = MDDropdownMenu(
            caller=menu_button,
            items=menu_items,
        )
        self.menu.open()

    def open_screen_profile(self):
        print("Profile screen opened")
        self.menu.dismiss()

    def open_screen_lists(self):
        print("Lists screen opened")
        self.menu.dismiss()

    def create_element(self):
        print("New element creation started")
        self.menu.dismiss()

    def switch_theme_style(self):
        theme_cls = self.app.theme_cls
        theme_cls.primary_palette = (
            "Darkblue" if theme_cls.primary_palette == "Orange" else "Orange"
        )
        theme_cls.theme_style = (
            "Dark" if theme_cls.theme_style == "Light" else "Light"
        )
        self.menu.dismiss()

    @staticmethod
    def exit_program():
        App.get_running_app().stop()