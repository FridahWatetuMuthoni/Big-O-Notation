/* 
Why Recurssion?
1. it breaks down large problems into small chunks
2. it is a fundamental used in more advanced algorithms

When to use Recurssion?
for problems that contain smaller instances of the same problem

Anatomy of Recursion:
Base Case: the smallest instance of a problem that is solved trivially
Recursive Case:
An instance of a problem that shricks the size of the inputt towards the base case
*/

//the factorial of a number n
//The runtime and space complexity is O(n)
function fact(n) {
    if (n === 1) {
        return 1
    }
    return n * fact(n - 1)
}

console.log(fact(100))
