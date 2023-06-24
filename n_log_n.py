"""
The outer loop which is the while loop has a time complexity of O(log n)
This is because log base 2 of 4 is 2 and we iterated twice in the while loop when n was 4
But the inner loop which is the for loop has a time complexity of O(n) because as n increases 
so does the amount of iterations therefore the below function has a time complexity of 
O(n log n)
example:
when n = 4
O(n log n) = O(4 log 4) = O(4 * 2) => we performed four iterations of the for loop twice because 
of the while loop hence O(n log n)
"""


def n_log_n(n):
    y = n
    while (n > 1):  # O(log n)
        n = n // 2
        for i in range(1, y+1):  # O(n)
            print(i)


n_log_n(4)
