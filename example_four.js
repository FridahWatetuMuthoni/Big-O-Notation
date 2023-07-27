const doubler = (items)=>{
    let newArray = [];

    for(let i = 0; i < items.length; i++){
        newArray.push(items[i])
        newArray.push(items[i])
    }

    return newArray;
}

doubler(['a', 'b', 'c']) // ['a', 'a', 'b', 'b', 'c', 'c']

/*
Calculating the space complexity of the doubler function
The new array grows by 2n => O(2n) => O(n)
*/