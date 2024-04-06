print("Name : Jay Kumar\nURN : 2203844 ")
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return line1.strip(), line2.strip()
    return None, None

def main():
    file1 = input("Enter the name of the first text file: ")
    file2 = input("Enter the name of the second text file: ")

    diff_line_file1, diff_line_file2 = compare_files(file1, file2)

    if diff_line_file1 is None and diff_line_file2 is None:
        print("Yes")
    else:
        print("No")
        print("First difference in file 1:", diff_line_file1)
        print("First difference in file 2:", diff_line_file2)

if __name__ == "__main__":
    main()
