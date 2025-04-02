//learning about the length property used with dot notation (i.e. .length)
//this can be useful for iteration count in loops when looping through an array
//it can be used with an array, with a string
let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; //number array
const multiple = 9 //multiple

for (let i = 0; i < numbers.length; i++) { //open loop, less than the length of the numbers array
  console.log(multiple, "x", numbers[i], "=", numbers[i] * multiple); //print the combination where multiple is 9, and numbers[i] is the current iteration in the array
}

// example output: 9 x 0 = 0
