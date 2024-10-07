import random
import tkinter as tk
from tkinter import messagebox

# Function to get computer's choice
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "user"
    else:
        return "computer"

# Function to handle user choice and game logic
def play_game(user_choice):
    computer_choice = get_computer_choice()
    
    # Display choices
    computer_choice_label.config(text=f"Computer chose: {computer_choice}", fg="blue")
    user_choice_label.config(text=f"You chose: {user_choice}", fg="blue")
    
    # Determine the winner
    winner = get_winner(user_choice, computer_choice)
    if winner == "user":
        result_label.config(text="You win!", fg="green")
        scores['user'] += 1
    elif winner == "computer":
        result_label.config(text="Computer wins!", fg="red")
        scores['computer'] += 1
    else:
        result_label.config(text="It's a tie!", fg="orange")
    
    # Update score display
    score_label.config(text=f"Score -> You: {scores['user']} | Computer: {scores['computer']}", fg="black")

# Function to reset the game
def reset_game():
    scores['user'] = 0
    scores['computer'] = 0
    score_label.config(text=f"Score -> You: 0 | Computer: 0", fg="black")
    user_choice_label.config(text="You chose: ", fg="black")
    computer_choice_label.config(text="Computer chose: ", fg="black")
    result_label.config(text="")

# Main window setup
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("400x350")
window.config(bg="#f0f0f0")  # Background color

# Initial Scores
scores = {'user': 0, 'computer': 0}

# Title
title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=10)

# User and Computer Choice Labels
user_choice_label = tk.Label(window, text="You chose: ", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="Computer chose: ", font=("Arial", 12), bg="#f0f0f0")
computer_choice_label.pack()

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), pady=10, bg="#f0f0f0")
result_label.pack()

# Score Label
score_label = tk.Label(window, text="Score -> You: 0 | Computer: 0", font=("Arial", 12), pady=10, bg="#f0f0f0")
score_label.pack()

# Buttons for choices
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, bg="#ffcccb", font=("Arial", 12), command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, bg="#add8e6", font=("Arial", 12), command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, bg="#90ee90", font=("Arial", 12), command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Reset Button
reset_button = tk.Button(window, text="Reset Game", width=20, bg="#ffeb3b", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(window, text="Exit", width=20, bg="#ff6347", font=("Arial", 12), command=window.quit)
exit_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
