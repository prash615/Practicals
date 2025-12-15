"""
recursion is a process in which a fun calls itself till a certain condition isnt met
"""

num = int(input("enter a num "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(fact)