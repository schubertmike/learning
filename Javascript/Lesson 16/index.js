// learning logical operators && for and (returns true if both conditions are met)
// || for or (returns true if at least 1 condition is met)
// and ! for not (returns true is the condition is false, and false if the condition is true)

let aqi = 12 //set aqi


//program is checking for aqi. Between certain numbers it outputs a different message
if (aqi >= 0 && aqi <= 50) {
    console.log("ooo that's some good air... crispy");
} else if (aqi >= 51 && aqi <= 100) {
    console.log("it's fine I guess");
} else if (aqi >= 101 && aqi <= 150) {
    console.log("yikes, getting up there");
} else if (aqi >= 151 && aqi <= 200) {
    console.log("oh yeah, uhhhh maybe don't go outside");
} else if (aqi >= 201 && aqi <= 300) {
    console.log("Sure, go outside... if you want to die young");
} else {
    console.log("Yeah, uhhhh, just wear a respirator at all times");
}
