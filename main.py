import ctypes
from kivy.core.window import Window
from kivy.core.window import Window as KivyWindow
from kivy.utils import platform
from kivymd.app import MDApp
from View.ManagerScreen.manager_screen import ManagerScreen
from View.screens import screens

class CriticHub(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if platform == "win":
            user32 = ctypes.windll.user32
            screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        else:
            screen_width, screen_height = KivyWindow.system_size

        Window.size = (screen_width, screen_height)
        Window.top = 0
        Window.left = 0

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Darkblue"

        self.manager_screen = ManagerScreen()

    def build(self):
        for screen_name, (module_path, class_name) in screens.items():
            self.manager_screen.load_screen(module_path, class_name, screen_name)
        self.manager_screen.switch_screen("menu")

        return self.manager_screen


if __name__ == "__main__":
    CriticHub().run()
