#WorksheetModule.py
import math

from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.tabbedpanel import TabbedPanelItem

from src.GUI.GUI_sub_files.WorksheetModule_folder.latex_widget_folder.latex_widget import *
from src.GUI.universal_GUI_variables import universal_font_size_int, universal_font_size_numeric_property
from src.logic.question_variables.testing_module_questions import testing_module_questions

class WorksheetModule(Screen):
    def build(self):
        inspector.create_inspector(Window, self)
        # return Builder.load_file("navigation.kv")

    def testingFunction(self):
        print("WorksheetModule -> testingFunction")

    def on_enter(self):
        app = App.get_running_app()
        worksheet_id = app.current_worksheet

        if worksheet_id == "testing_module":
            self.load_testing_module()

    def load_testing_module(self):
        self.ids.questions_screen.populate_questions(testing_module_questions)

class Questions(Screen):
    def previewTest(self):
        print("Questions -> previewTest -> self.ids.answer_text_id.text = "+self.ids.answer_text_id.text)

    def checkTest(self):
        print("Questions -> checkTest -> self.ids.answer_text_id.text = "+self.ids.answer_text_id.text)

    def populate_questions(self, questions):
        print("Questions -> populate_questions")
        print("\tself.ids = \t\t\t", self.ids)

        for key in self.ids:
            print("\t\t", str(key))

        tabs = self.ids.question_tabs
        tabs.clear_widgets()

        for q in questions:
            tab = TabbedPanelItem(text=q["title"])

            box = BoxLayout(
                orientation="vertical",
                #padding=10,
                #spacing=10
            )

            # Instructions (plain text)
            instruction_label = Label(
                text=q.get("instructions", ""),
                #size_hint_y=None,
                halign="left",
                valign="middle",
                size_hint_y=0.10,
                font_size=universal_font_size_int/2
            )
            instruction_label.bind(
                texture_size=instruction_label.setter("size")
            )

            # LaTeX math
            latex_widget = LatexLabel(
                latex_string=q["latex"],
                #size_hint_y=None
            )

            box.add_widget(instruction_label)
            box.add_widget(latex_widget)

            tab.add_widget(box)
            tabs.add_widget(tab)