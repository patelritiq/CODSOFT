import json


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

    @staticmethod
    def from_dict(data):
        return Contact(data["name"], data["phone"])


class ManageContacts:
    def __init__(self, filename="contacts.json"):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f)

    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                self.contacts = [Contact.from_dict(c) for c in json.load(f)]
        except FileNotFoundError:
            pass

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("\nYour contact list is empty.")
        else:
            print("\n~~~~~ Contact Vault ~~~~~")
            for i, c in enumerate(self.contacts, 1):
                print(f"{i}. {c.name} : {c.phone}")

    def search_contacts(self, keyword):
        results = [
            c
            for c in self.contacts
            if keyword.lower() in c.name.lower() or keyword in c.phone
        ]
        if results:
            print("\n>>>>> Search Results: ")
            for i, c in enumerate(results, 1):
                print(f"{i}. {c.name} : {c.phone}")
        else:
            print("No contacts found.")

    def update_contact(self, index, name, phone):
        self.contacts[index].name = name
        self.contacts[index].phone = phone
        self.save_contacts()

    def delete_contact(self, index):
        del self.contacts[index]
        self.save_contacts()


def main():
    manager = ManageContacts()

    while True:
        print("\n~~~~~ The Contact Vault ~~~~~")
        print(
            "1. Add Contact\n2. View Contacts\n3. Search Contacts\n4. Update Contact\n5. Delete Contact\n6. Exit"
        )
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Name: ")
            while True:
                phone = input("Phone number(10 digits): ")
                if len(phone) == 10 and phone.isdigit():
                    break
                print("Invalid phone number. Please enter a 10-digit number.")
            manager.add_contact(Contact(name, phone))
            print("Contact added successfully!")

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone to search: ")
            manager.search_contacts(keyword)

        elif choice == "4":
            manager.view_contacts()
            index = int(input("Enter the contact number to update: ")) - 1
            if 0 <= index < len(manager.contacts):
                name = input("New Name: ")
                while True:
                    phone = input("New Phone (10 digits): ")
                    if len(phone) == 10 and phone.isdigit():
                        break
                    print("Invalid phone number. Please enter a 10-digit number.")
                manager.update_contact(index, name, phone)
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")

        elif choice == "5":
            manager.view_contacts()
            index = int(input("Enter the contact number to delete: ")) - 1
            if 0 <= index < len(manager.contacts):
                manager.delete_contact(index)
                print("Contact deleted successfully!")
            else:
                print("Invalid contact number.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
