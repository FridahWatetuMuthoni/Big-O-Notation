/*
The time complexity of the foo function is constant because
the loop will always run 5 times no matter the size of n
*/

function foo(n){
    const result = 0;

    for(let i = 0; i < 5; i++){
        result += n;
    }

    return result
}


/*
Getting a specific value from an array has a time complexity of O(1)
Getting the length of an array is also O(1)
Hence the time complexity of the foo() function is O(1)
*/
function bar(array){
    return array[0] * array[array.length - 1]
}