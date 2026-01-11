"""
GUI master doesn't do a lot other than build the app. It's like rendering it.
"""
#GUI_master.py
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from src.GUI.GUI_sub_files.WorksheetModule_folder.WorksheetModule import *
from src.GUI.GUI_sub_files.MainMenuModule_folder.MainMenuModule import *
from src.GUI.GUI_variables.universal_GUI_variables import universal_font_size_numeric_property

#load kivy files using Builder so this file "total_program_main" can read them
Builder.load_file(''
                  'GUI_sub_files/MainMenuModule_folder/MainMenuModule.kv'
                  '')
Builder.load_file(''
                  'GUI_sub_files/WorksheetModule_folder/WorksheetModule.kv'
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

