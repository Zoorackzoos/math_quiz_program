# What are these files .md
files, folders. whichever.

## MainMenuModule_folder
This has the main menu. it's the 1st screen you see

## WorksheetModule_folder
This holds questions.  
there is NOT a module per question module.   
it's loaded with questions from variables in the "logic" folder.  

Those question variables are like this:
```python
example_module_questions = \
[
    {
        "title": "Q1",
        "instructions": "find the derivative of the following function",
        "latex": r"\frac{d}{dx} x^2 = ?",
        "answer": "2x",
        "tolerance": 0.01
    }
]
```