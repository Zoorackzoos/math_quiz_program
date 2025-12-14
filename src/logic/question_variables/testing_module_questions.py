#testing_module_questions.py
testing_module_questions = [
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
        "answer": "24",
        "tolerance": 0.01
    },
    {
        "title": "Square root & power",
        "latex": r"\sqrt{a^2 + b^2}",
        "answer": "24",
        "tolerance": 0.0
    },
    {
        "title": "Plain text + a short math expression (use \\text{})",
        "latex": r"\text{Evaluate: } x^2 + 1",
        "answer": "24",
        "tolerance": 0.01
    },
]