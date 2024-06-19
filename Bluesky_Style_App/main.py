from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
        self.root.ids.nav_drawer.set_state("close")


Example().run()
