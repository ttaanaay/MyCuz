from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    pass


class MaCuzApp(MDApp):

    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MaCuzApp().run()