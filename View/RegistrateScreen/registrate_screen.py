from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

from database import create_user
from View.ManagerScreen.manager_screen import ManagerScreen

class RegistrateScreen(MDScreen):
    def __init__(self, manager_screen=None, **kwargs):
        super().__init__(**kwargs)
        self.manager_screen = ManagerScreen()
        self.manager_screen = manager_screen or MDApp.get_running_app().manager_screen

    def registrate_success(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if not username or not password:
            toast("Please fill in all the fields!")
            return

        success = create_user(username, password)

        if success:
            toast("Registration successful!")
            self.manager_screen.switch_screen("login")
        else:
            toast("Error: Username already exists")

    def open_login_screen(self):
        self.manager_screen.switch_screen("login")