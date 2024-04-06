# A file concordance tracks the unique words in a file and their frequencies. Write a 
# program that displays a concordance for a file. The program should output the unique 
# words and their frequencies in alphabetical order. Variations are to track sequences of 
# two words and their frequencies, or n words and their frequencies
def generate_concordance(file_name):
    """Generates a concordance for the given text file."""
    concordance = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Remove punctuation and convert to lowercase for consistency
                word = word.strip('.,!?;:').lower()
                if word:
                    concordance[word] = concordance.get(word, 0) + 1
    return concordance

def display_concordance(concordance):
    """Displays the concordance in alphabetical order."""
    for word, frequency in sorted(concordance.items()):
        print(f"{word}: {frequency}")

def main():
    file_name = input("Enter the name of the file: ")
    try:
        concordance = generate_concordance(file_name)
        print("\nConcordance:")
        display_concordance(concordance)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
