from tkinter import *
from tkinter import messagebox

contacts = {}

def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

def refresh_list():
    contact_list.delete(0, END)
    for name in sorted(contacts):
        contact_list.insert(END, f"{name} - {contacts[name]['Phone']}")

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required.")
        return

    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists.")
        return

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully")

def search_contact():
    keyword = search_entry.get().strip()

    if keyword == "":
        messagebox.showwarning("Warning", "Enter Name or Phone")
        return

    for name, details in contacts.items():
        if keyword.lower() == name.lower() or keyword == details["Phone"]:
            name_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            address_entry.delete(0, END)

            name_entry.insert(0, name)
            phone_entry.insert(0, details["Phone"])
            email_entry.insert(0, details["Email"])
            address_entry.insert(0, details["Address"])

            return

    messagebox.showerror("Not Found", "Contact Not Found")

def update_contact():
    name = name_entry.get().strip()

    if name not in contacts:
        messagebox.showerror("Error", "Contact Not Found")
        return

    contacts[name]["Phone"] = phone_entry.get().strip()
    contacts[name]["Email"] = email_entry.get().strip()
    contacts[name]["Address"] = address_entry.get().strip()

    refresh_list()
    clear_fields()
    messagebox.showinfo("Updated", "Contact Updated Successfully")

def delete_contact():
    name = name_entry.get().strip()

    if name in contacts:
        del contacts[name]
        refresh_list()
        clear_fields()
        messagebox.showinfo("Deleted", "Contact Deleted Successfully")
    else:
        messagebox.showerror("Error", "Contact Not Found")

def load_contact(event):
    selected = contact_list.curselection()

    if selected:
        item = contact_list.get(selected[0])
        name = item.split(" - ")[0]

        details = contacts[name]

        clear_fields()

        name_entry.insert(0, name)
        phone_entry.insert(0, details["Phone"])
        email_entry.insert(0, details["Email"])
        address_entry.insert(0, details["Address"])


root = Tk()
root.title("Contact Book")
root.geometry("650x600")
root.resizable(False, False)

Label(root, text="CONTACT BOOK", font=("Arial", 20, "bold")).pack(pady=15)

frame = Frame(root)
frame.pack()

Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=8, sticky=W)
name_entry = Entry(frame, width=35)
name_entry.grid(row=0, column=1)

Label(frame, text="Phone").grid(row=1, column=0, padx=10, pady=8, sticky=W)
phone_entry = Entry(frame, width=35)
phone_entry.grid(row=1, column=1)

Label(frame, text="Email").grid(row=2, column=0, padx=10, pady=8, sticky=W)
email_entry = Entry(frame, width=35)
email_entry.grid(row=2, column=1)

Label(frame, text="Address").grid(row=3, column=0, padx=10, pady=8, sticky=W)
address_entry = Entry(frame, width=35)
address_entry.grid(row=3, column=1)

Button(root, text="Add Contact", width=15, command=add_contact).pack(pady=5)
Button(root, text="Update Contact", width=15, command=update_contact).pack(pady=5)
Button(root, text="Delete Contact", width=15, command=delete_contact).pack(pady=5)

Label(root, text="Search (Name / Phone)").pack(pady=5)

search_entry = Entry(root, width=35)
search_entry.pack()

Button(root, text="Search", width=15, command=search_contact).pack(pady=8)

Label(root, text="Saved Contacts", font=("Arial", 14, "bold")).pack()

contact_list = Listbox(root, width=55, height=10)
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", load_contact)

Button(root, text="Refresh List", width=15, command=refresh_list).pack(pady=5)

root.mainloop()