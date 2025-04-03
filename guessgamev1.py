import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title Label
        self.title_label = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Instructions Label
        self.instructions_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 12))
        self.instructions_label.pack(pady=5)

        # Input Field
        self.guess_entry = tk.Entry(root, font=("Helvetica", 12))
        self.guess_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Helvetica", 12))
        self.submit_button.pack(pady=10)

        # Feedback Label
        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.", fg="red")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too high! Try again.", fg="red")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="magenta")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
