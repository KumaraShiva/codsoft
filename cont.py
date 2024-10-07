import tkinter as tk
from tkinter import messagebox

# Contact list to store all contacts as dictionaries
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()
    view_contacts()

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)  # Clear the listbox
    if contacts:
        for idx, contact in enumerate(contacts):
            contact_list.insert(tk.END, f"{idx + 1}. {contact['name']} - {contact['phone']}")
    else:
        contact_list.insert(tk.END, "No contacts found.")

# Function to search contacts
def search_contact():
    search_term = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]

    if results:
        for idx, contact in enumerate(results):
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        contact_list.insert(tk.END, "No contacts found.")

# Function to update a contact
def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")
        return
    
    idx = selected[0]  # Get index of selected contact
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    # Update the selected contact
    contacts[idx] = {"name": name, "phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", "Contact updated successfully!")
    clear_fields()
    view_contacts()

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return

    idx = selected[0]
    del contacts[idx]
    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contacts()

# Function to clear the input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Setting up the main window
window = tk.Tk()
window.title("Contact Manager")
window.geometry("500x600")
window.config(bg="#ffffff")  # White background

# Title Label with Gradient Effect
title_label = tk.Label(window, text="Contact Manager", font=("Arial", 20, "bold"), bg="#ffffff", fg="#333399")
title_label.pack(pady=20)

# Input Fields
tk.Label(window, text="Name:", font=("Arial", 12), bg="#ffffff", fg="#4a4a4a").pack(anchor="w", padx=20)
name_entry = tk.Entry(window, font=("Arial", 12), width=40)
name_entry.pack(pady=5)

tk.Label(window, text="Phone:", font=("Arial", 12), bg="#ffffff", fg="#4a4a4a").pack(anchor="w", padx=20)
phone_entry = tk.Entry(window, font=("Arial", 12), width=40)
phone_entry.pack(pady=5)

tk.Label(window, text="Email:", font=("Arial", 12), bg="#ffffff", fg="#4a4a4a").pack(anchor="w", padx=20)
email_entry = tk.Entry(window, font=("Arial", 12), width=40)
email_entry.pack(pady=5)

tk.Label(window, text="Address:", font=("Arial", 12), bg="#ffffff", fg="#4a4a4a").pack(anchor="w", padx=20)
address_entry = tk.Entry(window, font=("Arial", 12), width=40)
address_entry.pack(pady=5)

# Buttons to add, update, and delete contacts
button_frame = tk.Frame(window, bg="#ffffff")
button_frame.pack(pady=15)

add_button = tk.Button(button_frame, text="Add Contact", width=15, font=("Arial", 12), bg="#4CAF50", fg="white", command=add_contact)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Contact", width=15, font=("Arial", 12), bg="#ffeb3b", fg="black", command=update_contact)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", width=15, font=("Arial", 12), bg="#ff6347", fg="white", command=delete_contact)
delete_button.grid(row=0, column=2, padx=5)

# Search bar
search_label = tk.Label(window, text="Search by Name or Phone:", bg="#ffffff", fg="#4a4a4a", font=("Arial", 12))
search_label.pack(anchor="w", padx=20)
search_entry = tk.Entry(window, font=("Arial", 12), width=30)
search_entry.pack(pady=5)
search_button = tk.Button(window, text="Search", width=10, bg="#87CEEB", font=("Arial", 12), command=search_contact)
search_button.pack(pady=5)

# Contact List Display
contact_list = tk.Listbox(window, height=10, width=50, font=("Arial", 12))
contact_list.pack(pady=10)

# View Contacts Button
view_button = tk.Button(window, text="View All Contacts", width=20, bg="#90ee90", font=("Arial", 12), command=view_contacts)
view_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(window, text="Clear Fields", width=15, bg="#f0ad4e", font=("Arial", 12), command=clear_fields)
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(window, text="Exit", width=15, bg="#ff6347", font=("Arial", 12), fg="white", command=window.quit)
exit_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
