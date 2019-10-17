author: Jeff Yang
title: Spiral Matrix – Brain Teaser Series
category: Algorithms
published: 2019-09-21

This is going to be the first of the “Brain Teaser” series, where I will be writing posts on the so-called “whiteboard interview questions” that I thought were interesting. This first post of the series is going to be about the “Spiral Matrix” problem, where you need to write a function that accepts an integer N and returns a N\*N spiral matrix.
Problem Statement: Write a function that accepts an integer N and returns a N\*N spiral matrix.

The problem statement itself may not paint a clear picture of what we are dealing with, so let us take a look at an example:
spiralMatrix(4)
![spiralMatrix(4)](../../static/upload/spiral_matrix_1.png)<br>

Hopefully, the picture above was clear enough to give you a good idea of what our function is supposed to do. Essentially, the function `spiralMatrix(n)` needs to produce a n\*n matrix that spirals inwards. The question may seem a bit daunting at first, but we’ll go through it step by step.

<1> Notice that we are dealing with a 2D Array

This problem can be challenging to even start because it does not directly say what type of data structure we are dealing with. To begin discussing the solution to this problem, we need to be very clear on the fact that the matrix shown above is essentially a 2D array, where there are multiple arrays within an array.

<2> How will we populate the 2d array, spiraling inwards?

Take a look at the following diagram:
![spiralMatrix](../../static/upload/spiral_matrix_2.png)<br>

The general idea is to populate the 2d array by iterating through each row and column, and incrementing the respective variables as we continue with the iteration. The pseudo code would be as follows:

* `startRow = 0`, iterate through `startCol` –> `endCol`, `startRow++`
* `endCol = 3`, iterate through `startRow` –> `endRow`,  `endRol—-`
* `endRow = 3`, iterate through `endCol` –> `startCol`, `endRow--`
* `startCol = 0`, iterate through `endRow` –> `startRow`, `startCol++` <br>

For each of the bullet points above, we will need a for loop. After we are done iterating through the 4 for loops once each, we will have populated the most outer layer of the N\*N matrix we are trying to return. Now, how do we make that one extra step so that we can make sure the inner matrix is also populated?

As you may have already noticed, we will be incrementing `startRow` or `startCol` and decrementing `endRow` or `endCol` as we proceed. All we need to make sure is that we continue our iteration to populate the matrix while `startRow` <= `endRow` AND `startCol <= endCol`!

The fully working code written in JavaScript is as follows:
```javascript
function spiralMatrix(n) {
    let result = new Array(n).fill().map(() => new Array(n).fill(''));
    let startRow = 0
    let endRow = n-1
    let startCol = 0
    let endCol = n-1
    let counter = 1

    while (startRow <= endRow && startCol <= endCol) {

        for (let i = startCol; i <= endCol; i++) {
            result[startRow][i] = counter
            counter++
        }
        startRow++

        for (let i = startRow; i <= endRow; i++) { 
            result[i][endCol] = counter counter++ 
        }
        endCol-- 

        for (let i = endCol; i >= startCol; i--) {
            result[endRow][i] = counter
            counter++
        }
        endRow--

        for (let i = endRow; i >= startRow; i--) {
            result[i][startCol] = counter
            counter++
        }
        startCol++
    }
    return result
}
```