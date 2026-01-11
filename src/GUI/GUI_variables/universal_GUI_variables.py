
from kivy.properties import NumericProperty

"""
kivy only accepts NumericProperty type variables
but
python generating kivy... only accepts ints or floats.
"""
universal_font_size_int = 40
universal_font_size_numeric_property = NumericProperty(universal_font_size_int)
