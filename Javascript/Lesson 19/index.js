//while loop condition is either true or false
//if true, the loop runs. The loop ends when the condition is false
//similar to if statement, but the logic keeps running while the condition is true
//example below

const luckyNumber = 7;
let guess = Math.floor(Math.random() * 10) + 1;

while (guess != 7) {//if guess isn't 7, run the loop
  console.log("Nope, it isn't", guess);//print that it isn't the number from the let variable
  guess = Math.floor(Math.random() * 10) + 1;//set the variable again, or it will just print the let variable infinitely
}

console.log("My lucky number is 7!"); //if it hits 7, stop the loop and print this console log

