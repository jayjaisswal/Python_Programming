import os

def display_file_contents(pathname):
    # Check if the pathname refers to a file
    if os.path.isfile(pathname):
        # Display the file name
        print(f"File: {pathname}")
        # Display the file contents
        with open(pathname, 'r') as file:
            contents = file.read()
            print(contents)
    # Check if the pathname refers to a directory
    elif os.path.isdir(pathname):
        # Get the list of names in the directory
        names = os.listdir(pathname)
        # Apply the function to each name in the directory
        for name in names:
            # Create the full path by joining the directory and the name
            full_path = os.path.join(pathname, name)
            # Recursively apply the function to the full path
            display_file_contents(full_path)
    else:
        print(f"Pathname {pathname} is neither a file nor a directory.")

# Test the function in a new program
if __name__ == "__main__":
    # Define a pathname (either a file or a directory)
    pathname = input("Enter the pathname of a file or directory: ")
    
    # Apply the function to the pathname
    display_file_contents(pathname)
