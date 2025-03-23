import ctypes
from kivy.core.window import Window
from kivy.core.window import Window as KivyWindow
from kivy.utils import platform

from kivy.lang import Builder
from kivy.app import App

from kivymd.uix.menu import MDDropdownMenu

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        id: root_box
        orientation: "horizontal"
        spacing: "12dp"
        padding: "12dp"

        MDIconButton:
            pos_hint: {"center_x": .5, "center_y": .98}
            on_release: app.open_menu(self)
            text: "Menu"
            icon: "menu"
"""


class Panel:
    menu: MDDropdownMenu = None

    def __init__(self):
        if platform == "win":
            user32 = ctypes.windll.user32
            screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        else:
            screen_width, screen_height = KivyWindow.system_size

        Window.size = (screen_width, screen_height)
        Window.top = 0
        Window.left = 0

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
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.primary_palette = (
            "White" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        self.menu.dismiss()

    @staticmethod
    def exit_program():
        App.get_running_app().stop()
