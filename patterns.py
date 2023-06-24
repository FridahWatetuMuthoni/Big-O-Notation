"""
The box function has a time complexity of O(n^2)
if n == 5
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
which is a 5 x 5 matrix hence the area is 5 * 5 which is the
same as 5 ^ 2 which is n ^ 2
hence the time complexity is O(n ^ 2)
"""


def box(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print(end="\n")


"""
The cube function has a time complexity of O(n^3)
if n == 5
which is a 5 x 5 x 5 matrix hence the volume is 5 * 5 * 5 which is the
same as 5 ^ 3 which is n ^ 3
hence the time complexity is O(n ^ 3)
"""


def cube(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


cube(5)


def angle_90(n):
    for i in range(n):
        for j in range(i):
            print("* ", end="")
        print(end="\n")


def inverted_angle(n):
    n = n + 1
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(f"{j} ", end="")
        print(end="\n")
