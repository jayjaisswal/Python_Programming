import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the Fahrenheit value to Celsius and display the result."""
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    celsius_entry.delete(0, tk.END)
    celsius_entry.insert(0, f"{celsius:.2f}")

def celsius_to_fahrenheit():
    """Convert the Celsius value to Fahrenheit and display the result."""
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    fahrenheit_entry.delete(0, tk.END)
    fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")

# Create the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Set up the labels and entry fields
tk.Label(root, text="Fahrenheit:").grid(row=0, column=0, padx=10, pady=10)
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=10)
fahrenheit_entry.insert(0, "32.0")

tk.Label(root, text="Celsius:").grid(row=0, column=1, padx=10, pady=10)
celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1, padx=10, pady=10)
celsius_entry.insert(0, "0.0")

# Set up the buttons
tk.Button(root, text=">>>>", command=fahrenheit_to_celsius).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="<<<<", command=celsius_to_fahrenheit).grid(row=2, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
