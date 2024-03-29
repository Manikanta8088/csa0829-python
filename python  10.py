def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

# Input a word from the user
word = input("Enter a word: ")

# Reverse the word using the reverse_word function
reversed_word = reverse_word(word)

# Print the reversed word
print("Reversed word:", reversed_word)
