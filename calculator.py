import tkinter as tk
import math

# Function to update the expression in the entry field
def press(key):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(key))

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()
        # Replace power operator
        expression = expression.replace('^', '**')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the sine of the input
def sine():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate the cosine of the input
def cosine():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate the tangent of the input
def tangent():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate the logarithm
def logarithm():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Setting up the main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x600")
window.config(bg="#f0f0f0")  # Light gray background

# Entry field for displaying expressions and results
entry = tk.Entry(window, font=("Arial", 24), width=15, borderwidth=2, relief="solid")
entry.pack(pady=20, padx=10)

# Button Layout
button_frame = tk.Frame(window)
button_frame.pack()

# Button colors
button_color = "#4CAF50"  # Green
button_color_hover = "#45a049"  # Darker green
button_color_num = "#2196F3"  # Blue
button_color_op = "#FF9800"  # Orange
button_color_func = "#9C27B0"  # Purple

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
    ('C', 6, 0), ('^', 6, 1), ('(', 6, 2), (')', 6, 3)
]

# Add buttons to the frame
for (text, row, col) in buttons:
    if text in ('+', '-', '*', '/', '=', '^'):
        button = tk.Button(button_frame, text=text, width=5, height=2, bg=button_color_op, fg="white", command=lambda t=text: press(t) if t != '=' else evaluate())
    elif text in ('sin', 'cos', 'tan', 'log'):
        button = tk.Button(button_frame, text=text, width=5, height=2, bg=button_color_func, fg="white", command=eval(text))
    elif text == 'C':
        button = tk.Button(button_frame, text=text, width=5, height=2, bg="red", fg="white", command=clear)
    else:
        button = tk.Button(button_frame, text=text, width=5, height=2, bg=button_color_num, fg="white", command=lambda t=text: press(t))

    button.grid(row=row, column=col, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
