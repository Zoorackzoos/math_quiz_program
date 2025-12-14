Nice call — rolling back to the original widget is the easiest, most robust path. Below I’ll give you a short **reference guide** (by example) you can copy into your question files. It shows:

* what the original `LatexLabel` (your widget) **can reliably render**,
* what **not** to put in `latex_string` (and why),
* recommended patterns for mixing plain text and math (use Kivy `Label` for text),
* a handful of ready-to-drop example question dicts.

### Quick reminders about your original widget

* The widget does `fig.text(..., f'${latex_string}$', ...)` — **it wraps your string in math mode**.
* **Do not** include literal `$` in your `latex_string`. The widget already adds them.
* Use Python raw strings: `r"..."` so backslashes behave properly.
* The widget uses Matplotlib **mathtext**, **not** a full LaTeX engine. Mathtext supports a useful subset of LaTeX math (fractions, integrals, sums, superscripts, subscripts, `\sqrt`, Greek letters, `\vec`, `\langle\rangle`, `\text{...}`, etc.) but **doesn’t support full environments/packages**.

---

## Good: examples that will render well with the original widget

```python
# Good examples (mathtext-safe)
good_questions = [
    {
        "title": "Simple derivative",
        "latex": r"\frac{d}{dx} x^2 = 2x",
        "answer": "2x",
        "tolerance": 0.01
    },
    {
        "title": "Definite integral",
        "latex": r"\int_{0}^{\pi} \sin x \, dx = 2",
        "answer": "2",
        "tolerance": 0.01
    },
    {
        "title": "Infinite series",
        "latex": r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}",
        "answer": "pi**2/6",
        "tolerance": 1e-6
    },
    {
        "title": "Gradient and vectors",
        "latex": r"\nabla f = \langle f_x, f_y, f_z \rangle",
        "answer": "",
        "tolerance": 0.01
    },
    {
        "title": "Square root & power",
        "latex": r"\sqrt{a^2 + b^2}",
        "answer": "",
        "tolerance": 0.0
    },
    {
        "title": "Plain text + a short math expression (use \\text{})",
        "latex": r"\text{Evaluate: } x^2 + 1",
        "answer": "",
        "tolerance": 0.01
    },
]
```

Notes:

* `\text{...}` is supported by mathtext and will render upright text within math mode.
* Inline math like `x^2`, `\frac{...}{...}`, `\int`, `\sum` are safe.

---

## Not supported / will cause errors (and what to do instead)

```python
bad_examples = [
    {
        "title": "Do NOT use full LaTeX environments",
        "latex": r"\begin{array}{l} \text{Line1} \\ \text{Line2} \end{array}",
        # ❌ mathtext often rejects \begin{...} → ParseException
    },
    {
        "title": "Do NOT use verbatim or complex package macros",
        "latex": r"\verb|some text| \usepackage{tikz}",
        # ❌ packages and verbatim are not supported
    },
    {
        "title": "Do NOT include $ signs",
        "latex": r"$x^2$",
        # ❌ the widget will add $...$ again resulting in malformed input
    },
]
```

Alternatives:

* For multiline *text* or long instructions, use a regular **Kivy `Label`** above/beside the `LatexLabel`.
* For complex LaTeX (cases, align, verbatim, packages, TikZ), use **full LaTeX rendering** (requires installing a TeX distribution) and a different pipeline (compile → PDF → PNG). That’s a separate upgrade path.

---

## Pattern I recommend: keep *math* in `latex` and *instructions* in Kivy Label

```python
# Recommended schema for each question:
example = {
    "title": "Q-example",
    "instruction": "Differentiate the function below:",   # put this in a Kivy Label
    "latex": r"\frac{d}{dx}\left( x^3 + 2x \right) = 3x^2 + 2",  # put this in your LatexLabel
    "answer": "3*x**2 + 2",
    "tolerance": 0.01
}
```

In your UI code, render `instruction` with a `Label` (normal text) and `latex` with `LatexLabel`.

---

## Short cheatsheet — what mathtext in the original widget handles well

Allowed / good:

* `^`, `_` (superscripts, subscripts)
* `\frac{a}{b}`
* `\sqrt{...}`
* `\sum_{...}^{...}`, `\int_{...}^{...}`
* Greek letters: `\alpha,\beta,\pi,\nabla`
* `\text{...}` for small upright text inside math
* `\langle ... \rangle`, `\vec{v}`
* inline combinations like `\sin x`, `\cos\theta`

Avoid / not reliable:

* `\begin{array}`, `\begin{align}`, `\begin{cases}` (use plain math or separate labels)
* `\verb`, `\texttt{}` or verbatim blocks
* `\usepackage{...}` or package-specific macros
* raw `$` delimiters (widget wraps for you)

---

## Example "reference file" you can keep and copy from

```python
# testing_module_questions_reference.py

questions_reference = [
    # Good: simple math
    {"title":"Deriv1", "instruction":"Differentiate:", "latex":r"\frac{d}{dx} x^2", "answer":"2x", "tolerance":0.01},

    # Good: integral
    {"title":"Integral1", "instruction":"Evaluate the integral:", "latex":r"\int_0^{\pi}\sin x\,dx", "answer":"2", "tolerance":0.01},

    # Good: series
    {"title":"Series", "instruction":"Recognize this sum:", "latex":r"\sum_{n=1}^{\infty}\frac{1}{n^2}", "answer":"pi**2/6", "tolerance":1e-6},

    # Good: text (use Kivy Label for longer text)
    {"title":"Readme", "instruction":"This problem has a long instruction; use a Kivy Label above the math.", "latex":r"\text{Short note: } x+1", "answer":"", "tolerance":0},

    # Bad: full LaTeX environment (DON'T put this into latex_string)
    {"title":"BadExample", "instruction":"Don't use full environments here; use separate widgets or full-LaTeX pipeline.",
     "latex": r"\begin{array}{l}\text{Line1}\\ \text{Line2}\end{array}", "answer":"", "tolerance":0}
]
```

---

## Final tips

* If you need **multi-line math** (e.g., aligned equations) or `cases` later, plan to upgrade to a **full LaTeX** render pipeline (compile `.tex` → `.pdf` → `.png`) — I can show that when you’re ready.
* Keep the `latex` field *pure math* whenever possible; keep wording/instructions in `instruction` strings (rendered by Kivy Labels).
* Use `r"..."` strings and **never** include `$...$` in `latex`.

---

If you want, I’ll:

* Convert a few of your real practice problems into the recommended schema, or
* Show the exact Kivy code (kv + Python) to render `instruction` above each `LatexLabel` in your tabs. Which would you like next?
