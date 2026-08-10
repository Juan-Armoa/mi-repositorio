import json
import os

class Contact:
    def __init__(self, name, phone, email, country):
        self.name = name
        self.phone = phone
        self.email = email
        self.country = country

    def to_dict(self):
        """Converts the Contact object into a dictionary to save in JSON."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "country": self.country
        }


class ContactBook:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self): 
        """Reads contacts from the JSON file. Returns empty list if file doesn't exist."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Contact(c["name"], c["phone"], c["email"], c["country"]) for c in data]
        except Exception:
            return []

    def save_contacts(self):
        """Saves current contacts into the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            data = [c.to_dict() for c in self.contacts]
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added and saved successfully!")

    def list_contacts(self):
        if not self.contacts:
            print("ERROR: No contacts found.")
            return

        print("\n--- Your Contacts ---")
        for c in self.contacts:
            print(f"- {c.name}: {c.phone} ({c.email}) - {c.country}")

    def search_contact(self, query):
        found = False
        for c in self.contacts:
            if c.name.lower() == query.lower():
                print(f"\nContact found: {c.name} - {c.phone} ({c.email}) - {c.country}")
                found = True
                break
        if not found:
            print("ERROR: Contact not found.")


# --- Main Loop ---
def main():
    book = ContactBook()

    while True:
        option = input("\nSelect an option:\n1. Add contact\n2. View contacts\n3. Search contact\n4. Exit: ").strip()

        if option == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            country = input("Country: ").strip()

            if name and phone:
                new_contact = Contact(name, phone, email, country)
                book.add_contact(new_contact)
            else:
                print("ERROR: Name and phone are required.")

        elif option == "2":
            book.list_contacts()

        elif option == "3":
            query = input("Enter name to search: ").strip()
            book.search_contact(query)

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()