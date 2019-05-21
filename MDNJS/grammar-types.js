//May 21
//Didn't realize the three different variable names.
// var - declare a variable
// let - block-scoped local variable
// const - block scoped, *read-only* named constant

//Value of a is undefined
var a;
console.log('The value of a is ' + a); 

//Variable hoisting
console.log('The value of b is' + b); 
var b;

//c not defined - uncaught reference error
//console.log('The value of c is ' + c); 

// The reserved word "undefined" can be used to find out if a variable has a value
var input;
if (input === undefined) {
    console.log('There is no value stored in the input variable');
} else {
    console.log('The value of the input variable is currently ' + input);
}

//"undefined" behaves as false when in boolean (true or false) context
var myArray = [];
if (!myArray[0]) {
    console.log("Boolean is false!");
} else {
    console.log("This will not run");
}

//"undefined" converts to NaN (not a number) when used in numeric context
//"null" converts to a 0 (zero) in numeric contexts and false in boolean
var d;
var e = null;
console.log(d * 32);
console.log(e * 32);

//**VARIABLE SCOPE */