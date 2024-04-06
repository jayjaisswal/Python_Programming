# Q.4 Write a program that computes and prints the average of the numbers in a text file. You 
# should make use of two higher-order functions to simplify the design.
from functools import reduce

def read_numbers_from_file(filename):
    """Read numbers from a text file and return them as a list of floats."""
    with open(filename, 'r') as file:
        numbers = file.read().split()
        return list(map(float, numbers))

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

def main():
    filename = input("Enter the name of the file containing numbers: ")
    try:
        numbers = read_numbers_from_file(filename)
        average = calculate_average(numbers)
        print("Average:", average)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
