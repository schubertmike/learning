// rock paper scissors program with random number generator for the computer opponent
// rock = 0, paper = 1, scissors = 2
let player = 0
let computer = Math.floor(Math.random() * 2) + 1

//assigning the player their position, depending on the number that corresponds with said position
if (player === 0) {
  player = "Rock";
} else if (player === 1) {
  player = "Paper";
} else if (player === 2) {
  player = "Scissors";
} else {
  console.log("error");
}

//doing the same thing for the computer
if (computer === 0) {
  computer = "Rock";
} else if (computer === 1) {
  computer = "Paper";
} else if (computer === 2) {
  computer = "Scissors";
} else {
  console.log("error");
}

console.log("Player Picked: ", player);
console.log ("Computer Picked: ", computer);
// rock = 0, paper = 1, scissors = 2
if (computer === "Rock" && player === "Paper") {
  console.log("The player wins!"); //if c = rock and p = paper, p wins
} else if (computer === "Rock" && player === "Scissors") {
  console.log("The computer wins!"); //if c is rock and p is scissors, c wins
} else if (computer === "Paper" && player === "Rock") {
  console.log("The computer wins!"); //if c is paper and p is rock, c wins
} else if (computer === "Paper" && player === "Scissors") {
  console.log("The player wins!"); //if c is paper and p is scissors, p wins
} else if (computer === "Scissors" && player === "Rock") {
  console.log("The player wins!"); //if c is scissors and p is rock, p wins
} else if (computer === "Scissors" && player === "Paper") {
  console.log("The computer wins!"); //if c is scissors and p is paper, c wins
} else {
  console.log("It's a tie! play again"); //otherwise it's a tie since the last 3 combinations are all if they are equal
} 
