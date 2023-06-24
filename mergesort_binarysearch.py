# The recursive portion of the mergesort as a time complexity of O(log n)
# But the merge sort function as a whole has the time complexity of O(n log n) because
# The merge function has a time complexity of O(n) therefore O(log n) * O(n) = O(n log n)
def merge_sort(arr):
    if (len(arr) <= 1):
        return arr

    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return left, right

# The merge function takes already sorted arrays and merges them together
# The merge function


def merge(left, right):
    left_i = 0
    right_j = 0
    sorted_arr = []
    while (left_i < len(left) and right_j < len(right)):
        if (left[left_i] < right[right_j]):
            sorted_arr.append(left[left_i])
            left_i += 1
        else:
            sorted_arr.append(right[right_j])
            right_j += 1
    while (left_i < len(left)):
        sorted_arr.append(left[left_i])
        left_i += 1

    while (right_j < len(right)):
        sorted_arr.append(right[right_j])
        right_j += 1

    return sorted_arr


arr = [54, 62, 93, 17, 77, 31, 44, 55, 20]
print(arr)
sorted_arr = merge_sort(arr)
print(sorted_arr)

# Looking for a value inside the sorted array using binary search


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = (start + end) // 2

        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return None


index = binary_search(sorted_arr, 54)
if index is not None:
    print(f"Value at {index} is {sorted_arr[index]}")
else:
    print("The value was not found")
