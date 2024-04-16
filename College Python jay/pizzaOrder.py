import tkinter as tk
from tkinter import messagebox

# Function to calculate the total cost and display the order summary
def place_order():
    # Get the size price
    size = size_var.get()
    if size == "Small":
        size_price = 5
    elif size == "Medium":
        size_price = 7
    elif size == "Large":
        size_price = 9

    # Calculate topping cost
    toppings = []
    toppings_price = 0
    if pepperoni_var.get():
        toppings.append("Pepperoni")
        toppings_price += 1
    if sausage_var.get():
        toppings.append("Sausage")
        toppings_price += 1
    if mushrooms_var.get():
        toppings.append("Mushrooms")
        toppings_price += 1
    if olives_var.get():
        toppings.append("Olives")
        toppings_price += 1
    if onions_var.get():
        toppings.append("Onions")
        toppings_price += 1

    # Get crust type
    crust_type = crust_var.get()

    # Calculate total cost
    total_cost = size_price + toppings_price

    # Display order summary
    order_summary = (
        f"Pizza Order Summary:\n"
        f"Size: {size}\n"
        f"Crust: {crust_type}\n"
        f"Toppings: {', '.join(toppings) if toppings else 'None'}\n"
        f"Total Cost: ${total_cost:.2f}\n"
    )
    messagebox.showinfo("Order Summary", order_summary)

# Create the main application window
window = tk.Tk()
window.title("Domino's Pizza Order")

# Define variables for different options
size_var = tk.StringVar(value="Medium")
crust_var = tk.StringVar(value="Regular")
pepperoni_var = tk.BooleanVar()
sausage_var = tk.BooleanVar()
mushrooms_var = tk.BooleanVar()
olives_var = tk.BooleanVar()
onions_var = tk.BooleanVar()

# Size options
tk.Label(window, text="Select pizza size:").grid(row=0, column=0, sticky="w")
tk.Radiobutton(window, text="Small", variable=size_var, value="Small").grid(row=0, column=1, sticky="w")
tk.Radiobutton(window, text="Medium", variable=size_var, value="Medium").grid(row=0, column=2, sticky="w")
tk.Radiobutton(window, text="Large", variable=size_var, value="Large").grid(row=0, column=3, sticky="w")

# Crust type options
tk.Label(window, text="Select crust type:").grid(row=1, column=0, sticky="w")
tk.Radiobutton(window, text="Regular", variable=crust_var, value="Regular").grid(row=1, column=1, sticky="w")
tk.Radiobutton(window, text="Thin", variable=crust_var, value="Thin").grid(row=1, column=2, sticky="w")
tk.Radiobutton(window, text="Stuffed", variable=crust_var, value="Stuffed").grid(row=1, column=3, sticky="w")

# Toppings options
tk.Label(window, text="Select toppings:").grid(row=2, column=0, sticky="w")
tk.Checkbutton(window, text="Pepperoni", variable=pepperoni_var).grid(row=2, column=1, sticky="w")
tk.Checkbutton(window, text="Sausage", variable=sausage_var).grid(row=2, column=2, sticky="w")
tk.Checkbutton(window, text="Mushrooms", variable=mushrooms_var).grid(row=2, column=3, sticky="w")
tk.Checkbutton(window, text="Olives", variable=olives_var).grid(row=3, column=1, sticky="w")
tk.Checkbutton(window, text="Onions", variable=onions_var).grid(row=3, column=2, sticky="w")

# Order button
order_button = tk.Button(window, text="Place Order", command=place_order)
order_button.grid(row=4, column=0, columnspan=4, pady=10)

# Start the application
window.mainloop()
