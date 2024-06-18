from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

# Define your screen classes
class MainScreen(Screen):
    pass

class SettingsScreen1(Screen):
    pass

class SettingsScreen2(Screen):
    pass

class SettingsScreen3(Screen):
    pass

class SettingsScreen4(Screen):
    pass


class Example(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')

    # Define a method to handle navigation back to main screen
    def navigate_main(self):
        self.root.current = 'Main'

    # Define a method to handle navigation back to settings screen
    def navigate_back(self):
        self.root.current = 'Settings'


Example().run()