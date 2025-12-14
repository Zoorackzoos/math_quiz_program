# latex_widget.py
import io
import re
import matplotlib.pyplot as plt
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty

# Heuristic to detect math-like content
_MATH_RE = re.compile(r"\\(frac|int|sqrt|sum|left|right|begin|pi)|[\^_]|[0-9]|[+\-=*/]|\\[a-zA-Z]+")


def _is_mathish(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    # if user explicitly wrapped in \text{} we treat it as text-ish (not math)
    if s.startswith(r"\text{") and s.endswith("}"):
        return False
    # if there are common math tokens, treat as math
    return bool(_MATH_RE.search(s))


def _unwrap_array(s: str) -> list:
    """
    If s contains a \begin{array}{...} ... \end{array}, extract the inner content
    and split on \\ into lines. Otherwise returns None.
    """
    m = re.search(r"\\begin\{array\}\{.*?\}(.*?)\\end\{array\}", s, flags=re.DOTALL)
    if not m:
        return None
    inner = m.group(1)
    # split on LaTeX linebreaks or real newlines
    parts = re.split(r"\\\\|\\n|\n", inner)
    return [p.strip() for p in parts if p is not None]


class LatexLabel(Image):
    latex_string = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Keep aspect, allow stretch for better fit inside layouts
        self.allow_stretch = True
        self.keep_ratio = True

        # Re-render on change
        self.bind(latex_string=self._render_latex)

        if self.latex_string:
            # initial render (if provided)
            self._render_latex()

    def _render_latex(self, *args):
        s = (self.latex_string or "").strip()
        if not s:
            return

        # Remove surrounding $ if user accidentally added them
        if s.startswith("$") and s.endswith("$"):
            s = s[1:-1].strip()

        # If user used \begin{array}... extract and use its lines; else split on explicit \\ or newline into lines
        array_lines = _unwrap_array(s)
        if array_lines is not None:
            lines = array_lines
        else:
            # split on explicit LaTeX newline or real newline, keep single-line as one element
            lines = re.split(r"\\\\|\\n|\n", s)

        # sanitize and filter empty lines
        lines = [ln.strip() for ln in lines]
        if not lines:
            return

        # Determine figure height based on number of lines
        n_lines = max(1, len(lines))
        fig_w = 7
        fig_h = max(1.2, 0.9 + 0.9 * n_lines)  # modest scaling

        fig = plt.figure(figsize=(fig_w, fig_h))
        # white background like earlier widget
        fig.patch.set_facecolor("white")
        plt.axis("off")

        # vertical placement: start near top and step down
        top = 0.85
        step = 0.8 / max(n_lines, 1)  # distribute lines vertically
        y = top

        fontsize = 22

        for line in lines:
            if not line:
                y -= step
                continue

            # If the line already explicitly uses \text{...}, let it be; otherwise decide by heuristic
            if line.startswith(r"\text{") and line.endswith("}"):
                # wrap in math mode so mathtext renders upright text via \text{...}
                draw = f"${line}$"
            else:
                if _is_mathish(line):
                    # treat as math: wrap in $...$
                    draw = f"${line}$"
                else:
                    # treat as plain text: wrap in \text{...} then math mode
                    safe = line.replace("}", r"\}").replace("{", r"\{")
                    draw = rf"$\text{{{safe}}}$"

            # center horizontally
            fig.text(0.5, y, draw, fontsize=fontsize, ha="center", va="top")
            y -= step

        # Render to PNG buffer
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=200, bbox_inches="tight", pad_inches=0.15)
        plt.close(fig)
        buf.seek(0)

        core = CoreImage(buf, ext="png")
        self.texture = core.texture

        # ensure widget gets proper height (prevents invisible widget until layout change)
        self.size_hint = (1, None)
        self.height = self.texture.height
