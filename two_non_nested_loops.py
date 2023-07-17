""" 
It is very possible for O(N) code to run faster than 0( 1) code for specific inputs. Big O just describes the rate of increase.
For this reason, we drop the constants in runtime. 
An algorithm that one might have described as 0(2N) is actuallyO(N).
Many people resist doing this. 
They will see code that has two (non-nested) for loops and continue this 0(2N).
They think they're being more "precise:'They're not.
consider the code below:
the runtime is O(n) and not O(2n) because we always drop the constants
"""


def max_value(arr):
    min = arr[0]
    max = arr[0]
    for element in arr:
        if (element < min):
            min = element
        if (element > max):
            max = element
    return [min, max]


def maximum_value(arr):
    min = arr[0]
    max = arr[1]

    for element in arr:
        if (element < min):
            min = element

    for element in arr:
        if (element > max):
            max = element
