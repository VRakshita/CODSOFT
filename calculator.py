from tkinter import *

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, END)
    entry_display.insert(END, str(current) + str(number))

def button_clear():
    entry_display.delete(0, END)

def button_equal():
    expression = entry_display.get()
    result = eval(expression)
    entry_display.delete(0, END)
    entry_display.insert(END, str(result))

# Create the main window
window = Tk()
window.title("Calculator")
window.configure(bg="#E8F5E9")

# Create an entry field to display the numbers and results
entry_display = Entry(window, font=("Arial", 20), bg="#F1F8E9", fg="#37474F", bd=0, justify=RIGHT)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
buttons = []
for i in range(10):
    button = Button(window, text=str(i), font=("Arial", 14, "bold"), bg="#81C784", fg="#37474F", bd=0,
                    command=lambda i=i: button_click(i))
    buttons.append(button)

# Position the number buttons on the grid
row_num = 1
col_num = 0
for i in range(9, -1, -1):
    buttons[i].grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num == 3:
        col_num = 0
        row_num += 1

# Create operator buttons
operators = ["+", "-", "*", "/"]
row_op = 1
col_op = 3
for operator in operators:
    button = Button(window, text=operator, font=("Arial", 14, "bold"), bg="#FFB74D", fg="#37474F", bd=0,
                    command=lambda operator=operator: button_click(operator))
    button.grid(row=row_op, column=col_op, padx=5, pady=5)
    row_op += 1

# Create other buttons
button_clear = Button(window, text="C", font=("Arial", 14, "bold"), bg="#EF5350", fg="#FFFFFF", bd=0, command=button_clear)
button_clear.grid(row=4, column=0, padx=5, pady=5)

button_zero = Button(window, text="0", font=("Arial", 14, "bold"), bg="#81C784", fg="#37474F", bd=0,
                     command=lambda: button_click(0))
button_zero.grid(row=4, column=1, padx=5, pady=5)

button_dot = Button(window, text=".", font=("Arial", 14, "bold"), bg="#81C784", fg="#37474F", bd=0,
                    command=lambda: button_click('.'))
button_dot.grid(row=4, column=2, padx=5, pady=5)

button_equal = Button(window, text="=", font=("Arial", 14, "bold"), bg="#4DD0E1", fg="#37474F", bd=0, command=button_equal)
button_equal.grid(row=4, column=3, padx=5, pady=5)

# Run the main window loop
window.mainloop()
