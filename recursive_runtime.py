"""
The tree will have depth N.
Each node (i.e., function call) has two children.
Therefore, each level will have twice as many calls as the one above it. 
The number of nodes on each level is:
level 0 => 2 ^ 0
level 1 = 2 ^ 1
level 2 = 2 ^ 2
level 3 = 2 ^ 3
level 4 = 2 ^ 4
Therefore, there will be 2^0 + 2^1 + 2^3 + 2^4 ....... + 2^n 
which is 2 ^ (n +1) - 1 nodes
Try to remember this pattern. 
When you have a recursive function that makes multiple calls,
the runtime will often (but not always) look like O( branches ^ depth),
where branches is the number of times each recursive call branches. 
In this case, this gives us O(2^N).
"""


def func(n):
    if (n <= 1):
        return 1
    return func(n - 1) + func(n - 1)


def func_2(n, sum=0):
    if (n <= 0):
        return sum
    sum += n
    return func_2(n - 1, sum)


result = func_2(5)
print(result)
