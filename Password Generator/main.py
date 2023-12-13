from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_entry.delete(0, END)
    password = ("".join(password_list))
    pyperclip.copy(password)
    password_entry.insert(0, string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="One or more Inputs are missing",
                             message="Please check your Inputs and try again")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email}"
                                                              f"\nPassword: {password}"
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open("./Small-Apps/Password Generator/count.txt", 'r') as file:
                count = int(file.read())
                count += 1
            with open("./Small-Apps/Password Generator/count.txt", 'w') as file:
                file.write(str(count))
            ###----------------------###
            entries = [str(count), '. ', website, ' || ',
                       email, ' || ', password, '\n']
            ###---------------------###
            with open("./Small-Apps/Password Generator/Password Manager.txt", "a") as txt:
                # txt.write(f"{count}. {website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                txt.writelines(entries)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#f7f5ee")

logo_png = PhotoImage(file="./Small-Apps/Password Generator/logo.png")
canvas = Canvas(width=200, height=200, bg="#f7f5ee", highlightthickness=0)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="#f7f5ee")
website_label.grid(row=1, column=0, ipady=5)
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, ipady=2)
website_entry.focus()

email_label = Label(text="Email/Username:", bg="#f7f5ee")
email_label.grid(row=2, column=0, ipady=5)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, ipady=2)
email_entry.insert(END, string="raiyan.is.here@gmail.com")

password_label = Label(text="Password:", bg="#f7f5ee")
password_label.grid(row=3, column=0, ipady=5)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, ipady=2)
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
