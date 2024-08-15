import tkinter as tk
from tkinter import messagebox

def add_task():
    task=task_entry.get()
    if task !="":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning","you must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "you must select a task.")

def update_task():
    try:
        task_index=task_listbox.curselection()[0]
        new_task=task_entry.get()
        if new_task=="":
            messagebox.showwarning("Warning","you must enter a new task")
            return
        task_listbox.delete(task_index)
        task_listbox.insert(task_index,new_task)
        task_entry.delete(0,tk.END)
        
    except IndexError:
        messagebox.showwarning("Warning","You must select a task")

root = tk.Tk()
root.title("To Do  list")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add task", width=42, command=add_task)
add_task_button.pack(pady=5)

update_button=tk.Button(root,text="Update Task",command=update_task)
update_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

delete_task_button = tk. Button(root, text="Delete task", width=42, command=delete_task)
delete_task_button.pack(pady=5)

root.mainloop()