
# Prefix Sum & Suffix Sum - Programming Tools

## Summary

Hey guys! It is a pleasure having you back in my articles. 
Today I bring you this two tools that are widely use when trying to solve a problem in the Software Engineering industry. 
We are going to start with the [Prefix Sum](https://en.wikipedia.org/wiki/Prefix_sum), also called cumulative sum or inclusive scan.
And when we have covered that we will move on to the [Suffix Sum](https://en.wikipedia.org/wiki/Suffix_array), instead of having the sum direction from left to right, it will be from right to left.


## Prefix Sum

To calculate the prefix sum of an array we just need to grab the previous value of the prefix sum and add the current value of the traversed array. The idea behind is that in the previous position of the prefix array we will have the sum of the previous elements. This becomes really helpful because if you want to know what is the total sum up to certain point, you can just check for the value in the prefix sum array. Another use for this programming tool is when you want to know the value between two positions in the array, without the need of going through each item in the array you can just do a calculation from the values in the prefix sum array, reducing complexity and therefor saving time and money. Without any fuss or delay let me show you how can you get the prefix sum array.

Here is the implementation in Javascript:
```javascript
const prefixSum = arr => { 

    // Get the size of the array.
    const n = arr.length

    // Create an empty array of the same size as input.
    const result = new Array(n)

    // Initialize the first position of the array with the same value as the first item of the item.
    result[0] = arr[0]

    // Go through the input array, starting in the position 0, to the n.
    for (let i = 1; i < n; i++)

        // Assign the result of the previous value and the value in the current position in the input array.
        result[i] = result[i-1] + arr[i]

    return result
}

const prefixTestArray = [2, 4, 6, 8, 10, 12, 14]

console.log(prefixSum(prefixTestArray))
```


## Suffix Sum

For the Suffix Sum array, we will use a similar approach to the Prefix Sum, with the slight modification that we wil start from the end and go to the beginning of the array.

You can check out some Javascript implementation of the Suffix Sum:
```javascript
const suffixSum = arr => {
    const n = arr.length
    const result = new Array(n)
    // Instead of assigning the first position, we assign the last with the last value of the input array.
    result[n-1] = arr[n-1]

    // Go through the input array, starting in the last position, until the first.
    for( let i = n - 2; i >= 0; i-- )
        result[i] = result[i+1] + arr[i]
    return result
}

const suffixTestArray = [2, 4, 6, 8, 10, 12, 14]

console.log(suffixSum(suffixTestArray))
```

## Conclusion

I hope you would find this useful in your near future. I know that if you have a lot of experience solving programming problems you might find this trivial, but let us not forget our humble beginnings when we didn't know too much about these simple tools that can help us in time of need.
I wish you some joyful coding days ahead of you!

