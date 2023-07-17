""" 
Suppose you have an algorithm that has two steps. 
When do you multiply the runtimes and when do you add them?
In the example one, we do A chunks of work then B chunks of work.
Therefore, the total amount of work is O(A + B).
In the example two, we do B chunks of work for each element in A. 
Therefore, the total amount of work is O(A * B).
If your algorithm is in the form "do this, then, when you're all done, do that"then you add the runtimes.
If your algorithm is in the form "do this for each time you do that"then you multiply the runtimes.
"""

# the runtime of this one is O(a + b)


def example_one(arr1, arr2):
    for element in arr1:
        print(element)
    for element in arr2:
        print(element)


# the runtime of this is O(a*b)
def example_two(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print(i, j)
