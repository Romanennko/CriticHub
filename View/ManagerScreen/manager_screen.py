import os

from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager

class ManagerScreen(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_screen(self, screen, screen_name):
        if not self.has_screen(screen_name):
            self.add_widget(screen)

    def switch_screen(self, screen_name):
        if self.has_screen(screen_name):
            self.current = screen_name
        else:
            print(f"Screen '{screen_name}' not found!")

    def has_screen(self, screen_name):
        return screen_name in self.screen_names

    def load_screen(self, module_path, class_name, screen_name):
        try:
            module = __import__(module_path, fromlist=[class_name])
            screen_class = getattr(module, class_name)

            kv_path = os.path.join(*module_path.split(".")[:-1], f"{screen_name}_screen.kv")
            if os.path.exists(kv_path):
                Builder.load_file(kv_path)
            else:
                print(f"KV file not found: {kv_path}")

            screen = screen_class(name=screen_name)
            self.add_screen(screen, screen_name)
        except AttributeError as e:
            print(f"Error: Class {class_name} not found in module {module_path}. Exception: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error loading screen {screen_name}: {e}")
        print(f"Screens in Manager: {[screen.name for screen in self.screens]}")