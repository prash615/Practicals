import random

while True:
    choice = input("Press 'Enter' to play or 'q' to Quite : ")
    choice = choice.strip()
    if choice == "q":
        print("thanks for playing ! bye !!!")
        break
    elif choice == "":
        num = random.randint(1, 6)
        print(f"your num is :{num}")
    else:
        print("invalid input")

print("GAME OVER !!!")