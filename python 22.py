def count_vowels_consonants(statement):
    vowels = 0
    consonants = 0

    # Convert the statement to lowercase to simplify counting
    statement = statement.lower()

    # Define vowels
    vowel_set = set("aeiou")

    for char in statement:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants

def compare_counts(vowels, consonants):
    if vowels > consonants:
        return "Vowels"
    elif consonants > vowels:
        return "Consonants"
    else:
        return "Both vowels and consonants are equal"

def main():
    statement = input("Enter a statement: ")
    vowels, consonants = count_vowels_consonants(statement)
    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)
    max_count = compare_counts(vowels, consonants)
    print("The maximum count is in:", max_count)

if __name__ == "__main__":
    main()
