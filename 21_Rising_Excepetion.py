salary = float(input("Enter Your Salary : "))

if salary < 0:
    raise  ValueError("Salary cannot be negative") #Exception can use
else:
    print(salary)