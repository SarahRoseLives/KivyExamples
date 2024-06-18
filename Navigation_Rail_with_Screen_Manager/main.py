from kivy.lang import Builder
from kivymd.app import MDApp



class Example(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def switch_screen(self, screen_name):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name


Example().run()
