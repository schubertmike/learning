//fizz buzz
let number = 1; //assigning initial value
let max = 15; //assigning max value

for (let i = number; i <= max; i++) {//opening the loop, initial value, max value, and iterations
  if (i % 3 === 0 && i % 5 === 0) {//looking at multiples of 3 and 5 first
    console.log("FizzBuzz"); //print fizzbuzz if multiple of 3 and 5
  } else if (i % 3 === 0) { //next looking at multiples of 3
    console.log("Fizz"); //print fizz
  } else if (i % 5 === 0) { //looking at multiples of 5
    console.log("Buzz"); //print buzz
  } else {
    console.log(i); //if neight multiple of 3 or 5, just print the iteration number
  }
}
