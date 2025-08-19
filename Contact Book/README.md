# 📒 Contact Book (Python)

A simple **Contact Book application** implemented in Python using **Linked Lists** and **File Storage**.  
This project demonstrates how to store, search, update, delete, and display contacts while maintaining **alphabetical order** of insertion.  

---

## 📌 Overview
The Contact Book is a console-based program that:
- Uses a **self-referential structure (linked list)** for storing contacts in memory.
- Stores contacts in a **binary file** (`contacts.dat`) for persistence using `pickle`.
- Ensures contacts are always inserted **alphabetically** by name.
- Provides a **menu-driven interface** for easy use.

---

## ✨ Features
- ➕ **Add Contact** – Insert new contacts in alphabetical order.  
- 🔍 **Search Contact** – Find a contact by name.  
- ✏️ **Update Contact** – Modify phone number or email of an existing contact.  
- 🗑 **Delete Contact** – Remove a contact from the list.  
- 📋 **Display Contacts** – Show all saved contacts in sorted order.  
- 💾 **File Persistence** – Contacts are saved and reloaded automatically from file.  

---

## 🛠 Data Structures Used
- **Linked List (Self-referential Structure)**  
  Each contact is stored as a node (`ContactNode`) with:
  - `name`
  - `phone`
  - `email`
  - `next` → pointer to the next contact node  

- **File Storage (`pickle`)**  
  Contacts are serialized and saved in a file (`contacts.dat`) so data is not lost when the program exits.  

---

## ▶️ How It Runs
1. Clone this repository:
   git clone https://github.com/your-username/contact-book.git
   cd contact_book.py
2.Run the code:
python contact_book.py

