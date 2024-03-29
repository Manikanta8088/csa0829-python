def remove_duplicates(sorted_array):
    if len(sorted_array) == 0:
        return []

    # Initialize variables
    unique_elements = [sorted_array[0]]

    # Iterate through the array starting from the second element
    for i in range(1, len(sorted_array)):
        # If the current element is different from the previous one, add it to the unique elements list
        if sorted_array[i] != unique_elements[-1]:
            unique_elements.append(sorted_array[i])

    return unique_elements

# Example usage:
sorted_array = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
result = remove_duplicates(sorted_array)
print("Array with duplicates removed:", result)
