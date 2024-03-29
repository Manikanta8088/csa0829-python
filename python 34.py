import string

def count_and_print_special_characters(line):
    special_characters = string.punctuation
    special_chars_count = 0

    print("Special characters in the line:")
    for char in line:
        if char in special_characters:
            print(char, end=" ")
            special_chars_count += 1

    print("\nNumber of special characters:", special_chars_count)

if __name__ == "__main__":
    line = input("Enter a line: ")
    count_and_print_special_characters(line)
