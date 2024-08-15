import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import random
import string

def password_gen():
    length=int(length_entry.get())
    include_uppercase=uppercase_var.get()
    include_lowercase=lowercase_var.get()
    include_numbers=numbers_var.get()
    include_special=special_var.get()

    if not(include_uppercase or include_lowercase or include_numbers or include_special):
        messagebox.showwarning("Input Error", "please select at least one character type*")
        return
    characters=""
    if include_uppercase:
        characters +=string.ascii_uppercase
    if include_lowercase:
        characters +=string.ascii_lowercase
    if include_numbers:
        characters +=string.digits
    if include_special:
        characters +=string.punctuation
    
    password=''.join(random.choice(characters)for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root=tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("400x300")
root.configure(bg="silver")

font_l= tkfont.Font(family="helvetica",size= 10)
font_b=tkfont.Font(family="helvetica",size= 8, weight="bold")

length_label=tk.Label(root, text="password length:",font=font_l,bg="dark slate gray",fg="white")
length_label.grid(row=1, column=0,padx=10,pady=5)

length_entry=tk.Entry(root,font=font_l)
length_entry.grid(row=2,column=0,pady=5,padx=5)

uppercase_var=tk.BooleanVar()
uppercase_check=tk.Checkbutton(root, text="include uppercase letters", variable=uppercase_var,font=font_l,bg="slate gray")
uppercase_check.grid(row=3,column=1,padx=5,pady=5)

lowercase_var=tk.BooleanVar()
lowercase_check=tk.Checkbutton(root, text="include lowercase letters", variable=lowercase_var,font=font_l,bg="slate gray")
lowercase_check.grid(row=4,column=1,padx=5,pady=5)

numbers_var=tk.BooleanVar()
numbers_check=tk.Checkbutton(root, text="include numbers (digits)", variable=numbers_var,font=font_l,bg="slate gray")
numbers_check.grid(row=5,column=1, padx=5,pady=5)

special_var=tk.BooleanVar()
special_check=tk.Checkbutton(root, text="include special characters", variable=special_var,font=font_l,bg="slate gray")
special_check.grid(row=6,column=1,padx=5,pady=5)

password_entry = tk.Entry(root,width=40,font=font_b,bg="gainsboro")
password_entry.grid(row=8,column=0,columnspan=2,padx=5,pady=10)

generate_button=tk.Button(root, text="generate",command=password_gen,font=font_b,bg="dark slate gray",fg="white")
generate_button.grid(row=7,column=0,padx=5,pady=5,columnspan =1)

root.mainloop()