""" 
The time complexity of the log_func function is O(log n)

log_func(8) ->base call
    |
log_func(4) -> level one
    |
log_func(2) -> level two
    |
log_func(1) -> level three
    |
log_func(0)

The log_func goes three levels deep before n == 0
log base 2 of 8 is 3
"""


def log_func(n, count=0):
    if (n == 0):
        print(count)
        return "Done"
    count += 1
    n = n // 2
    return log_func(n, count)


# print(log_func(8))

# the log_n function has a time complexity of O(log n)


def log_n(n):
    count = 0
    while (n > 1):
        n = n // 2
        count += 1
    print("While Loop Done")
    return count


# count = log_n(8)
# print(count)

# the binary search has a O(log n) time complexity

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


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binary_search(arr, 3)
# print(index)


def binary_search_recurssion(arr, start, end, target):
    if (start >= end):
        return None
    mid = (start + end) // 2
    if (arr[mid] == target):
        return mid
    elif (arr[mid] > target):
        end = mid - 1
        return binary_search_recurssion(arr, start, end, target)
    else:
        start = mid + 1
        return binary_search_recurssion(arr, start, end, target)


start = 0
end = len(arr) - 1
result = binary_search_recurssion(arr, start, end, 20)
print(f"Binary Recurssion Result: {result}")
