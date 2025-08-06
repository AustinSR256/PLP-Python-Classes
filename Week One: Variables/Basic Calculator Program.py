print("HELLO, WELCOME TO MY SIMPLE CALCULATOR")

print('''
Enter 2 numbers and specify the operation using one of the following codes:

  addition:        'a'
  subtraction:     's'
  multiplication:  'm'
  division:        'd'
''')

first_no = float(input("Enter the first number: "))
second_no = float(input("Enter the second number: "))
operation = input("Specify the operation: ").lower()

if operation == 'a':
    result = first_no + second_no
    print(f"The sum of {first_no} and {second_no} is {result}.")
elif operation == 's':
    result = first_no - second_no
    print(f"The difference between {first_no} and {second_no} is {result}.")
elif operation == 'm':
    result = first_no * second_no
    print(f"The product of {first_no} and {second_no} is {result}.")
elif operation == 'd':
    if second_no != 0:
        result = first_no / second_no
        print(f"The quotient of {first_no} divided by {second_no} is {result}.")
    else:
        print("Error: Division by zero is undefined.")
else:
    print("Invalid operation selected.")
