# the below function has two none nested loops that work on the same array of size n
# hence the time is O(n + n) == O(2n)
# we remove the constant hence the runtime is O(n)
def sum(arr):
    sum = 0
    product = 1
    for element in arr:
        sum += element
    for element in arr:
        product *= element
    print(f"sum = {sum}")


# The inner for loop has O(N) iterations and it is called N times. Therefore, the runtime is O( N^2).
# Another way we can see this is by inspecting what the "meaning" of the code is.
# It is printing all pairs (two_ element sequences).
# There are O(N^2) pairs; therefore, the runtime is O(N^2).
# if n = 4 = 4 *4 = 16 =n^2
def printPairs(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print(arr[i] + arr[j])


""" 
This pattern of for loop is very common. 
It's important that you know the runtime and that you deeply understand it. 
You can't rely on just memorizing common runtimes. Deep comprehension is important.
Counting the Iterations:
The first time through j runs for N-1 steps. 
The second time, it's N-2 steps. 
Then N-3 steps. And so on.
Therefore, the number of steps total is:
(N-1) + (N-2) + (N-3) + ... + 2 + 1
= 1 + 2 + 3 + 4 + 5 .....+ (n - 1)
The sum of an arithmetic progression is:
Sn = (n/2)(2a + (n-1)d)
Where:
Sn is the sum of the arithmetic progression.
n is the number of terms in the arithmetic progression.
a is the first term of the arithmetic progression.
d is the common difference between consecutive terms of the arithmetic progression.
By substituting the values of n, a, and d into the formula, you can calculate the sum of the arithmetic progression.
our progression is: 1 + 2 + 3 + 4 + ..... n - 1
n = n-1
hence:
Sn = ((n-1)/2)(2 + ((n-1)-1)(1))
The sum of 1 through n - 1 is  = n(n - 1) / 2
when we remove the constants the runtime is O(n^2)
"""


def print_unordered_pairs(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            count += 1
            print(f"{arr[i]}, {arr[j]}")
    print(count)


arry = [1, 2, 3, 4]
print_unordered_pairs(arry)

""" 
For each element ofarrayA, the inner for loop goes throughb iterations, whereb = arrayB. length. lfa = arrayA.length,then the runtime isO(ab).
If you saidO( N^2), then remember your mistake for the future. It's notO(N ^2) because there are two different inputs. Both matter. This is an extremely common mistake.
"""
# the runtime is O(ab)


def print_unordered_pairs(arr_a, arr_b):
    for i in range(0, len(arr_a)):
        for j in range(0, len(arr_b)):
            if (arr_a[i] < arr_b[j]):
                print(f"{arr_a[i]}, {arr_b[j]}")


""" 
Suppose we had an algorithm that took in an array of strings, sorted each string, and then sorted the full array. What would the runtime be?
Let's define new terms-and use names that are logical.
->Let 's' be the length of the longest string.
->Let 'a' be the length of the array. Now we can work through this in parts:
• Sorting each string is 0(s log s).
• We have to do this for every string (and there are a strings),so that's 0(a* s log s).
* Now we have to sort all the strings.There are 'a' strings,so you'll may be inclined to say that this takes O(a log a) time.
* This is what most candidates would say. You should also take into account that you need
to compare the strings. Each string comparison takes O(s) time. There areO(a log a) comparisons,
therefore this will take 0(a*s log a) time.
If you add up these two parts,you get0(a*s (log a + log s)).
This is it. There is no way to reduce it further.
"""
