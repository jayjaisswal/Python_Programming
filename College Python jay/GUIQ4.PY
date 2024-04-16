import tkinter as tk

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        
        # Initialize the game variables
        self.reset_game()
        
        # Create the GUI components
        self.guess_label = tk.Label(root, text=f"Computer's guess: {self.current_guess}")
        self.guess_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.too_small_button = tk.Button(root, text="Too small", command=self.too_small)
        self.too_small_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.too_large_button = tk.Button(root, text="Too large", command=self.too_large)
        self.too_large_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.correct_button = tk.Button(root, text="Correct", command=self.correct)
        self.correct_button.grid(row=1, column=2, padx=10, pady=10)
        
        self.new_game_button = tk.Button(root, text="New game", command=self.reset_game)
        self.new_game_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Disable the New game button at start-up
        self.new_game_button.config(state=tk.DISABLED)

    def reset_game(self):
        """Reset the game to the initial state."""
        # Initialize the range of possible guesses
        self.low = 1
        self.high = 100
        self.current_guess = (self.low + self.high) // 2
        
        # Update the label with the current guess
        if hasattr(self, 'guess_label'):
            self.guess_label.config(text=f"Computer's guess: {self.current_guess}")
        
        # Enable the game buttons and disable the New game button
        if hasattr(self, 'too_small_button'):
            self.too_small_button.config(state=tk.NORMAL)
        if hasattr(self, 'too_large_button'):
            self.too_large_button.config(state=tk.NORMAL)
        if hasattr(self, 'correct_button'):
            self.correct_button.config(state=tk.NORMAL)
        if hasattr(self, 'new_game_button'):
            self.new_game_button.config(state=tk.DISABLED)

    def too_small(self):
        """Handle the 'Too small' button press."""
        # Update the range and calculate a new guess
        self.low = self.current_guess + 1
        self.current_guess = (self.low + self.high) // 2
        
        # Update the label with the new guess
        self.guess_label.config(text=f"Computer's guess: {self.current_guess}")

    def too_large(self):
        """Handle the 'Too large' button press."""
        # Update the range and calculate a new guess
        self.high = self.current_guess - 1
        self.current_guess = (self.low + self.high) // 2
        
        # Update the label with the new guess
        self.guess_label.config(text=f"Computer's guess: {self.current_guess}")

    def correct(self):
        """Handle the 'Correct' button press."""
        # Display a message indicating the game is over
        self.guess_label.config(text=f"Computer's guess: {self.current_guess} (Correct!)")
        
        # Disable the game buttons and enable the New game button
        self.too_small_button.config(state=tk.DISABLED)
        self.too_large_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)
        self.new_game_button.config(state=tk.NORMAL)

# Create the main application window
root = tk.Tk()
game = GuessTheNumberGame(root)

# Start the main event loop
root.mainloop()
