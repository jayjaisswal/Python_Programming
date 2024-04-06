import os

def view_file_contents():
  """Displays a list of files in the current directory and allows viewing the contents of a chosen file.

  Raises:
    FileNotFoundError: If the specified file is not found.
  """

  # Get a list of files in the current directory
  try:
    files = os.listdir(os.curdir)
  except PermissionError:
    print("Error: Access denied. You don't have permission to list files in this directory.")
    return

  # Print list of files
  print("Available files:")
  for filename in files:
    print(f"\t- {filename}")

  # Prompt user for file to view
  chosen_file = input("Enter the name of the file to view (or 'q' to quit): ")

  # Check for quit option
  if chosen_file.lower() == 'q':
    return

  # Open and display file contents (with error handling)
  try:
    with open(chosen_file, 'r') as file:
      contents = file.read()
      print("\nFile contents:")
      print(contents)
  except FileNotFoundError:
    print(f"Error: File '{chosen_file}' not found.")

def main_menu():
  """Displays the main menu and handles user choices."""

  # ... (rest of your main menu code)

  # Add option to view file contents
  print("5. View file contents")

  choice = input("Enter your choice (1-5, or 'q' to quit): ")

  if choice == '5':
    view_file_contents()
  # ... (handle other menu choices)

if __name__ == "__main__":
  main_menu()
