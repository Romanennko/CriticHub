import json
import os

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

from database import check_credentials, check_user_exists
from View.ManagerScreen.manager_screen import ManagerScreen

SESSION_FILE = "user_session.json"

class LoginScreen(MDScreen):

    def __init__(self, manager_screen=None, **kwargs):
        super().__init__(**kwargs)
        self.manager_screen = ManagerScreen()
        self.manager_screen = manager_screen or MDApp.get_running_app().manager_screen
        self.auto_login()

    def is_logged_in(self):
        if os.path.exists(SESSION_FILE):
            try:
                with open(SESSION_FILE, "r") as f:
                    data = json.load(f)
                    return "username" in data
            except (json.JSONDecodeError, KeyError):
                os.remove(SESSION_FILE)
        return False

    def login_success(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if not username or not password:
            toast("Please fill in all the fields!")
            return

        if check_credentials(username, password):
            self.save_session(username)
            toast(f"Welcome, {username}!")
            self.manager_screen.switch_screen("menu")
        else:
            toast("Invalid username or password!")

    def open_registrate_screen(self):
        self.manager_screen.switch_screen("registrate")

    def auto_login(self):
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, "r") as f:
                data = json.load(f)
                username = data.get("username")

                if username and check_user_exists(username):
                    toast(f"Welcome back, {username}!")
                    self.manager_screen.switch_screen("menu")
                else:
                    os.remove(SESSION_FILE)

    def save_session(self, username):
        with open(SESSION_FILE, "w") as f:
            json.dump({"username": username}, f)

    def logout(self):
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)
        self.manager_screen.switch_screen("login")