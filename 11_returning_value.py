def odd_even(num):
    if num % 2 == 0:
        return  "EVEN"
    else:
        return  "ODD"

result = odd_even(10)
print(result)


def airthmatic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

val1 = int(input("enter a num :"))
val2 = int(input("enter a num :"))

result1, result2, result3, result4 = airthmatic(val1, val2)
print(f"the add of {val1} and {val2} is {result1}")
print(f"the sub of {val1} and {val2} is {result2}")
print(f"the mul of {val1} and {val2} is {result3}")
print(f"the div of {val1} and {val2} is {result4}")
