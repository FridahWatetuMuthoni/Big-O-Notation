/*
LOGARITHMIC- O(log n):
logarithimic runtime is when the number of steps cans be expressed as a logarithim on 
the input size
a log is the opposite of an exponent
an exponent is repeated multiplication and a log is repeated division
*/

const fun = (n) => {
    while (n > 1) {
        console.log(n)
        n = n / 2
    }
    console.log("done")
}

fun(16)
//16
//8
//4
//2
//log 16 = 4

const foo = (n) => {
    if (n <= 1) {
        console.log("Hurray!");
        return
    }
    console.log(n)
    return foo(n/2)
}

foo(30)