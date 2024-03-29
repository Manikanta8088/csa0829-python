def remove_duplicates(arr):
    if not arr:
        return []

    result = [arr[0]]

    for num in arr[1:]:
        if num != result[-1]:
            result.append(num)

    return result

if __name__ == "__main__":
    sorted_array = [int(x) for x in input("Enter the sorted array separated by spaces: ").split()]
    unique_array = remove_duplicates(sorted_array)
    print("Array after removing duplicates entirely:", unique_array)
