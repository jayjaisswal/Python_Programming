print("Name : Jay Kumar\nURN : 2203844 ")
def print_unique_words(file_name):
    unique_words = set()

    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            unique_words.update(words)

    unique_words = sorted(unique_words)
    
    for word in unique_words:
        print(word)

file_name = input("Enter the name of the text file: ")
print("Unique words in alphabetical order:")
print_unique_words(file_name)
