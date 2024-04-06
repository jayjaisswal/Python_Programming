
# Write a recursive function that expects a pathname as an argument. The pathname can be 
# either the name of a file or the name of a directory. If the pathname refers to a file, its 
# name is displayed, followed by its contents. Otherwise, if the pathname refers to a 
# directory, the function is applied to each name in the directory. Test this function in a 
# new program
import os

def display_path_contents(path):
    """Recursively display the contents of a file or a directory."""
    if os.path.isfile(path):
        # If the path refers to a file, display its name and contents
        print("File:", path)
        with open(path, 'r') as file:
            print("Contents:")
            print(file.read())
    elif os.path.isdir(path):
        # If the path refers to a directory, apply the function to each item in the directory
        print("Directory:", path)
        for item in os.listdir(path):
            display_path_contents(os.path.join(path, item))
    else:
        # If the path doesn't refer to a file or directory, display an error message
        print("Invalid path:", path)

# Test the function
path = input("Enter the pathname: ")
display_path_contents(path)
