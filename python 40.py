def find_mth_maximum_and_nth_minimum(arr, m, n):
    arr.sort()  
    mth_maximum = arr[-m]  
    nth_minimum = arr[n - 1]  
    return mth_maximum, nth_minimum

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the array of numbers separated by spaces: ").split()]
    m = int(input("Enter the value of M: "))
    n = int(input("Enter the value of N: "))

    mth_maximum, nth_minimum = find_mth_maximum_and_nth_minimum(arr, m, n)

    
    sum_result = mth_maximum + nth_minimum
    difference_result = mth_maximum - nth_minimum

    print(f"Mth maximum number: {mth_maximum}")
    print(f"Nth minimum number: {nth_minimum}")
    print(f"Sum of Mth maximum and Nth minimum: {sum_result}")
    print(f"Difference of Mth maximum and Nth minimum: {difference_result}")
