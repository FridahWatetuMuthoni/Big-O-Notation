const foo = (array) => {
    for (let i = 0; i < array.length; i++){
        for (let j = 0; j < array.length; j++){
            console.log(array[i] + "/" + array[j])
        }
    }
}

foo([1, 2, 3, 4, 5])

/*
The bar function has a time complexity of n^2
because the number of recursive calls which is the depth of the recursive calls is n
and the width of it, which basically means the dorminat term in each recursive call is n
because the slice() method has a time complexity of n
therefore depth * width = n * n = O(n^2)
*/
let bar = (str) => {
    if (str.length === 0) {
        return
    }
    const first_char = str[0]
    const rest = str.slice(1)
    console.log(first_char)
    bar(rest);
}

bar("coderbyte")