from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import Screen

class MainMenuModule(Screen):

    def build(self):
        inspector.create_inspector(Window, self)
        # return Builder.load_file("navigation.kv")

class MainMenuScreen(Screen):

    def test_function(self):
        print("test_function")