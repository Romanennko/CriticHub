from kivy.lang import Builder

from kivymd.app import MDApp

from panel import Panel, KV

class MainScreen(MDApp, Panel):
    def build(self):
        return Builder.load_string(KV)


MainScreen().run()