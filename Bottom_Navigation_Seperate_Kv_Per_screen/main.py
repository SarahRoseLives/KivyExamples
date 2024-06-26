from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MainScreen(MDScreen):
    pass

class MDScreen1(MDScreen):
    pass

class MDScreen2(MDScreen):
    pass

class MDScreen3(MDScreen):
    pass

class Example(MDApp):
    def build(self):
        # Load the main kv file containing the bottom navigation
        Builder.load_file("main.kv")
        # Load each screen's kv file
        Builder.load_file("screen1.kv")
        Builder.load_file("screen2.kv")
        Builder.load_file("screen3.kv")

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return MainScreen()

if __name__ == "__main__":
    Example().run()
