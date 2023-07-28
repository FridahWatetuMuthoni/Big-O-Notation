# The Number of Iterations performed by a function for n

## What is the time complexity of this function?

def some_function(n):
    i = 1
    while(i <= n):
        print(“Hello World”)
        i += 2

The time complexity of the given function can be analyzed by examining the number of iterations the while loop performs.

The function you provided has a while loop that keeps running until a condition is met. In this case, the condition is i <= n, which means the loop will continue as long as i is less than or equal to n.

Inside the loop, the function prints "Hello World" and increments i by 2. So, in each iteration of the loop, the value of i increases by 2.

To calculate the time complexity of this function, we need to figure out how many iterations the loop will go through before the condition i <= n is no longer true.

Let's say we have a number n (for example, n = 10). We want to find out how many times we need to add 2 to a starting value of 1 until the value becomes greater than n.

We can start with i = 1 and add 2 in each iteration: 1, 3, 5, 7, 9, 11. We stop when i becomes greater than n. In this case, i = 11 is greater than n = 10, so we needed 5 iterations to reach this point.

Now, instead of doing this manually, we can use a mathematical formula to find the number of iterations. The formula we can use is:

Sum = (n / 2) * (first term + last term)

In this case, the first term is 1 (the starting value of i), and the last term is the value of i when the condition i <= n is no longer true.

Using this formula, we can calculate the sum of the arithmetic progression. In our example, it would be (10 / 2) * (1 + 11) = 55.

So, for a given value of n, the number of iterations required is the sum of an arithmetic progression. But we want to find the largest integer value of i that satisfies i <= n. We can solve this inequality using a quadratic equation.

The equation is: k^2 + k - 2n > 0

Here, k represents the number of iterations needed. We want to find the value of k that makes the inequality true.

Using the quadratic formula, which is a formula to solve quadratic equations, we can find the value of k:

k = (-1 + sqrt(1 + 8n)) / 2

However, we are interested in the largest integer value of k. So we round up this value to the nearest integer, which is done using the ceiling function (represented by ceil).

Therefore, the time complexity of the given function is approximately sqrt(n), where sqrt stands for the square root function.

## Solving the quadratic equation

Let's break down the process of solving the inequality k * (k + 1) / 2 > n step by step:

1. Start with the given inequality: k * (k + 1) / 2 > n.

2. Multiply both sides of the inequality by 2 to eliminate the fraction: 2 *(k* (k + 1) / 2) > 2 * n.

   This simplifies to: k * (k + 1) > 2n.

3. Expand the left side of the inequality: k^2 + k > 2n.

4. Rearrange the inequality by subtracting 2n from both sides: k^2 + k - 2n > 0.

   Now, we have a quadratic inequality in the form of ax^2 + bx + c > 0, where a = 1, b = 1, and c = -2n.

5. To solve this quadratic inequality, we need to find the values of k for which the quadratic expression is greater than zero.

6. One approach is to find the roots of the quadratic equation k^2 + k - 2n = 0. However, in this case, we don't need the exact roots; we just need to know the range of values for which the inequality is satisfied.

7. We can use the quadratic formula to find the roots of the quadratic equation: k = (-b ± sqrt(b^2 - 4ac)) / (2a).

   Plugging in the values a = 1, b = 1, and c = -2n, we get: k = (-1 ± sqrt(1 - 4(-2n))) / 2.

8. Simplifying the expression inside the square root: k = (-1 ± sqrt(1 + 8n)) / 2.

9. Since we are interested in the values of k for which the inequality is greater than zero (k > 0), we can discard the negative root.

10. The positive root gives us the lower bound of the values of k that satisfy the inequality: k = (-1 + sqrt(1 + 8n)) / 2.

11. To find the largest integer value of k that satisfies the inequality, we can take the ceiling of this expression using the ceiling function (represented by ceil()).

   Therefore, the largest integer value of k that satisfies the inequality is: k = ceil((-1 + sqrt(1 + 8n)) / 2).

12. Finally, the time complexity of the given function is O(ceil((-1 + sqrt(1 + 8n)) / 2)), or simply O(sqrt(n)), as we can ignore the ceiling function and constant factors in asymptotic analysis.
