const foo = (n)=>{
    for(let a = 0; a < n/2; a++){
        console.log(a)
    }

    for(let b = 0; b < n; b++){
        for(let c = 0; c < n; c++){
            console.log(b + "," + c)
        }
    }
}

/*
for(let a = 0; a < n/2; a++){
        console.log(a)
}
let a = 0 => 1
a < n/2 => n/2
a++ => n/2 + 1
total = 1 + n/2 + n/2 + 1 => 2 + n => n


for(let b = 0; b < n; b++){
    for(let c = 0; c < n; c++){
        console.log(b + "," + c)
    }
}
let b = 0 => 1
b < n => n
b++ = n + 1
total = 1+n+n+1 => 2 + 2n => n

let c = 0 => 1
c < n => n
c++ => n + 1
total = 1+n+n+1 => 2n + 2 => n

both loops => n*n => n^2

runtime => O(n + n^2) => O(n^2)
*/