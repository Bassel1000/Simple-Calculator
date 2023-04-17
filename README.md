# Simple-Calculator
Calcuator with basic math operations made with tkinter
1. We have imported tkinter and math module
```python
from tkinter import *
import math
```
2. We have created a root window
```python
root = Tk()

root.title("Calculator")
```
3. We have created a text entry box by using Entry class of tkinter
```python
e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

```
4. We have created a function button_click() which will take the number as an argument 
   and will display the number on the text box
```python
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
```
5. We have created a function button_clear() which will clear the text box
```python
def button_clear():
    e.delete(0, END)
```
6. We have created a function button_add() which will take the first number and will 
   store it in a global variable f_num and will delete the text box
```python
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
```
7. We have created a function button_equal() which will take the second number and will 
   delete the text box and will display the result of the operation
```python
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
```
8. We have created a function button_subtract() which will take the first number and will 
   store it in a global variable f_num and will delete the text box
```python
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
```
9. We have created a function button_multiply() which will take the first number and will 
   store it in a global variable f_num and will delete the text box
```python
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    
```
10. We have created a function button_divide() which will take the first number and will 
   store it in a global variable f_num and will delete the text box
```python
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
```
## Define buttons 
1. We are making use of the Button widget of the tkinter library to create a button.
2. The first argument is the name of the root window.
3. The second argument is the text that is to be displayed on the button.
4. The third argument is the "padx" and "pady" arguments which are used to set the width and height of the button.
5. The last argument is the "command" argument which links the button to a function. In this case, we are using the "lambda" keyword to link the button to the function. The lambda keyword allows us to create a function on the fly.
6. We are using the "lambda" keyword to pass the value of the button to the function. The value can be accessed using the "num" argument in the function.
```python
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))

button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))

button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))

button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))

button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))

button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))

button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)

button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)

button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)

button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)

button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

```
### last step to put buttons on the screen 
```python
button_1.grid(row=3, column=0)

button_2.grid(row=3, column=1)

button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)

button_4.grid(row=2, column=0)

button_5.grid(row=2, column=1)

button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)

button_8.grid(row=1, column=1)

button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)

button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)

button_multiply.grid(row=6, column=1)

button_divide.grid(row=6, column=2)

root.mainloop()
```
# Here is the final result
![image](https://user-images.githubusercontent.com/94708469/232416390-817c6365-1c71-4399-95f9-09f40527b9d0.png)
