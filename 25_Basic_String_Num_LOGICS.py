#BASIC LOGIC
from itertools import count
s1 = "P   ython"
c = 0
for i in s1:
    c = c + 1
print(f"length of this sting is {c}")

l1 = [1, 2, 3, 4]
d = 0
for ii in l1:
    d = d + 1
print(f"the length of this list is {d}")

numbers = [1, 2, 3, 4]
total = 0
for num in numbers:
    total = total + num
print(f"sum of l2 is {total}")

l2 = [1, 2, 6, 3, 4]
max_num = l2[0]
for i in l2:
    if i > max_num:
        max_num = i
print(f"max {max_num}")

l3 = [11, 2, 6, 3, 4]
min_num = l3[0]
for i in l3:
    if i < min_num:
        min_num = i
print(f"min {min_num}")

l4 = [11, 2, 6, 3, 4]
even_num = []
total_even_num = 0
for i in l4:
    if i % 2 == 0:
        even_num.append(i)
        total_even_num = total_even_num + 1
print(f"even num are {even_num} and total num even num are {total_even_num} ")

l5 = [11, 2, 6, 3, 4]
total_odd_num = 0
odd_num = []
for i in l5:
    if i % 2 != 0:
        odd_num.append(i)
        total_odd_num += 1
print(f"even num are {odd_num} and total num even num are {total_odd_num} ")

#remove duplicate
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
unq_nums = list(set(nums))
print(unq_nums)



#STRING PROBLEMS
#Reverse a string.
text = "Python"
rev_text = ''
for char in text:
    rev_text = char + rev_text
print(f"reverse of string is {rev_text}")

#Check whether a string is a palindrome.
name = "MADAM"
rev_str = ''
for ch in name:
    rev_str = ch + rev_str
if rev_str == name:
    print(f"Yes {name} is palindrome")
else:
    print(f"No {name} is not  palindrome")

#Remove duplicate characters from a string.
greet = "Hello Hello Hello How are How You Doing Have A great Day !!"
greet1 = "Prasannajeet"
unique_string = ''
for ch in greet:
    if ch not in unique_string:
        unique_string = unique_string + ch
print(unique_string)

#Count vowels in a string.
text = "Programming"
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
       count = count + 1
print(count)

#NUMBER LOGIC
#Check whether a number is even or odd.
number = 5
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
numb = 6
print("Even" if numb % 2 == 0 else "Odd")

#Find factorial of a number using a loop.
num1 = 5
fact = 1
for i in range(1, num1 + 1):
    fact = fact * i
print(f"factorial of {num1} is {fact}")

#Print Fibonacci series up to n terms.
n = 8
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("====================")
#2nd opt using 3rd variable
num2 = 8
a = 0
b = 1
for i in range(num2):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
print("=============")

#Check whether a number is prime.
x = 17
if x <= 1:
    print(f"{x} is not a prime number")
else:
    for i in range(2, x):
        if x % i == 0:
            print(f"{x} is not Prime number")
            break
        else:
            print(f"{x} is  Prime Number")
            break

#Count number of digits in a number.
a1 = 123
count_digits = 0
while a1 != 0:
    a1 = a1 // 10
    count_digits = count_digits + 1
print(f" num of digits are {count_digits}")
#short cut dont use
t1 = 123
print(f"{t1} num of digits are {len(str(t1))}")

#Reverse a number
org_num = 123564715
rev_num = 0
while org_num != 0:
    digit = org_num % 10
    rev_num = rev_num * 10 + digit
    org_num = org_num // 10
print(rev_num)

#Check whether a number is a palindrome.
my_num = 1212
reversed_number = 0
x1 = my_num

while my_num > 0:
    digit = my_num % 10
    reversed_number = reversed_number * 10 + digit
    my_num = my_num // 10
print("Yes Palindrome" if x1 == reversed_number else "No its not Palindrome")


#Find sum of digits of a number.
nums = 123456
count = 0
while nums > 0:
    digits = nums % 10
    count = count + digits
    nums = nums // 10
print(f"Find sum of digits of a number  is {count} prash.")

#Find the largest digit in a number.
my__nums = 12356416
temp = my__nums
max_digit = 0
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp = temp // 10
print(f"largest digit in {my__nums} is {max_digit}")


    
