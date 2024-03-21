import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height * height)
    
    if bmi < 18.5:
        result_label.config(text=f"Your BMI is {bmi:.2f}, you are underweight", fg="blue")
    elif bmi < 25:
        result_label.config(text=f"Your BMI is {bmi:.2f}, you have a normal weight", fg="green")
    elif bmi < 30:
        result_label.config(text=f"Your BMI is {bmi:.2f}, you are slightly overweight", fg="orange")
    elif bmi < 35:
        result_label.config(text=f"Your BMI is {bmi:.2f}, you are obese", fg="red")
    else:
        result_label.config(text=f"Your BMI is {bmi:.2f}, you are clinically obese", fg="darkred")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=0, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="", fg="black")
result_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Start the main event loop
root.mainloop()
