/*
What is combinatorics?
field of math concerned with counting things
Common Questions:
1. Given N things, in how many ways can we arrange them?
2. In how many ways can we do X?
3. Whta is the shortest way to do Y?
What is a combination?
a collection of things where the order does not matter

Given a set of n things, there are N^n possible combinations
*/

const combinations = (elements) => {
    if (elements.length === 0) {
        return [[]]
    }
    const first_element = elements[0]
    const combsWithoutFirst = combinations(elements.slice(1))
    const combsWithFirst = []
    
    combsWithoutFirst.forEach(comb => {
        const combWithFirst = [...comb, first_element];
        combsWithFirst.push(combWithFirst)
    })

    return [...combsWithoutFirst, ...combsWithFirst]
}

console.log(combinations(['a', 'b','c']))