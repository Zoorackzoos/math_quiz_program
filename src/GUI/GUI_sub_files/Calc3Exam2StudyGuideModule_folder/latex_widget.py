# latex_widget.py
import io
import matplotlib.pyplot as plt
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty


class LatexLabel(Image):
    latex_string = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Render every time the latex_string changes
        self.bind(latex_string=self._render_latex)

        # If KV loaded with an initial value
        if self.latex_string:
            self._render_latex()

    def _render_latex(self, *args):
        if not self.latex_string:
            return

        fig = plt.figure()
        fig.text(0.1, 0.5, f'${self.latex_string}$', fontsize=20)

        buffer = io.BytesIO()
        plt.axis('off')
        fig.savefig(buffer, format='png', dpi=200, bbox_inches='tight', pad_inches=0.1)
        buffer.seek(0)
        plt.close(fig)

        self.texture = CoreImage(buffer, ext='png').texture
