s1 = "  python to  "
s2 = 25
print("on" in s1)
s3 = s1.strip()
print(s3)
s4 = s1.replace("python", "java")
print(s4)

str = "welcome welcome to python"
str2 = "come"
print(f"occurrence of {str2} is {str.count(str2)}")

days_of_weeks = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
print(days_of_weeks[0])

list1 = ["apple", "banana", "cherry"]
print(list1)
list1.append("aaloo")
print(list1)

list2 = ["india", "australia","newzeland"]
print(list2)
list2.insert(2, "Prash")
print(list2)

vegetables = ["apple", "banana", "cherry"]
print(vegetables)
vegetables.extend(["prash", "mallik"])
print(vegetables)

vegetables.remove("apple")
print(vegetables)

animal = ["cat", "rat", "frog"]
print(animal)
animal.pop(1)
print(animal)

car = ["honda", "bmw", "toyota"]
print(car)
car.reverse()
print(car)

num1 = [1, 5, 8, 2, 3, 4, 6, 6, 3, 5, 0, 0, 5]
print(num1)
num1.reverse()
print(num1)

num1.sort(reverse=True)
print(num1)

digit = [1, 5, 8, 2, 3, 4, 6, 6, 3, 5, 0, 0, 5]
print(digit)
item_to_count = int(input("Enter item to count: "))
c = digit.count(item_to_count)
print(c)

print(f"min num is {min(digit)}")
print(f"max num is {max(digit)}")

# tpl1 = 200, 300, 52, 63
# print(tpl1)
l1 = [200, 300, 52, 63, 666]
print(l1, type(l1))
tpl3 = tuple(l1)
print(tpl3, type(tpl3))
print(f"is : {type(l1)}")

# list mutable , tuple, strings are not

weeks = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
print(weeks)
weeks[3] = "thursday"
print(weeks)
