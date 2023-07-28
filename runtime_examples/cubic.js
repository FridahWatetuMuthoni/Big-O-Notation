const foo = (array) => {
    for (let i = 0; i < array.length; i++){
        for (let j = 0; j < array.length; j++){
            for (let k = 0; k < array.length; k++){
                console.log(i, j, k)
            }
        }
    }
}

foo([1,2,3,4,5])