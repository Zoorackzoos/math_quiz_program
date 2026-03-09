"""
WorksheetModule.py

this is where questions & answers are administrated based on each test / quiz.
"""
import math
from asyncio.windows_events import NULL
from logging import root

from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.textinput import TextInput
from sqlalchemy import null, Null
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem


from src.GUI.GUI_sub_files.WorksheetModule_folder.latex_widget_folder.latex_widget import *
from src.GUI.GUI_variables.universal_GUI_variables import universal_font_size_int, universal_font_size_numeric_property
from src.logic.question_variables.testing_module_questions import testing_module_questions
from src.GUI.GUI_master import TotalProgramMainApp

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

# this populates based on the question amount.
# we have this so when the user goes from problem to problem, their inputs save.
user_inputted_answers = []

def update_user_inputted_answers(user_answer, tab_amount="\t"):
    print(tab_amount,"update_user_inputted_answers")
    tab_amount += "\t"
    """
     TODO: implement a algorithm that gets question_integer based off of a title.
     you would fetch the title, then search thru a question list variable
      to see which question matched the title, then with that instance
      find it's "question_integer" value
      """
    total_program_screen_manager = TotalProgramMainApp.get_running_app().root
    worksheet_screen = total_program_screen_manager.get_screen("WorksheetModule")
    question_integer = TotalProgramMainApp.get_running_app().root.ids

    print(tab_amount,"worksheet_screen.ids : ",worksheet_screen.ids)
    print(tab_amount,"worksheet_screen.ids.questions_screen : ",worksheet_screen.ids.questions_screen)
    print(tab_amount,"worksheet_screen.ids.questions_screen.ids : ",worksheet_screen.ids.questions_screen.ids)



    #user_inputted_answers[question_integer] = user_answer
    #print(tab_amount,"user_expected_answers:")
    #tab_amount += "\t"
    #print("\n",user_inputted_answers)

class Questions(Screen):

    def previewTest(self):
        print("Questions -> previewTest -> self.ids.answer_text_id.text = "+self.ids.answer_text_id.text)

    def checkTest(self):
        print("Questions -> checkTest -> self.ids.answer_text_id.text = "+self.ids.answer_text_id.text)

    def populate_questions(self, questions):
        """

        :param questions: from src/logic/question_variables .
                it's a list that contains sets, each set is a question.
        :return: adds question widgets to the tabbed panel widget
        """
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

            # TODO: refactor user_inputted_answer's temp NULL value a real null value instead of a string.
            user_inputted_answers.append("NULL")


class QuestionsTabbedPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super(QuestionsTabbedPanel, self).__init__(**kwargs)
        # Bind the function to the 'current_tab' property
        self.bind(current_tab=self.on_tab_change)

    def on_tab_change(self, instance, new_tab):
        # Triggered when tab changes. 'new_tab' is the new tab item.
        print(f"Tab changed to: {new_tab.text}")

class UserAnswerTextInput(TextInput):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        print("UserAnswerTextInput -> keyboard_on_key_down -> self.text: ")
        print("\t",self.text)
        update_user_inputted_answers(self.text)
        return super().keyboard_on_key_down(window, keycode, text, modifiers)
