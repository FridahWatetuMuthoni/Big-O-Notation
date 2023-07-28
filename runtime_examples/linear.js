/*
O(n) is when the amount of time taken is equal to n
*/

let foo = (n) => {
    for (let i = 0; i < n.length; i++){
        console.log(n[i])
    }
}

let bar = (n) => {
    if (n === 0) {
        console.log(n)
    }
    bar(n - 1)
}


/*
The time complexity of the boom function is:
O(max(m, n)), where m, n are the string lengths
OR
O(n), where n is the length of the longer string
*/

const boom = (str1, str2) => {
    if (str1.length > str2.length) {
        for (let i = 0; i < str1.length; i++){
            console.log(str1[i])
        }
    }
    else {
        for (let j = 0; j < str2.length; j++){
            console.log(str2[j])
        }
    }
}

boom("swim", "run")