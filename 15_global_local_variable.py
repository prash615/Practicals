n = 1

def fun():
    global n
    n = 5
    print(f"in {n}")
fun()
print(f"out {n}")


num = int(input("enter num : "))
print( "even" if num % 2 == 0 else  "odd")
