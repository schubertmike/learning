// familiarization with exponents and javascript math in general
/* the task asks for bmi calculation based on meters squared, since I don't know my height in meters, 
I need to convert it from inches. Plus I need to convert my weight from LBS to KG */
let currentWeightLBs = 240.9; //current weight with let variable
let currentWeightKG = currentWeightLBs / 2.205; //formula to convert lb to kg
const currentHeightInches = 72; // height in inches
const currentHeightMeters = currentHeightInches * 0.0254; //formula to convert height in inches to height in meters

console.log(currentHeightMeters); //print height in meters

let bmi = currentWeightKG / currentHeightMeters ** 2;

console.log(bmi); //prints approximate BMI based on the above data
