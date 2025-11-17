#Calc3Exam2StudyGuideModule.py
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import Screen

from src.GUI.GUI_sub_files.Calc3Exam2StudyGuideModule_folder.latex_widget import *

class Calc3Exam2StudyGuideModule(Screen):
    def build(self):
        inspector.create_inspector(Window, self)
        # return Builder.load_file("navigation.kv")

class Questions(Screen):
    pass
