#MainMenuModule.py
from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import Screen
"""
i have this in camelCase because the kivy naming conventions are that way.
"""
class MainMenuModule(Screen):

    def build(self):
        inspector.create_inspector(Window, self)
        # return Builder.load_file("navigation.kv")

class MainMenuScreen(Screen):

    def printModuleSelection(self):
        app = App.get_running_app()
        worksheet_id = app.current_worksheet
        print("MainMenuScreen -> printModuleSelection -> " + str(worksheet_id))

    def test_function(self):
        print("test_function")