from kivy.lang import Builder
from kivymd.app import MDApp


class Example(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')


Example().run()