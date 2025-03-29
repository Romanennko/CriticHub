from kivymd.uix.screen import MDScreen
from View.ManagerScreen.manager_screen import ManagerScreen
from kivymd.app import MDApp

class LoginScreen(MDScreen):

    def __init__(self, manager_screen=None, **kwargs):
        super().__init__(**kwargs)
        self._user_logged_in = False
        self.manager_screen = ManagerScreen()
        self.manager_screen = manager_screen or MDApp.get_running_app().manager_screen

    @property
    def user_logged_in(self):
        return self._user_logged_in

    def login_success(self):
        self._user_logged_in = True
        self.manager_screen.switch_screen("menu")