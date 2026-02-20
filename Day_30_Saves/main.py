import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ("Arial", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def Generate_Password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [(random.choice(letters))
                        for _ in range(random.randint(2, 4))]
    password_symbols = [(random.choice(symbols))
                        for _ in range(random.randint(2, 4))]
    password_numbers = [(random.choice(numbers))
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    new_password = "".join(password_list)
    pyperclip.copy(new_password)
    password_entry.insert(0, new_password)


def Add_Password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Entry",
                            message="Please don't leave any fields empty!")
    else:

        try:
            with open("data.json", "r") as password_data:
                data = json.load(password_data)
        except:
            with open("data.json", "w") as password_data:
                json.dump(new_data, password_data, indent=4)
        else:
            pass

        finally:
            with open("data.json", "r") as password_data:
                data = json.load(password_data)
                data.update(new_data)

            with open("data.json", "w") as password_data:
                json.dump(data, password_data, indent=4)

        website_entry.delete(0, tkinter.END)
        email_username_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)


def Search_Command():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as passwords_file:
            all_data = json.load(passwords_file)

    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="Data file doesn't exist.")

    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title=f"{website_name}", message="No details for the website exists")
    
    except KeyError as key_not_found:
        messagebox.showinfo(title=key_not_found, message="No details for the key found.")

    else:

        stored_email = all_data[website_name]["email"]
        stored_password = all_data[website_name]["password"]
        with open("data.json", "r") as passwords_file:
            pyperclip.copy(stored_password)
            messagebox.showinfo(title=f"{website_name}",
                                message=f"Email: {stored_email}\nPassword: {stored_password}")


# ---------------------------- UI SETUP ------------------------------- #


# Creates the window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_rowconfigure(1, pad=5)
window.grid_rowconfigure(2, pad=5)
window.grid_rowconfigure(3, pad=5)
window.grid_columnconfigure(1, weight=0, pad=0)
window.grid_columnconfigure(2, weight=0, pad=0)


# Puts the image on the window
canvas = tkinter.Canvas(width=200, height=200)
password_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)

# Write the text "Website:" ,    "Email/Username:",  "Password:"
website_text = tkinter.Label(text="Website:", font=FONT)
email_username_text = tkinter.Label(text="Email/Username:", font=FONT)
password_text = tkinter.Label(text="Password:", font=FONT)

# Creates entry for website name , email/username , password
website_entry = tkinter.Entry(width=41)
website_entry.focus()

email_username_entry = tkinter.Entry(width=41)
email_username_entry.insert(0, "anishcryptic@gmail.com")

password_entry = tkinter.Entry(width=41)

# Generate Password , Add Password button
generate_password_button = tkinter.Button(
    text="Generate", command=Generate_Password)
add_password_button = tkinter.Button(
    text="Add Password", command=Add_Password, width=43)
search_password_button = tkinter.Button(
    text="Search", command=Search_Command, width=7)

# Layout
canvas.grid(row=0, column=1)

website_text.grid(row=1, column=0)
email_username_text.grid(row=2, column=0)
password_text.grid(row=3, column=0)


website_entry.grid(row=1, column=1, sticky="w")
email_username_entry.grid(row=2, column=1, sticky="w")
password_entry.grid(row=3, column=1, sticky="w")


generate_password_button.grid(row=3, column=1, sticky="e")
add_password_button.grid(row=4, column=1, sticky="w")
search_password_button.grid(row=1, column=1, sticky="e")

window.mainloop()
