#WorksheetModule.py
from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.tabbedpanel import TabbedPanelItem

from src.GUI.GUI_sub_files.WorksheetModule_folder.latex_widget import *

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
        questions = [
            {
                "title": "Q1",
                "latex": r"\frac{d}{dx}(x^2)",
                "answer": "2x"
            },
            {
                "title": "Q2",
                "latex": r"\nabla f",
                "answer": "<fx, fy, fz>"
            }
        ]

        self.ids.questions_screen.populate_questions(questions)

class Questions(Screen):
    def testingFunction(self):
        print("Questions -> testingFunction -> "+self.ids.answer_text_id.text)

    def populate_questions(self, questions):
        print("Questions -> populate_questions")
        print("\tself.ids = \t\t\t",self.ids)
        #i tried to get it to spit out the values as well but it gave me the slip.
        for key in self.ids:
            print("\t\t", str(key))
        tabs = self.ids.question_tabs
        tabs.clear_widgets()

        for q in questions:
            tab = TabbedPanelItem(text=q["title"])

            box = BoxLayout(orientation="vertical")
            box.add_widget(
                LatexLabel(latex_string=q["latex"])
            )

            tab.add_widget(box)
            tabs.add_widget(tab)