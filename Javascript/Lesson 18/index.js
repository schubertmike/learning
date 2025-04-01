// introduction to the while loop

let randomNumber = Math.floor(Math.random() * 10); //random number generator from 0 to 10

while (randomNumber != 7) { //if number does not equal 7, run the loop
  console.log("Duck 🦆"); //print duck
  randomNumber = Math.floor(Math.random() * 10); //then generate random number from 0 to 10 again
}

console.log("Goose! 🦢"); //if the random number is equal to 7, then print goose
