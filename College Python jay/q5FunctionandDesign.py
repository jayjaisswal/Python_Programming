def myRange(start=None, stop=None, step=None):
    # Determine the arguments provided and their default values
    if stop is None:
        # If stop is None, it means the function was called with only one argument
        # The provided argument is considered the stop value, and start is set to 0
        stop = start
        start = 0
    if step is None:
        # If step is None, it means the function was called with two arguments
        # The provided arguments are start and stop, and step is set to 1
        step = 1
    
    # Initialize an empty list to hold the values
    values = []
    
    # Check the direction of counting based on the step value
    if step > 0:
        # Counting up from start to stop (not including stop)
        current = start
        while current < stop:
            values.append(current)
            current += step
    elif step < 0:
        # Counting down from start to stop (not including stop)
        current = start
        while current > stop:
            values.append(current)
            current += step
    else:
        # Step cannot be zero
        raise ValueError("Step cannot be zero")
    
    return values

# Test the function myRange

# Test case 1: One argument (stop), start defaults to 0, step defaults to 1
print(myRange(5)) 
# Test case 2: Two arguments (start and stop), step defaults to 1
print(myRange(2, 6))  # Expected output: [2, 3, 4, 5]

# Test case 3: Three arguments (start, stop, and step)
print(myRange(1, 10, 2))

# Test case 4: Negative step (counting down)
print(myRange(10, 5, -1)) 