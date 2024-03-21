print("Name : Jay Kumar\nURN : 2203844 ")
total_sum = 0
count = 0
# Input loop to receive numbers from the user
print("Enter numbers (press Enter to finish):")
while True:
    num_input = input("Enter a number: ")
    
    # Check if the user pressed Enter to indicate finish
    if num_input == "":
        break
    
    try:
        # Convert input to float and update sum and count
        num = float(num_input)
        total_sum += num
        count += 1
    except ValueError:
        print("Please enter a valid number.")

# Check if any numbers were entered
if count == 0:
    print("No numbers were entered.")
else:
    # Calculate average
    average = total_sum / count
    
    # Print sum and average
    print("Sum of the numbers:", total_sum)
    print("Average of the numbers:", average)
