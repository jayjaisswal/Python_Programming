import tkinter as tk
from tkinter import messagebox

def submit_form():
    """Handle form submission."""
    # Retrieve the values from the input fields
    name = entry_name.get()
    email = entry_email.get()
    gender = gender_var.get()
    hobbies = []
    if hobby_reading_var.get():
        hobbies.append("Reading")
    if hobby_sports_var.get():
        hobbies.append("Sports")
    if hobby_traveling_var.get():
        hobbies.append("Traveling")
    
    # Display a summary of the submitted data
    summary = (
        f"Form Summary:\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Gender: {gender}\n"
        f"Hobbies: {', '.join(hobbies) if hobbies else 'None'}"
    )
    messagebox.showinfo("Form Submission", summary)

# Create the main application window
window = tk.Tk()
window.title("General Form")

# Define variables for different options
gender_var = tk.StringVar(value="Male")
hobby_reading_var = tk.BooleanVar()
hobby_sports_var = tk.BooleanVar()
hobby_traveling_var = tk.BooleanVar()

# Name entry
tk.Label(window, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

# Email entry
tk.Label(window, text="Email:").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(window)
entry_email.grid(row=1, column=1)

# Gender options
tk.Label(window, text="Gender:").grid(row=2, column=0, sticky="w")
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky="w")

# Hobbies options
tk.Label(window, text="Hobbies:").grid(row=3, column=0, sticky="w")
tk.Checkbutton(window, text="Reading", variable=hobby_reading_var).grid(row=3, column=1, sticky="w")
tk.Checkbutton(window, text="Sports", variable=hobby_sports_var).grid(row=3, column=2, sticky="w")
tk.Checkbutton(window, text="Traveling", variable=hobby_traveling_var).grid(row=3, column=3, sticky="w")

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=4, pady=10)

# Start the application
window.mainloop()
