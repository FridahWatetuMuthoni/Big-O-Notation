"""
You got a list of items, where every item has a value and a weight. You got a bag that holds
a maximum weight of X.
Write a program that maximizes the value of the items you put into the bag whilst
ensuring that you dont exceed the maximum weight
"""

""" 
The time complexity of the `maximum_weight` function can be analyzed as follows:
1. Sorting the items: 
The `sorting_items` function sorts the `items` list based on the weight of each item. 
Sorting a list of size `n` has a time complexity of O(n log n).

2. Iterating over the sorted items: 
The `for` loop in the `maximum_weight` function iterates over the sorted items, 
which takes O(n) time, where `n` is the number of items in the list.

Overall, the time complexity of the `maximum_weight` function is dominated by the sorting step, which is O(n log n).
"""

items = [
    {id: 1, "value": 10, "weight": 3},
    {id: 2, "value": 6, "weight": 8},
    {id: 3, "value": 3, "weight": 3},
    {id: 4, "value": 4, "weight": 2},
    {id: 5, "value": 15, "weight": 1},
    {id: 6, "value": 9, "weight": 4},
    {id: 7, "value": 66, "weight": 2},
    {id: 8, "value": 26, "weight": 1},
]


def maximum_weight(items):
    max_weight = 8
    total = 0
    bag = []
    sorted_items = sorting_items(items)
    for item in sorted_items:  # O(n)
        if (item["weight"] == max_weight or item["weight"] > max_weight):
            continue
        else:
            if (total + item["weight"] > max_weight):
                continue
            else:
                total += item["weight"]
                bag.append(item)
    return bag


def sorting_items(arr):
    sorted_items = sorted(arr, key=lambda x: x["weight"])  # O(n log n)
    return sorted_items


bag = maximum_weight(items)
for item in bag:
    print(item)
