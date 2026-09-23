import tkinter as tk
from tkinter import messagebox
from database import connect_database

window = tk.Tk()
window.title("FitTrack")
window.geometry("400x300")

title = tk.Label(
    window,
    text="FIT TRACK",
    font=("Arial", 24, "bold"))

title.pack(pady=30)

username_label = tk.Label(window, text="Username:")
username_label.pack()

username_entry =tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

def show_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*") 
show_password_var = tk.BooleanVar()

show_password_check = tk.Checkbutton(
    window,
    text = "Show Password",
    variable = show_password_var,
    command = show_password)

show_password_check.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()

    db = connect_database()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                   (username, password))

    user = cursor.fetchone()

    if user:
        messagebox.showinfo("login", "Login successful!")

    else:
        messagebox.showerror("Login", "Invalid username or password.")

        cursor.close()
        db.close()
           

login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=20)

window.mainloop()