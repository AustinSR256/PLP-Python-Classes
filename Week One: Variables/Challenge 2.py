import random
python_questions = {
    "What is Python?": "Programming language",
    "Who created Python?": "Guido van Rossum",
    "Is Python interpreted or compiled?": "Interpreted",
    "What is a variable?": "Storage",
    "What is a list?": "Ordered collection",
    "What is a tuple?": "Immutable list",
    "What is a dictionary?": "Key-value pair",
    "What is a set?": "Unordered collection",
    "What is indentation used for?": "Code blocks",
    "What is a function?": "Code block",
    "What does `def` do?": "Define function",
    "What is `None`?": "Null value",
    "What is a string?": "Text data",
    "What is an integer?": "Whole number",
    "What is a float?": "Decimal number",
    "What is a boolean?": "True/False",
    "What does `if` do?": "Conditional",
    "What does `for` do?": "Loop",
    "What does `while` do?": "Loop",
    "What is `break` used for?": "Exit loop",
    "What is `continue` used for?": "Skip iteration",
    "What is `pass` used for?": "Empty block",
    "What does `return` do?": "Exit function",
    "What is a module?": "Code library",
    "What is `import` used for?": "Load module",
    "What is a class?": "Object blueprint",
    "What is an object?": "Class instance",
    "What is `self`?": "Instance reference",
    "What is inheritance?": "Class extension",
    "What is polymorphism?": "Many forms",
    "What is encapsulation?": "Data hiding",
    "What is a lambda?": "Anonymous function",
    "What is a decorator?": "Function wrapper",
    "What is a generator?": "Lazy iterator",
    "What is an iterator?": "Iterable object",
    "What is exception?": "Error",
    "What is `try` used for?": "Catch errors",
    "What is `finally` used for?": "Always runs",
    "What is `with` used for?": "Context manager",
    "What is PEP 8?": "Style guide",
    "What is pip?": "Package manager",
    "What is PyPI?": "Package index",
    "What is virtualenv?": "Environment tool",
    "What is recursion?": "Self-call",
    "What is slicing?": "Subset selection",
    "What is `__init__`?": "Constructor",
    "What is `__str__`?": "String method",
    "What is list comprehension?": "Compact loop",
    "What is duck typing?": "Behavior-based typing",
    "What is GIL?": "Global Interpreter Lock",
    "What is multithreading?": "Concurrent execution"
}


questions = list(python_questions.keys())
count = 0
score = 0

while count < 10:
    question = random.choice(questions)
    print(f"\nQuestion {count+1}: {question}")
    answer = input("Your answer: ").lower()
    correct = python_questions[question].lower()

    # Split both answers into words
    user_words = set(answer.split())
    correct_words = set(correct.split())

    # Check if any word in user's answer is in correct answer words
    if user_words & correct_words:
        print("The answer is correct!")
        score += 1
    else:
        print("The answer is wrong!!!")
        print(f"Correct answer: {python_questions[question]}")

    count += 1

print(f"\nYour final score is {score} out of 10.")
