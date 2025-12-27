class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)

    def show(self):
        return f"Name: {self.name}, Contact Number: {self.phone}"

    @classmethod
    def show_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory!")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone

        return f"no found {search_name}"


c1 = Contact("Alice", 7418529630)
c2 = Contact("Carol", 1234567890)
print(Contact.phone_directory)
print(c1.show())
print(c2.show())

print(Contact.search_contact("Alice"))
print(Contact.search_contact("alice"))
