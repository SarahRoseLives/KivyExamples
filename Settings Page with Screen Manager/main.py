from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

# Define your screen classes
class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class SettingsScreen1(Screen):
    pass

class SettingsScreen2(Screen):
    pass

class SettingsScreen3(Screen):
    pass

class SettingsScreen4(Screen):
    pass

# Create the main application class
class Example(MDApp):

    def build(self):
        # Load the kv file
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

    # Define a method to handle navigation back to main screen
    def navigate_main(self):
        self.root.current = 'Main'

    # Define a method to handle navigation back to settings screen
    def navigate_back(self):
        self.root.current = 'Settings'


# Entry point of the application
if __name__ == '__main__':
    Example().run()
