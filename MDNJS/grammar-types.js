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

//May 22
//**VARIABLE SCOPE */

//Variables declared outside a function are *global*. Within function are *local*

//Scope of x below is global, so variable is available to console.log
if (true) {
    var x = 5;
}
console.log(x);

//Using let declaration makes the y variable local to the block statement ( statement within {} ) and produces error when console.log y
if (true) {
    let y = 5;
}
//console.log(y);

//**VARIABLE HOISTING*/
//Variables declared later can be "lifted" to the top of the function or statement. However, hoisted variables return value of "undefined" - even if you declare variable value after you use or refer to it.
//The let (const) declaration DOES NOT HOIST
//Place variables in function as close to the top as possible

console.log(f === undefined); //true
var f = 3;
//This is the same as
var g;
console.log(g === undefined); //true
g = 3;

var myvar = 'my value';
(function(){
    console.log(myvar); //undefined
    var myvar = 'local value';
}());
//This is the same as
var myvar2 = 'my value';
(function() {
    var myvar;
    console.log(myvar2); //undefined
    myvar2 = 'local value';
});

//FUNCTION HOISTING
//Funcion declaration gets hoisted. Function expressions DO NOT

//Declaration
foo (); 
function foo() {
    console.log('bar');
}

//Expression
//baz (); //TypeError -> Not a function
var baz = function() {
    console.log('bar2');
}

//GLOBAL VARIABLES
//In web pages, global object is window. So global variables can be accessed with window.variable

//CONSTANTS 
//These are read-only, named constants. ID syntax is same as for variables.
//Constants CANNOT change value through assignment or be re-declared. They are only initialized to a value.
//Scope rules are same as for "let" block-scope variables.
//Constants CANNOT have same name as function or variable within the same scope
//Contents of const array or objects assigned are not protected. The following statements are fine:
const MY_OBJECT =  {'key': 'value'};
MY_OBJECT.key = 'otherValue';
console.log(MY_OBJECT);
//AND
const MY_ARRAY = ['HTML', 'CSS'];
MY_ARRAY.push('JAVASCRIPT');
console.log(MY_ARRAY);

//DATA STRUCTURES AND TYPES//
// 8 Data types

//7 Primitives
// 1. Boolean - true & false
// 2. null - special keyword devoting a null value
// 3. undefined -  a top-level property whose value is not defined
// 4. Number - an integer or floating point number
// 5. BigInt - an integer with arbitrary precision
// 6. String - a sequence of characters that represent a text value
// 7. Symbol - a data type whose instances are unique and immutable

// 8. Object - named containers for values, functions, and procedures

//DATA TYPE CONVERSION

//Variables are converted from numbers to strings automatically
//The + operator will convert numbers to strings 
h = 'The answer is ' + 42
console.log(h);

//Other operators do NOT get this conversion
console.log('Subtraction:');
console.log('37' - 7);
console.log('Addition:');
console.log('37' + 7);

//CONVERT STRINGS TO NUMBERS

//parseInt() returns only whoe numbers
//parseFloat() will return decimals.

//Also possible to use the + symbol to retrieve number from string
console.log('String:');
console.log('1.1' + '1.1');
console.log('Number:');
console.log(+'1.1' + +'1.1');

//LITERALS

//Literals represent values in JS. 
//These represent fixed values, not variables, that you *literally* provide in your code.

//ARRAY LITERALS

//Array literal is zero or more expressions (array elements), enclosed in square brackets []. 
//When initialized, it's length is set to the number of arguments/elements specified.

//Array literals are also array objects

//You may leave comma-separated spaced for additional elements:
var fish = ['Lion,', , 'Angel', 'Sharknado'];

//Trailing commas, however, are ignored. This list only has 3 elements (not 4):
var myvar3 = ['home', ,'school', ];
//Leading commas are NOT ignored. This list has 4 elements:
var myvar4 = [, 'home', ,'school', ];

//Best practice to explicitly declare missing elements as *undefined* to increase clarity

//BOOLEAN LITERALS

// Two values - true and false

//NUMERIC LITERALS

//Several different types of integers.
//Base 10 (typical numbers), hexadecimal (base 16), octal (base 8), and binary (base 2)

//FLOATING-POINT LITERALS

//Syntax is:
// [(+|-)] [digits].[digits] [E|e] [(+|-)] digits]
//"E" or "e" is an exponent

//Examples:
// 3.1415926
// -.12345678
// -3.1E+12
// .1e-23

//OBJECT LITERALS

//A list of zero or more pairs of property names and associated values enclosed in curly braces {}. Do not use object literal at beginning of a statement, since the opening brace will be misinterpreted as the beginning of a block.

var sales = 'Toyota';

function carTypes(name) {
    if (name === 'Honda') {
        return name;
    } else {
        return "Sorry, we don't sell " + name + ".";
    }
}

var car = { myCar: 'Saturn', getCar: carTypes('Honda'), special: sales };

console.log(car.myCar);
console.log(car.getCar);
console.log(car.special);