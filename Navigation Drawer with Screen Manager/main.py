from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem



class ContentNavigationDrawer(MDBoxLayout):
    def add_items(self, app):
        # Add navigation items for each screen
        for i in range(1, 6):
            item = OneLineListItem(
                text=f"Screen {i}",
                on_release=app.create_screen_changer(f"screen{i}")
            )
            self.ids.box.add_widget(item)


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        root = Builder.load_file('main.kv')
        return root

    def on_start(self):
        # Access the ContentNavigationDrawer and add items
        drawer_content = self.root.ids.nav_drawer.children[0]
        drawer_content.add_items(self)

    def create_screen_changer(self, screen_name):
        def change_screen(instance):
            self.root.ids.screen_manager.current = screen_name
            self.root.ids.nav_drawer.set_state("close")

        return change_screen


Example().run()
