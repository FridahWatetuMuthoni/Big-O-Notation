const bar = (n)=>{
    for(let i = 0; i < 3; i++){ //O(1)
        for(let j = 0; j < n; j++){ //O(n)
            console.log(j) //O(1)
        }
    }

    for(let k = 0; k < 10000; k++){ //O(1)
        console.log(k) // O(n)
    }
}

//runtime = O(3n + 10000) => O(n)