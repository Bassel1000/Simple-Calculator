import tkinter as tk

# Define the functions for the calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Define the function to perform the calculation
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    choice = choice_var.get()
    result = 0

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)

    label_result.config(text=result)
    history.append(f"{num1} {choice_symbols[choice]} {num2} = {result}")

# Define the function to show the history
from tkinter import messagebox

def show_history():
    history_text = "\n".join(history)
    messagebox.showinfo("History", history_text)

# Define the function to delete the last digit of the currently focused input field
def delete_digit():
    if entry_num1.focus_get() == entry_num1:
        entry_num1.delete(len(entry_num1.get()) - 1, tk.END)
    elif entry_num2.focus_get() == entry_num2:
        entry_num2.delete(len(entry_num2.get()) - 1, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("420x390")  # Set the size of the window

# Set the background color of the root window
root.configure(background="#ca3d3d")

# Create the input fields
label_num1 = tk.Label(root, text="Enter first number:",foreground="white", background="black", font=("Arial", 16))
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Enter second number:",foreground="white", background="black", font=("Arial", 16))
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Create the radio buttons for the operation choice
choice_var = tk.IntVar()

radio_add = tk.Radiobutton(root, text="Add", variable=choice_var, value=1,foreground="white", background="black", font=("Arial", 16))
radio_add.grid(row=2, column=0)

radio_subtract = tk.Radiobutton(root, text="Subtract", variable=choice_var, value=2,foreground="white", background="black", font=("Arial", 16))
radio_subtract.grid(row=2, column=1)

radio_multiply = tk.Radiobutton(root, text="Multiply", variable=choice_var, value=3,foreground="white", background="black", font=("Arial", 16))
radio_multiply.grid(row=3, column=0)

radio_divide = tk.Radiobutton(root, text="Divide", variable=choice_var, value=4,foreground="white", background="black", font=("Arial", 16))
radio_divide.grid(row=3, column=1)

# Create the buttons for each number
def add_digit(digit):
    if entry_num1.focus_get() == entry_num1:
        entry_num1.insert(tk.END, digit)
    elif entry_num2.focus_get() == entry_num2:
        entry_num2.insert(tk.END, digit)

button_0 = tk.Button(root, text="0", font=("Arial", 16), command=lambda: add_digit("0"),bg="black",fg="white",width=3,height=1)
button_0.grid(row=4, column=0)

button_1 = tk.Button(root, text="1", font=("Arial", 16), command=lambda: add_digit("1"),bg="black",fg="white",width=3)
button_1.grid(row=4, column=1)

button_2 = tk.Button(root, text="2", font=("Arial", 16), command=lambda: add_digit("2"),bg="black",fg="white",width=3)
button_2.grid(row=4, column=2)

button_3 = tk.Button(root, text="3", font=("Arial", 16), command=lambda: add_digit("3"),bg="black",fg="white",width=3)
button_3.grid(row=5, column=0)

button_4 = tk.Button(root, text="4", font=("Arial", 16), command=lambda: add_digit("4"),bg="black",fg="white",width=3)
button_4.grid(row=5, column=1)

button_5 = tk.Button(root, text="5", font=("Arial", 16), command=lambda: add_digit("5"),bg="black",fg="white",width=3)
button_5.grid(row=5, column=2)

button_6 = tk.Button(root, text="6", font=("Arial", 16), command=lambda: add_digit("6"),bg="black",fg="white",width=3)
button_6.grid(row=6, column=0)

button_7 = tk.Button(root, text="7", font=("Arial", 16), command=lambda: add_digit("7"),bg="black",fg="white",width=3)
button_7.grid(row=6, column=1)

button_8 = tk.Button(root, text="8", font=("Arial", 16), command=lambda: add_digit("8"),bg="black",fg="white",width=3)
button_8.grid(row=6, column=2)

button_9 = tk.Button(root, text="9", font=("Arial", 16), command=lambda: add_digit("9"),bg="black",fg="white",width=3)
button_9.grid(row=7, column=1)

# Create the button to perform the calculation
button_calculate = tk.Button(root, text="Calculate", font=("Arial", 16), command=calculate,bg="black",fg="white")
button_calculate.grid(row=8, column=0)

# Create the label to display the result
label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.grid(row=8, column=1)

# Create the button to show the history
button_history = tk.Button(root, text="History", font=("Arial", 16), command=show_history,bg="black",fg="white")
button_history.grid(row=9, column=0)

# Create the button to delete the last digit of the currently focused input field
button_delete = tk.Button(root, text="Delete", font=("Arial", 16), command=delete_digit,bg="black",fg="white")
button_delete.grid(row=7, column=2)

# Create the list to store the history
history = []

# Define the symbols for each operation choice
choice_symbols = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}

# Bind the Delete key to the delete_digit() function
root.bind("<Delete>", lambda event: delete_digit())

root.mainloop()



