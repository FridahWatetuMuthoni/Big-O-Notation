/*
Exponential => O(c^n)
n is the size of the input
c is some constant
includes O(2^n), O(3^n) etc

The difference between O(log n) and O(2^n) is
the first one includes continuosly dividing n by 2 => depth = O(log n)
and the second one continuosly subtract n by 1 => depth = n but it happens twice
because of the two function calls each time => 2^n. if the function was called three times
the runtime would have been O(3^n)
*/

/*
The time complexity of the foo function is O(2 ^n)
*/
const foo = (n) => {
    if (n === 1) {
        return
    }
    foo(n - 1)
    foo(n - 1)
}


/*
The time complexity of the zap function is O(2 ^(n/2)) => O(2 ^(n * 1/2) ) => O(2^n)
*/
const zap = (n) => {
    if (n === 1) {
        return
    }
    zap(n - 2)
    zap(n - 2)
}

// The time complexity of the bar function is O(3^n)
const bar = (n) => {
    if (n === 1) {
        return
    }
    bar(n - 1)
    bar(n - 1)
    bar(n - 1)
}