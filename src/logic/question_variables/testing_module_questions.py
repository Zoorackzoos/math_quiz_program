testing_module_questions = [
    {
        "title": "Q1",
        # single-line text + math
        "latex": r"\text{Evaluate the derivative: } x^2",
        "answer": "2x",
        "tolerance": 0.01
    },
    {
        "title": "Q2",
        # single-line plain text
        "latex": r"\text{This is question 2! Please answer } 2",
        "answer": "2",
        "tolerance": 0.01
    },
    {
        "title": "Q3",
        # multiline: text on top, math on bottom
        "latex": r"\begin{array}{l}\text{Evaluate the derivative:}\\ 2x + 3x^2 + 2\end{array}",
        "answer": "4*x + 6*x^1",   # example symbolic form (you'll parse later)
        "tolerance": 0.01
    }
]
