import os
import pickle

# ---------------- Node Structure ----------------
class ContactNode:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None  # self-referential (linked list)

# ---------------- Linked List Contact Book ----------------
class ContactBook:
    def __init__(self, filename="contacts.dat"):
        self.head = None
        self.filename = filename
        self.load_contacts()

    # Insert contact alphabetically
    def add_contact(self, name, phone, email):
        new_node = ContactNode(name, phone, email)

        if self.head is None or self.head.name.lower() > name.lower():
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.save_contacts()
        print(f"✅ Contact '{name}' added successfully!")

    # Search by name
    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                return current
            current = current.next
        return None

    # Update contact
    def update_contact(self, name, new_phone=None, new_email=None):
        contact = self.search_contact(name)
        if contact:
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            self.save_contacts()
            print(f"✅ Contact '{name}' updated successfully!")
        else:
            print("❌ Contact not found!")

    # Delete contact
    def delete_contact(self, name):
        current = self.head
        prev = None
        while current:
            if current.name.lower() == name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.save_contacts()
                print(f"🗑 Contact '{name}' deleted successfully!")
                return
            prev = current
            current = current.next
        print("❌ Contact not found!")

    # Display all contacts
    def display_contacts(self):
        if not self.head:
            print("📭 No contacts found.")
            return
        current = self.head
        print("\n--- Contact List ---")
        while current:
            print(f"👤 {current.name} | 📞 {current.phone} | ✉️ {current.email}")
            current = current.next

    # Save to file
    def save_contacts(self):
        contacts = []
        current = self.head
        while current:
            contacts.append((current.name, current.phone, current.email))
            current = current.next
        with open(self.filename, "wb") as f:
            pickle.dump(contacts, f)

    # Load from file
    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                contacts = pickle.load(f)
                for name, phone, email in sorted(contacts):
                    self.add_contact(name, phone, email)


# ---------------- Menu-Driven Program ----------------
if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to search: ")
            contact = book.search_contact(name)
            if contact:
                print(f"👤 {contact.name} | 📞 {contact.phone} | ✉️ {contact.email}")
            else:
                print("❌ Contact not found!")

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to keep same): ")
            email = input("Enter new email (leave blank to keep same): ")
            book.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "4":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "5":
            book.display_contacts()

        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")
