# grocery = {"milk": 60, "biscuit": 85, "tea": 100}
# print(grocery)
# print(type(grocery))
# grocery["shampoo"] = 100
# print(grocery)
# print(type(grocery))
#
# for gcs in grocery:
#     print(gcs)

score = [200, 300, 52, 63, 666]
highest = score[0]

for scr in score:
    if highest > scr:
        highest = scr

print(highest)

import random
print(random.random())
print(random.randint(50, 60))
print(random.choice(score))

correct_password = "Python"
while True:
    user_pass = input("enter your pass : ")
    if correct_password == user_pass:
        print("okie")
        break
    else :
        print("not ok")

print("success")