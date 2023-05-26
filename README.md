# Calculator
This is a simple calculator GUI built using Python and the Tkinter library. The calculator allows the user to enter two numbers and choose an operation to perform (addition, subtraction, or multiplication). The result is displayed in a label on the GUI, and the history of calculations is stored in a list.

Getting Started
To run the calculator, you'll need to have Python and the Tkinter library installed on your computer. You can download Python from the official website (https://www.python.org/downloads/) and install Tkinter using pip: ```pip install tkinter```
# How to Use
1.Enter the first number in the "Enter first number" input field. <br>
2.Enter the second number in the "Enter second number" input field. <br>
3.Choose the operation you want to perform by clicking on one of the radio buttons. <br>
4.Click the "Calculate" button to perform the operation and display the result in the "Result" label. <br>
5.To view the history of calculations, click the "History" button. <br>
6.To delete the last digit of the currently focused input field, click the "Delete" button. <br>
# Code Explanation
The code is divided into several functions:

calculate: This function is called when the user clicks the "Calculate" button. It gets the values of the two input fields and the selected operation, performs the calculation, and displays the result in the "Result" label. <br>
show_history: This function is called when the user clicks the "History" button. It joins the history list into a string and displays it in a message box. <br>
delete_digit: This function is called when the user clicks the "Delete" button. It checks which input field is currently focused and deletes the last digit of that field. <br>
main: This function creates the GUI using the Tkinter library. <br>
## The GUI consists of several widgets:

Two input fields for the two numbers. <br>
Three radio buttons for the three operations. <br>
A "Calculate" button to perform the calculation <br>
A "History" button to view the history of calculations. <br>
A "Delete" button to delete the last digit of the currently focused input field. <br>
A "Result" label to display the result of the calculation. <br>
A "Enter first number" label to indicate the purpose of the first input field. <br>
A "Enter second number" label to indicate the purpose of the second input field. <br>
# Result
![image](https://github.com/Bassel1000/Simple-Calculator/assets/94708469/6c35ece2-b908-48a4-990c-3deb86b7b85a)
![image](https://github.com/Bassel1000/Simple-Calculator/assets/94708469/4d58a58b-f891-426e-942f-f6fba53469c6)

