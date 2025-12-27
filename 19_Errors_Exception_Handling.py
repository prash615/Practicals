"""
1. Compile time error => Syntax error & Indentation error
2. Exceptions => errors during execution
"""
try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter another number : "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Deno meter cant be Zero ")
except ValueError:
    print("Input should be only digit")
