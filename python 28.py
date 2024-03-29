def count_space_line_vowels_consonants(file_name):
    space_count = 0
    line_count = 0
    vowels_count = 0
    consonants_count = 0

    # Define vowels
    vowels_set = set("aeiouAEIOU")

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line_count += 1
                for char in line:
                    if char.isspace():
                        space_count += 1
                    elif char.isalpha():
                        if char.lower() in vowels_set:
                            vowels_count += 1
                        else:
                            consonants_count += 1

        return space_count, line_count, vowels_count, consonants_count
    except FileNotFoundError:
        return None, None, None, None

def main():
    test_files = ["Hello.txt", "Welcome to saveetha School of Engineering"]

    for file_name in test_files:
        space_count, line_count, vowels_count, consonants_count = count_space_line_vowels_consonants(file_name)
        if space_count is not None:
            print(f"File: {file_name}")
            print("Number of spaces:", space_count)
            print("Number of lines:", line_count)
            print("Number of vowels:", vowels_count)
            print("Number of consonants:", consonants_count)
            print()
        else:
            print(f"File '{file_name}' not found.\n")

if __name__ == "__main__":
    main()
