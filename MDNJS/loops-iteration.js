
//********** for loop 
//loop iterates until a = 5

for(a = 0; a < 5; a++) {
    console.log(a);
}
console.log("Variable a is now " + a);

//Since the console.log IN the loop happens after the a < 5 check, this loop only logs 0-4 before the loop terminates. 

//********** do loop
//loop iterates until b = 5

var b = 0
do {
    b++;
    console.log(b);
} while (b < 5);
console.log("Variable b is now " + b);

// Since the statement (b++ and console.log) is executed before the condition (b < 5) is checked, this one doesn't print out 0, and does print out 5 inside the loop. The final console.log also prints out 5.

//********* while loop
// loop iterates until c = 5

var c = 0
while ( c < 5){
    c++;
    console.log(c);
}
console.log("Variable c is now " + c);

//Prints out similar to the do...while loop