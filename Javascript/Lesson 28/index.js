//looking at other array methods like indexOf and includes
const characters = [ //array
  "The Wally Watchers",
  "Wilma",
  "Fritz",
  "Wizard Whitebeard",
  "Odlaw",
  "Waldo",
  "Woof"
];

//conditional looking for waldo; if waldo is included in the array, print where in the array he's included
//from here, we could probably remove waldo, or I bet we could place him in another array or database somehow.
if(characters.includes("Waldo")) { 
  const waldoIndex = characters.indexOf("Waldo");
  console.log("Found Waldo at index", waldoIndex);
} else {
  console.log("Not Found");
}
