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
