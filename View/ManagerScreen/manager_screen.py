import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from View.screens import screens

class ManagerScreen(ScreenManager):
    _screen_names = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def create_screen(self, name_screen):
        if name_screen not in self._screen_names:
            self._screen_names.append(name_screen)
            self.load_common_package(name_screen)
            exec(f"import View.{screens[name_screen]}")
            self.app.load_all_kv_files(
                os.path.join(self.app.directory, "View", screens[name_screen.split(".")[0]])
            )
            view = eval(
                f'View.{screens[name_screen]}.{screens[name_screen].split(".")[0]}View()'
            )
            view.name = name_screen

            return view

    def load_common_package(self, name_screen) -> None:
        def _load_kv(path_to_kv):
            if not any(path_to_kv in loaded_path_kv for loaded_path_kv in Builder.files):
                print(f"Loading KV file: {path_to_kv}")
                Builder.load_file(path_to_kv)

        kv_paths = {
            "registrate": os.path.join("View", "RegistrateScreen", "registrate_screen.kv"),
            "login": os.path.join("View", "LoginScreen", "login_screen.kv"),
            "menu": os.path.join("View", "MenuScreen", "menu_screen.kv"),
            "list": os.path.join("View", "ListScreen", "list_screen.kv"),
            "profile": os.path.join("View", "ProfileScreen", "profile_screen.kv"),
            "create": os.path.join("View", "CreateElementScreen", "create_element_screen.kv"),
        }

        if name_screen in kv_paths:
            _load_kv(kv_paths[name_screen])
