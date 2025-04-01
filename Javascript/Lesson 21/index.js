//looping from 1 to 50 using for loop, incorporating continue and break into the loop
for (i = 0; i <= 50; i++) { //initial value of i = 0, iterating up to 50, increments of 1
  if (i % 2 == 1)  { //conditional checking for odd number, using modulo where remainder is 1
    continue; //if odd number, continue
  } if (i === 42) { //if i is equal to 42, do the following
    console.log(i); //log i (in this case, log 42)
    break; //stop the loop
  }
  console.log(i); //log each number in the loop
}
