//loops exercise
//I need to practice my loops more
const myNumber = 850;
let binary = "";

for (let i = myNumber; i >= 1; i = Math.floor(i / 2)) { //before, I was using myNumber, that messed things up a bit. Use let i and make it equal to myNumber
  if (i % 2 == 0) { //checking if i / 2 gives a remainder of 0 if so, do the following
    binary = "0" + binary; //assign binary stsring of 0 and add it before binary
  } else {
    binary = "1" + binary; //otherwise assign binary string of 1 and add it before binary
  }
}
console.log(binary); //print binary
