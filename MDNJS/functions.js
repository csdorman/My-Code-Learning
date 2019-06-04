//Function Scratchpad

//These variables are in the global scope
var num1 = 20,
    num2 = 3,
    name = "John";

//This function is in the global scope
function multiply(){
    console.log(num1 * num2);
}

multiply(); //Returns 60

//This is a global function and nested variables and a nested function
function getScore() {
    //Nested variables
    var num1 = 2,
        num2 = 3;

    //Nested function
    function add() {
        console.log(name + ' scored ' + (num1 + num2));
    }

    return add();
}

getScore();

//Loop example
var x = 0;
while (x < 10) { //loop condition "x < 10"
    //do stuff
    x++;
}

//Same thing as a recursive function

function loop(x) {
    if (x >= 10) //exit condition x >= 10
        return;
    //do stuff
    loop(x + 1); //recursive call
}
loop(0);

//Nested functions

function addSquares(a, b) {
    function square(x) {
        //console.log(x);
        return x * x;

    }
    var squareSum = square(a) + square(b);
    console.log(squareSum);
}

a = addSquares(2, 3);
b = addSquares(4, 5);

