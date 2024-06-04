#### Day 29: Building a Password Manager GUI App with Tkinter
**Challenge:** Create a password manager application with a GUI using Tkinter, including functionalities to save and retrieve passwords.

```python
import tkinter as tk
from tkinter import messagebox
import json

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        new_data = {website: {"username": username, "password": password}}
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Password Manager")

website_label = tk.Label(window, text="Website:")
website_label.grid(row=0, column=0)
website_entry = tk.Entry(window, width=35)
website_entry.grid(row=0, column=1, columnspan=2)

username_label = tk.Label(window, text="Email/Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(window, width=35)
username_entry.grid(row=1, column=1, columnspan=2)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(window, width=21)
password_entry.grid(row=2, column=1)
password_button = tk.Button(window, text="Generate Password")
password_button.grid(row=2, column=2)

add_button = tk.Button(window, text="

Add", width=36, command=save_password)
add_button.grid(row=3, column=1, columnspan=2)

window.mainloop()
```


