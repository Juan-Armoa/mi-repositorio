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
        contacts_dict_list = [contact.to_dict() for contact in  self.contacts]
        
        with open("contacts.json", "w") as file:
            json.dump(contacts_dict_list, file, indent=4)
            print("contacts saved to file succesfully!")

p1 = Contact("Gonzalo", "11223344", "gonza@gmail.com", "Argentina")
p2 = Contact("Aron", "11224214", "aron@gmail.com", "Argentina")

my_book = ContactBook()
my_book.add_contact(p1)
my_book.add_contact(p2)

print("Total contacts in book:", len(my_book.contacts))
my_book.save_contacts()