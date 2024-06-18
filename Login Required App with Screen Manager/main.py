from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import requests
from kivymd.uix.dialog import MDDialog

class LoginScreen(Screen):
    def check_login(self):
        username = self.ids.username_field.text
        password = self.ids.password_field.text

        # HTTP POST request to server for login
        url = 'http://localhost:5000/login'
        data = {'username': username, 'password': password}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            app = MDApp.get_running_app()
            app.root.current = 'main'
        else:
            self.ids.username_field.error = True
            self.ids.password_field.error = True

class RegisterScreen(Screen):
    def register_user(self):
        username = self.ids.reg_username_field.text
        password = self.ids.reg_password_field.text

        # HTTP POST request to server for registration
        url = 'http://localhost:5000/register'
        data = {'username': username, 'password': password}
        response = requests.post(url, json=data)

        if response.status_code == 201:
            dialog = MDDialog(title='Success', text='User created successfully!')
            dialog.open()
            app = MDApp.get_running_app()
            app.root.current = 'login'
        elif response.status_code == 400:
            self.ids.reg_username_field.error = True
        else:
            dialog = MDDialog(title='Error', text='Failed to create user')
            dialog.open()

class MainAppScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'  # Choose between "Light" or "Dark"
        Builder.load_file('main.kv')
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(MainAppScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
