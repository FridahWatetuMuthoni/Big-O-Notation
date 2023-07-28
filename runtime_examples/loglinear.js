/*
LogLinear runtime:
O(n * log n)=> O(nlogn)
Loglinear occurs when linear behaviour is nested in log steps
Loglinear is bigger than n but smaller than N^2

In JavaScript, the `str.slice()` function is used to extract a portion of a string and 
return it as a new string without modifying the original string. 
The time complexity of `str.slice()` is O(n), where n is the length of the extracted substring.
The reason for this linear time complexity is that the function needs to copy each character from the original string to form the new substring.
It doesn't matter whether you slice a small or large portion of the string; the time it takes will be directly proportional to the length of the extracted substring.
Here's an example of using `str.slice()`:
const originalString = "Hello, World!";
const extractedSubstring = originalString.slice(0, 5);
// "Hello"
In this example, we are extracting the substring from index 0 to 4 (5 characters), 
so the time complexity will be O(5), which simplifies to O(n) in big O notation as we consider the worst-case scenario.
*/

const bar = (str) => {
    console.log(str)
    if (str.length <= 1) {
        return
    }
    const mid = Math.floor(str.length / 2)
    console.log(mid)
    bar(str.slice(0, mid))
}

bar("pentagonagencies")

/*
To get the runtime of the foo function we need to consider both the height and the width of the
function:
For the height/depth part:
if n = 8 the amount of recursive calls is 3. Therefore the height/ depth of the recurssive
calls is Log n => log 8 = 3 => hence the three calls
8 => 4 => 2 => 1

For the width part:
For each level of the recursive function we iterate thru each item hence O(n)

To get the total runtime we need to multiply height * width
hence: log n * n => O(nlogn)
*/

const foo = (array) => {
    let str = "";
    for (let i = 0; i < array.length; i++){
        str += array[i]
    }
    console.log(str)
    console.log("-------------")

    if (array.length <= 1) {
        return
    }
    const mid = Math.floor(str.length / 2)
    const left = str.slice(0, mid)
    const right = str.slice(mid)
    foo(left)
    foo(right)
}

foo(['freecodecamp', 'university', 'cooperation'])