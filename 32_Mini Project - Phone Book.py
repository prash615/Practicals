class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Contact Number: {self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory!")
        else:
            print("All contacts from the directory!! =>")
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone

        return f"no found {search_name}"

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False

n_contacts = int(input("How many contact do u want to add ?: "))
for i in range(n_contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter contact Number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid phone number for {name}. "
              f"Phone number should be at least 8 digits "
              f"and should only contain numbers.")

# c1 = Contact("Alice", 7418529630)
# c2 = Contact("Carol", 1234567890)
# print(Contact.phone_directory)
# print(c1.show())
# print(c2.show())
# print(Contact.search_contact("Alice"))
# print(Contact.search_contact("alice"))

Contact.show_all_contact()
