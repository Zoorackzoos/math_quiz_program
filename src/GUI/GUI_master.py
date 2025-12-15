#GUI_master.py
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
from kivy.modules import inspector

from src.GUI.GUI_sub_files.WorksheetModule_folder.WorksheetModule import *
from src.GUI.GUI_sub_files.MainMenuModule_folder.MainMenuModule import *
from src.GUI.universal_GUI_variables import universal_font_size_numeric_property

#load kivy files using Builder so this file "total_program_main" can read them
Builder.load_file(''
                  'GUI_sub_files/MainMenuModule_folder/MainMenuModule.kv'
                  '')
Builder.load_file('GUI_sub_files/WorksheetModule_folder/WorksheetModule.kv'
                  '')


class TotalProgramMainApp(App):
    universal_font_size_app_variable = universal_font_size_numeric_property

    current_worksheet = StringProperty("")

    def build(self):
        root = ScreenManager()

        # For inspection (press control-e to toggle).
        inspector.create_inspector(Window, self)

        root.add_widget(MainMenuModule())
        root.add_widget(WorksheetModule())

        root.current = 'MainMenuModule'
        return root



if __name__ == '__main__':
    TotalProgramMainApp().run()

