# find common values between two arrays
def common_values(arr1, arr2):
    common = []
    for i in arr1:
        if i in arr2:
            common.append(i)
    return common
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(common_values(arr1, arr2))


# Remove duplicates elements from array
def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result
arr = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))


# Second largest number in array
def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]
arr = [10, 20, 4, 45, 99]
print(second_largest(arr))


# Count even and odd numbers
def count_even_odd(arr):
    even = 0
    odd = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
arr = [1, 2, 3, 4, 5, 6]
even, odd = count_even_odd(arr)
print("Even:", even)
print("Odd:", odd)


# Difference between largest and smallest
def diff_max_min(arr):
    return max(arr) - min(arr)
arr = [10, 5, 20, 3]
print(diff_max_min(arr))


# Check if array contains 12 and 23
def check_elements(arr):
    return 12 in arr and 23 in arr
arr = [12, 5, 23, 8]
print(check_elements(arr))


# Remove duplicates and return new array
def remove_duplicates(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr
arr = [1, 1, 2, 3, 3, 4]
print(remove_duplicates(arr))



