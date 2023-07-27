/*
Write a function, unique, that takes an array and
returns a new array containing unique elements

*/


//the runtime of outerloop => n
//the runtime of the innerloop => m
//hence O(n * m) => O(n * m)

function unique(array){
    let newArray = []

    for(let i = 0; i < array.length; i++){
        if(!(newArray.includes(array[i]))){
            newArray.push(array[i])
        }
    }
    return newArray;
}

let arr = ["cat","dog","rat","dog","cat","bird"]
console.log(unique(arr))

//the runtime of outerloop => n
//the runtime of the innerloop => m
//hence O(n * m) => O(n * m)

function unique_2(arr) {
    const uniqueArr = [];
    
    for (let i = 0; i < arr.length; i++) {
        let isUnique = true;
        
        for (let j = 0; j < uniqueArr.length; j++) {
            if (arr[i] === uniqueArr[j]) {
                isUnique = false;
                break;
            }
        }
        if (isUnique) {
            uniqueArr.push(arr[i]);
        }
    }
    return uniqueArr;
}

/*
The unique_3 function has a runtime of the first loop O(n)
Adding an item to a set is O(1)
converting a set to an array = O(n)
therefore: O(n + 1 + n) => O(2n + 1) => O(n)
*/

function unique_3(array){
    const newArray = new Set()

    for(let i = 0; i < array.length; i++){
        newArray.add(array[i]) // add method adds only unique elements to set
    }
    return Array.from(newArray);
}

console.log(unique_3(arr))