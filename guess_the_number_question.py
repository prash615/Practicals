
import random
print("Welcome to the number guessing game. We have a number that needs to be guessed. YOU have 10 attempts.")
print("The secret number is between 1 and 50")

attempts = 5
secret_num = random.randint(1, 50)

num = 1
while num <= 10:
    print(f"you left {attempts} left")
    user_input = int(input("Enter num u want :"))
    if user_input == secret_num:
        print("U guess correct num !!")
        break
    else:
        if user_input < secret_num:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"you guess wrong num try {higher_or_lower} num")

    num += 1
    attempts -= 1
print(f"game over the secret num was {secret_num}")


def procedure_guessing_num (num1, num2):
    if guess % 2 == 0:
        return "Even"
    else:
        return "Odd"

guess = int(input("enter guessing num : "))


