from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp

class Panel:
    def __init__(self, manager_screen=None):
        self.menu: MDDropdownMenu = None
        self.manager_screen = manager_screen or MDApp.get_running_app().manager_screen

    def open_menu(self, menu_button):
        menu_items = []
        for item, method in {
            "Menu": lambda : self.open_screen("menu"),
            "Profile": lambda: self.open_screen("profile"),
            "View lists": lambda: self.open_screen("list"),
            "Create new element": lambda: self.open_screen("create"),
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

    def open_screen(self, screen_name):
        if self.manager_screen:
            self.manager_screen.switch_screen(screen_name)
        else:
            print("ManagerScreen is not set!")
        self.menu.dismiss()

    def switch_theme_style(self):
        app = MDApp.get_running_app()

        app.theme_cls.primary_palette = (
            "Darkblue" if app.theme_cls.primary_palette == "Indigo" else "Indigo"
        )

        app.theme_cls.theme_style = (
            "Dark" if app.theme_cls.theme_style == "Light" else "Light"
        )

        self.menu.dismiss()

    @staticmethod
    def exit_program():
        MDApp.get_running_app().stop()
