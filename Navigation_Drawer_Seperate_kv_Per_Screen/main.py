from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MDScreen1(MDScreen):
    pass

class MDScreen2(MDScreen):
    pass

class MainScreen(MDScreen):
    pass

class Example(MDApp):
    def build(self):
        # Load the main kv file containing the navigation drawer
        Builder.load_file("navigationdrawer.kv")
        # Load each screen's kv file
        Builder.load_file("screen1.kv")
        Builder.load_file("screen2.kv")

        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return MainScreen()

if __name__ == "__main__":
    Example().run()
