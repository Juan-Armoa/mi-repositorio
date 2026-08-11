import json

class Contact:
    def __init__(self, name, phone, email, country):
        self.name = name
        self.phone = phone
        self.email = email
        self.country = country

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "country": self.country
        }

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added to the book!")

    def save_contacts(self):
        contacts_dict_list = [contact.to_dict() for contact in self.contacts]
        with open("contacts.json", "w") as file:
            json.dump(contacts_dict_list, file, indent=4)
            print("Contacts saved to file successfully!")

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                contacts_data = json.load(file)
                self.contacts = [
                    Contact(c["name"], c["phone"], c["email"], c["country"])
                    for c in contacts_data
                ]
            print("Contacts loaded successfully!")
        except FileNotFoundError:
            print("No contacts file found")

# Pruebas
p1 = Contact("Gonzalo", "11223344", "gonza@gmail.com", "Argentina")
p2 = Contact("Aron", "11224214", "aron@gmail.com", "Argentina")

my_book = ContactBook()
my_book.add_contact(p1)
my_book.add_contact(p2)
my_book.save_contacts()


another_book = ContactBook()
another_book.load_contacts()


for c in another_book.contacts:
    print(f"Name: {c.name} | Phone: {c.phone}")