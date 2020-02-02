const testArray = [2,4,6,8,10,12,14]
// [2, 6, 12, 20, 30, 42, 56]
console.log('Javascript Prefix Sum')

const prefixOldSchool = (arr) => {
    const n = arr.length
    const result = new Array(n)
    result[0] = arr[0]
    for (let i = 1; i < n; i++)
        result[i] = result[i-1] + arr[i]
    return result
}
const prefixNewSchool = (arr) => arr.reduce(
    (prev, curr, ind) => 
        [...prev, curr + (prev[ind-1]||0)],
    []
)

console.log(prefixOldSchool(testArray))
console.log(prefixNewSchool(testArray))