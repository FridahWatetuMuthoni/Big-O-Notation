const boom =(n)=>{
    for(let i = 0; i < 3; i++){
        bam(n)
    }

    for(let k = 0; k < 10000; k++){
        console.log(k)
    }
}

const bam = (m)=>{
    for(let j = 0; j < m; j++){
        console.log(j)
    }
}

/*
The first for loop => 3 * n => 3n
The second for loop => 10000
runtime => O(3n + 10000) => O(n)
 */