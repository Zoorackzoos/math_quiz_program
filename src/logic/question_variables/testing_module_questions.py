"""
src/logic/question_variables/testing_module_questions.py
this stores json-like "almost" latex files that get rendered with the latex widget
    they're lists that contain sets.

you need
1. title            usually just the question and it's number. maybe also indicates question parts.
2. instructions     tells the user what to do given the question's latex. similar to webwork problem.s
3. latex            not "always" necessary but most of the time you'll have a question with latex like elements.
4. answer
5. tolerance        "how close a numeric answer has to be to the real answer, to count as correct"
                    also "most quiz programs have this"
"""
testing_module_questions = [
    {
        "question integer": 1,
        "title": "1",
        "instructions": "find the derivative of the following function",
        "latex": r"\frac{d}{dx} x^2 = ?",
        "answer": "2x",
        "tolerance": 0.01
    },
    {
        "question integer": 2,
        "title": "2",
        "instructions": "Evaluate the following function",
        "latex": r"\int_{0}^{\pi} \sin x = ?",
        "answer": "2",
        "tolerance": 0.01
    },
    {
        "question integer": 3,
        "title": "3",
        "instructions": "Evaluate the following function",
        "latex": r"\sum_{n=1}^{\infty} \frac{1}{n^2} = ?",
        "answer": "pi^2/6",
        "tolerance": 1e-6
    },
    {
        "question integer": 4,
        "title": "4",
        "instructions": "Parametrize the following functions in respect of x,y and z.",
        "latex": r"\nabla f = ?",
        "answer": "<f_x, f_y, f_z>",
        "tolerance": 0.01
    },
    {
        "question integer": 5,
        "title": "5",
        "instructions": "If this equation represents a cone, what would it be equal to?",
        "latex": r"\sqrt{x^2 + y^2} = ?",
        "answer": "z",
        "tolerance": 0.0
    },
    {
        "question integer": 6,
        "title": "6",
        "instructions": "find the derivative of the following function",
        "latex": r"\frac{d}{dx} x^2 + 1 = ?",
        "answer": "2x",
        "tolerance": 0.01
    }
]