//learning about other elements
//.unshift adds one or more elements to the beginning of the array
//.push adds one or more to the end of the array
//.shift removes and returns the first element in an array, and shifts the remaining elements back by 1
//.pop removes and returns the last element in the array

//examples below

const musicPlaylist = [ //establishing the array
  "Tom Sawyer",
  "Sabotage",
  "I Wanna Dance With Somebody",
  "Don't Speak",
  "Bulls On Parade",
  "Thriller",
  "The Breaks",
  "Brick",
  "Aeroplane Over the Sea",
  "Tubthumping"
];

const shiftedPlaylist = musicPlaylist.shift(); //removing the first element
const poppedPlaylist = musicPlaylist.pop(); //removing the last element
const pushedPlaylist = musicPlaylist.push("Mirroring"); //adding to the end of the array
const unshiftedPlaylist1 = musicPlaylist.unshift("Versace on the floor","MUTT"); //adding to the beginning of the array


console.log(musicPlaylist);

//my personal additions
console.log(musicPlaylist.length); //prints the length of the array (remember it starts at 0)
console.log(musicPlaylist[6]); //prints the 6th element in the array, in this case Thriller
