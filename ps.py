import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        # Get user input for password length
        length = int(length_entry.get())
        
        if length < 6:
            result_label.config(text="Password length must be at least 6!", fg="red")
            return
        
        # Define character set for password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display generated password
        result_label.config(text=f"Generated Password: {password}", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

# Function to reset the form
def reset_form():
    length_entry.delete(0, tk.END)
    result_label.config(text="")

# Setting up the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(window, text="Password Generator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)

# Length Entry Label
length_label = tk.Label(window, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0")
length_label.pack(pady=5)

# Length Entry Field
length_entry = tk.Entry(window, font=("Arial", 12), width=15)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(window, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(window, text="Reset", font=("Arial", 12), bg="#f0ad4e", fg="white", command=reset_form)
reset_button.pack(pady=10)

# Result Label to Display Generated Password
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

# Exit Button
exit_button = tk.Button(window, text="Exit", font=("Arial", 12), bg="#ff6347", fg="white", command=window.quit)
exit_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
