// learning about the Math.random() function, and how to break it out from 0 to 1
//use the math.floor function and embed the math.random function with a multiplier to break it out from 0 to 1
//for example, Math.floor(Math.random() * 10); should give us a random integer from 0 to 9

//magic 8 ball code

const question = "What's your question buddy?"; //asking the question
const answerNumber = Math.floor(Math.random() * 9) + 1; //random number for the answer

let answer = ""; //empty string for answer to fill

if (answerNumber === 1){ //could use a loop but I'm not at that point in the course yet. Insstead, we use a long if else if statement
    answer = 'Defo my dude';
} else if (answerNumber === 2){
    answer = 'mos def';
} else if (answerNumber === 3) {
    answer = 'cha bra';
} else if (answerNumber === 4) {
    answer = 'lol idk ask someone else';
} else if (answerNumber === 5) {
    answer = 'ask me again in 5 minutes';
} else if (answerNumber === 6) {
    answer = 'it a secret my dude';
} else if (answerNumber === 7) {
    answer = 'my mom said no';
} else if (answerNumber === 8) {
    answer = 'yeah not looking good';  
} else if (answerNumber === 9) {
    answer = 'nah that is not happening';
} else {
    console.log('error');
}

console.log("Question: ", question); //this part doesn't really do anything so I'd delete for now
console.log("Answer: ", answer); //outputs the answer, but appends Answer: to the beginning
 
