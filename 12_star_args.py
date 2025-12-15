# *args -variable length positional arguments 0 to n

def add(*args):
    return sum(args)

result = add(12,25,53,78,88)
print(f"result is {result}")



def student_detials(sname, sid, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent in exam ")
    else:
        percentage = sum(marks) / len(marks)
        print(f"{sname} with id {sid} is secured {percentage:.2f}% marks")

student_detials("Prash", 101, 50,56,85,96,54,77.0)
student_detials("Rohan", 102)
student_detials("Rishi", 103, 50,56,85,96,54,77.0)
student_detials("Mehul", 104, 50,56,85,96,54,77.0)
student_detials("Rudresh", 105)
