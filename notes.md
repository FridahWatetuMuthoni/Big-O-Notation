# Big O Notation Notes From Cracking the Coding Interview

## What is Big O Notation

Imagine the following scenario: You've got a file on a hard drive and you need to send it to your friend who lives across the country. You need to get the file to your friend as fast as possible. How should you send it?
Most people's first thought would be email, FTP, or some other means of electronic transfer. That thought is reasonable, but only half correct.
If it's a small file, you're certainly right. It would take 5 - 10 hours to get to an airport, hop on a flight, and then deliver it to your friend.
But what if the file were really, really large? Is it possible that it's faster to physically deliver it via plane?
Yes, actually it is. A one-terabyte (1 TB) file could take more than a day to transfer electronically. It would be much faster to just fly it across the country. If your file is that urgent (and cost isn't an issue), you might just want to do that.
What if there were no flights, and instead you had to drive across the country? Even then, for a really huge file, it would be faster to drive.

## Time Complexity

This is what the concept of asymptotic runtime, or big O time, means. We could describe the data transfer "algorithm" runtime as:
Electronic Transfer: 0( s ), where s is the size of the file. This means that the time to transfer the file increases linearly with the size of the file. (Yes, this is a bit of a simplification, but that's okay for these purposes).
Airplane Transfer: 0( 1) with respect to the size of the file. As the size of the file increases, it won't take any longer to get the file to your friend. The time is constant.
No matter how big the constant is and how slow the linear increase is, linear will at some point surpass constant.
There are many more runtimes than this. Some of the most common ones are O(log N), O(N log N), O(N), O(<sup>2</sup>) and 0( 2<sup>N</sup>). There's no fixed list of possible runtimes, though.
You can also have multiple variables in your runtime. For example, the time to paint a fence that's w meters wide and h meters high could be described as O(wh). If you needed p layers of paint, then you could say that the time is O(whp).
What is the relationship between best/worst/expected case and big 0/theta/omega?
It's easy for candidates to muddle these concepts (probably because both have some concepts of" higher': "lower" and "exactly right"), but there is no particular relationship between the concepts.
Best, worst, and expected cases describe the big O (or big theta) time for particular inputs or scenarios.
Big 0, big omega, and big theta describe the upper, lower, and tight bounds for the runtime.

## Space Complexity

Time is not the only thing that matters in an algorithm. We might also care about the amount of memory_ or space-required by an algorithm.
Space complexity is a parallel concept to time complexity. If we need to create an array of size n, this will require 0( n) space. If we need a two-dimensional array of size nxn, this will require O( n<sup>2</sup>) space.
Stack space in recursive calls counts, too. For example, code like this would takeO(n) time andO(n) space.

int sum(int n){
     if (n <= 0) {
        return 0;
     }
     return n + sum(n-1);
}

Each call adds a level to the stack.
-> sum(4)
-> sum(3)
-> sum(2)
-> sum(1)
-> sum(0)

Each of these calls is added to the call stack and takes up actual memory.
However, just because you have n calls total doesn't mean it takes O(n) space. Consider the below function, which adds adjacent elements between O and n:

int pairSumSequence(int n) {
    int sum = 0;
    for(int i = 0; i < n; i++)
    {
        sum += pairSum(i, i + 1);
    }
    return sum;
}

int pairSum(int a, int b){
    return a + b;
}
There will be roughly O(n) calls to pairSum. However, those calls do not exist simultaneously on the call stack, so you only needO(1) space.

## Drop the Non-Dominant Terms

What do you do about an expression such as O( N<sup>2</sup> + N) ? That second N isn't exactly a constant. But it's not especially important.
We already said that we drop constants. Therefore, 0(N<sup>2</sup> + N<sup>2</sup> ) would be O (N<sup>2</sup>). If we don't care about that latter <sup>2</sup> term, why would we care about N? We don't.
