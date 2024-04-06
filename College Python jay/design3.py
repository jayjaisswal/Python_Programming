import os

def process_path(pathname):
  """Processes a file or directory, displaying contents or recursing into subdirectories.

  Args:
    pathname: The path to the file or directory.
  """

  if os.path.isfile(pathname):
    # Display filename and contents
    print(f"File: {pathname}")
    with open(pathname, 'r') as file:
      print(file.read())
  else:
    # Recursively process directory contents
    print(f"Directory: {pathname}")
    for name in os.listdir(pathname):
      process_path(os.path.join(pathname, name))

def main():
  """Prompts user for a pathname and calls process_path."""

  pathname = input("Enter a pathname (file or directory): ")
  process_path(pathname)

if __name__ == "__main__":
  main()
