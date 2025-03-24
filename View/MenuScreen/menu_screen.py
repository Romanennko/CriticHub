from kivymd.uix.screen import MDScreen

from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDIconButton

from View.Panel.panel import Panel


class MenuScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.panel = Panel(self)

        layout = BoxLayout(
            orientation="horizontal",
            spacing="12dp",
            padding="12dp",
        )

        menu_button = MDIconButton(
            text="Menu",
            icon="menu",
            pos_hint={"center_x": 0.5, "center_y": 0.98},
            on_release=lambda instance: self.panel.open_menu(instance),
        )

        layout.add_widget(menu_button)
        self.add_widget(layout)
