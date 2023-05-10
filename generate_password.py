#Generate Password
import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox as msgbox

# UpperLetters is the list of uppercase letters.
characters = "AB!@#$%^&*()CDEabcijkyzFGpqrstuHIJ0defgh1234~_+`\-}=]:<>?,./KLMNOP{|[QRS56789TUlmnovwxVWXYZ"

#New Password
new_password = []


#function to generate random password
def on_level(level):
    if not new_password and user_name.get() != "":
        pick = random.choices(characters, k=level)
        new_password.append(pick)
        user_password = "".join(new_password[0])
        message.set(user_password)
    else:
        if user_name.get() =="":
            msgbox.showerror("Error","Write your name first")
        else:
            msgbox.showerror("Password","Password already generated, Please press reset")

#function Reset
def on_reset():
    global new_password
    if not new_password:
        msgbox.showerror("Password","You didnt generate your password, Please generate it first")
    else:
        new_password = []
        msgbox.showinfo("Ready","App was Reset")
    return message.set("")

root = tk.Tk()
root.title("Generator")
root.resizable(False, False)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

ttk.Label(
    root,
    text="Password Generator",
    font=("TkDefaultFont", 16)
).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

ttk.Label(
    root,
    text=datetime.now().strftime("%Y-%m-%d"),
    font=("TkDefaultFont", 13)
).grid(row=1, column=0, sticky="s",padx=5, pady=5)


df = tk.Frame(root) 
df.grid(row=2, column=0, pady=10, sticky="nsew")
df.columnconfigure([0,1], weight=1)

ttk.Label(
    df,
    text="User_Name"
).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

user_name = tk.StringVar(value="")
ttk.Entry(
    df,
    textvariable=user_name
).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

bf = tk.Frame(root)
bf.grid(row=3, column=0, pady=10, sticky="nsew")
bf.columnconfigure([0,1,2], weight=1)

pw_easy = 4
ttk.Button(
    bf,
    text="Easy",
    width=10,
    command= lambda: on_level(pw_easy)
).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

pw_medium = 8
ttk.Button(
    bf,
    text="Medium",
    width=10,
    command= lambda: on_level(pw_medium)
).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

pw_hard = 12
ttk.Button(
    bf,
    text="Hard",
    width=10,
    command= lambda: on_level(pw_hard)
).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

ff = tk.Frame(root)
ff.grid(row=4, column=0, pady=10, sticky="nsew")
ff.columnconfigure([0,1], weight=1)

ttk.Label(
    ff,
    text="New Password"
).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

message = tk.StringVar()
ttk.Label(
    ff,
    textvariable=message
).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

ttk.Button(
    ff,
    text="RESET",
    command=on_reset
).grid(row=1,columnspan=2,padx=5, pady=5, sticky="nsew")


root.mainloop()