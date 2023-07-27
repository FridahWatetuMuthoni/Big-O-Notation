/*
Analyzing Recursive Code Space and Time Complexity
number of function calls in each function call ^ depth
Our space complexity should consider the space taken by recursive calls on the call stack

*/

const zoom = (n)=>{
    if(n === 0){
        console.log("liftoff!")
        return
    }
    console.log(n)
    zoom(n - 1)
}

zoom(5)
//5
//4
//3
//2
//1
//The runtime of the zoom function is 1^n => O(n)
//space complexity is O(n)

/*
The time complexity of the fib call is
number of recurcive function calls in the function raised to n
2^n
the runtime = O(2^n)
space complexity = O(n)
*/
const fib = (n)=>{
    if(n === 1){
        return 1
    }
    if(n === 2){
        return 1
    }
    if(n > 2){
        return fib(n - 2) + fib(n - 1)
    }
}

/*
The time complexity of the zap function is
O(n/2) => O(n * 1/2) => O(n)
and the space complexity is O(n)
 */
const zap = (n)=>{
    if(n < 1){
        console.log("blastoff!")
        return
    }
    console.log(n)
    zap(n - 2)
}

