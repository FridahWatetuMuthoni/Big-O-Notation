# BIG-O NOTATION AND ALGORITHMS ANALYSIS

## Big-O notation explanation

Big O notation is used to analyze the efficiency of an algorithm as its input approaches inifinity, which means that as the size of the input grows, how drastically do the space or time requirements grow with it.
For example lets say that we have a dentist and she takes 30 minutes to treat one patient.As her line of patients increases , the time that it takes for her to treat all of the patients will scale linearly with the number of patients waiting in line.
This is because it always takes her a constant amount of time to treat each individual patient which is 30 minutes. This gives us a general understanding of how long our dentist would take to treat 10 patients, 20 patients or even 100,000 patients. This is beacuse since we know that the dentist takes a contant amount of time, which is 30 minutes to treat each patient, we can always calculate the amount of time it would take for her to treat any number of patients by multiplying the number of patients times 30 minutes.
With this in mind, we can categorize her efficiency as being linear O(n). where n is the number of patients.
The amount of work it takes for her to finish her work scales linearly or proportionally with the number of patients., We use the same technique to determine the efficiency of algorithms.
We can get a general idea of how functions time efficiency scales by categorizing a given functions efficiency the same way that we categorize the dentist efficiency

## ORDER OF GROWTH HIERARCHY

    O(1) => constant time
                |
    O(log n) => logarithmic time
                |
    O(n)=> linear time
                |
    O(n log n)=> linearithmic time
                |
    O(n ^ 2) => Quadratic time
                |
    O(n ^ 3) => cubic time
                |
    O(2 ^ n) => exponential
                |
    O(n!) => factorial

## LOGARITHMS

A logarithm is the power that a number needs to be raised to to get some other number
In computer science unless specified otherwise, we can always assume that the number
that we want to raise to some power is 2, meaning that the base is always 2 unless specified otherwise.
log<sub>2</sub> 8 = 3
What is the number that we can raise 2 to to get 8 or 2 <sup>?</sup> = 8.
the answer is 3.
Therefore Log base 2 of 8 is 3

## MERGE SORT TIME COMPLEXITY

arr = [6, 1, 23, 3]
To understand the time complexity of mergesort we'll take an array of length 4 into consideration. We will pass this array to the mergesort function.
And what that call to the merge sort will do is divide the array approximately in half and those halves will be passed to merge sort recursively.
And after the arrays are done dividing , we will have arrays of length one meaning that we cant split the arrays any further. And to understand the time complexity of merge sort, we need to understand  O(log n). So as we know, in computer science, O(log n) is the same as log<sub>2</sub> n. where n is the length of our array which in our case is 4.

Therefore:
log<sub>2</sub> 4 = 2  because 2<sup>2</sup> = 4

which means that for array of length 4, there will be two levels of recurssion in our recursive tree structure.
And for each one of these levels, what we need to do is we need to touch every element of n, because we need to sort them and inorder to sort them we need to compare elements to create the merged array.
So that means that at each level we need to merge. And this merge function needs to touch every element of n.
Therefore, what that means is that each level has a time complexity of O(n) and there are O(log n) levels,
Hence the time complexity is going to be O(log n) * O(n) == O(n log n)

O(4 *  log 4) == O( 4 * 2 )
4 is the number of elements to traverse while 2 is the number of recursions in the recurssion tree structure

![alt text](./images/merge-sort-time-complexity.png)

## FIBONACCI TIME COMPLEXITY

![alt text](./images/fibonacci-time-complexity.png)

## FACTORIAL TIME COMPLEXITY

![alt text](./images/factorial-time-complexity-1.png)

![alt text](./images/factorial-time-complexity-2.png)

## COMMON MISTAKES

![alt text](./images/common-mistakes-1.png)

![alt text](./images/common-mistakes-2.png)
