#WorksheetModule.py
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import Screen

from src.GUI.GUI_sub_files.WorksheetModule_folder.latex_widget import *

class WorksheetModule(Screen):
    def build(self):
        inspector.create_inspector(Window, self)
        # return Builder.load_file("navigation.kv")

    def testingFunction(self):
        print("WorksheetModule -> testingFunction")

class Questions(Screen):
    def testingFunction(self):
        print("Questions -> testingFunction")
