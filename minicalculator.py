import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())

        operation = operation_var.get()

        if operation=="+":
            result=num1+num2
        elif operation=="-":
            result=num1-num2
        elif operation=="*":
            result=num1*num2
        elif operation=="/":
            if num2==0:
                messagebox.showerror("Error","cannot divide by zero")
                return
            else:
                result=num1/num2
            
        else:
            messagebox.showerror("Error","Invalid operation")
            return
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error","Invalid input")

root=tk.Tk()
root.title("MINI CALCULATOR")
root.configure(bg='grey')

tk.Label(root, text ="enter num1:",bg="black", fg="white",font=("Arial bold",12)).grid(row=0,column=0,pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0,column=1,pady=10)

tk.Label(root, text="enter num2:",bg="black" ,fg="white",font=("Arial bold",12)).grid(row=1,column=0,pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1,pady=10)

operation_var = tk.StringVar(value="select")
tk.Label(root, text="select operation:",bg="black", fg="white").grid(row=2,column=0,pady=5,padx=10)

tk.Radiobutton(root, text="+", variable=operation_var, value="+", bg="black", fg="darkblue",font=("Arial",16)).grid(row=2, column=1, padx=10,pady=5)
tk.Radiobutton(root, text="-", variable=operation_var, value="-", bg="black", fg="darkblue",font=("Arial",16)).grid(row=3, column=1, padx=10,pady=5)
tk.Radiobutton(root, text="*", variable=operation_var, value="*", bg="black", fg="darkblue",font=("Arial",16)).grid(row=4, column=1, padx=10,pady=5)
tk.Radiobutton(root, text="/", variable=operation_var, value="/", bg="black", fg="darkblue",font=("Arial",16)).grid(row=5, column=1, padx=10,pady=5)

calculate_button = tk.Button(root, text="calculate", command=calculate)
calculate_button.grid(row=5,column=0,columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ", bg="black", fg="lightblue")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()