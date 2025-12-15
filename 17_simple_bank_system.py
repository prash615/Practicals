balance = 0.00
kyc_documents = {}

print("============================")


def check_balance():
    print(f"your current balance is {balance} Rs")
    print("============================")

def deposit(amount):
    global balance
    if amount >= 0:
        balance = balance + amount
    else:
        print("Nagative balance can't be add")
        print("======================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw a negative or zero amount")
    elif amount > balance:
        print("Cannot withdraw. Insufficient balace")
        print("======================")
    else:
        balance = balance - amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("===================")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")
        print("=========================")


print("============================")
print("Welcome to Prash Bank")
print("============================\n")

if __name__ == "__main__":
    while True:
        print(""" 
                1. Check your balance
                2. Deposite an amount 
                3. Withdraw an amount
                4. Check KYC
                5. Update KYC
                6. Quit
        """)
        choice = input("Enter your choice (1-6) : ")
        print("=============================")
        if choice == "1":
            check_balance()
        elif choice == "2":
            amt = float(input("Enter an amount to be deposit :"))
            print("============================")
            deposit(amt)
            print(f"Amount {amt} deposited successfully")
            print("===========================")

        elif choice == "3":
            amt = float(input("Enter an amount to be withdraw :"))
            withdraw(amt)
            print(f"Amount {amt} withdraw successfully")
        elif choice == "4":
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter a number u want to add : "))
            for i in range(n_documents):
                key = input("Enter doc type : ")
                value = input("enter doc num : ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("KYC Update")
            print("=====================")
        elif choice == "6":
            print("Quiting have a nice day")
            break
        else:
            print("Invalid choice !! Re-try.")
        print("======================\n")


print("Thank you for banking with us :)")
