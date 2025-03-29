from kivy.core.window import Window
from kivymd.app import MDApp
from View.ManagerScreen.manager_screen import ManagerScreen
from View.screens import screens

class CriticHub(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.fullscreen = "auto"

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
