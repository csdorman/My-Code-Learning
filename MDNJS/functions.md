# Functions in JS

One of the **fundamental building blocks in JS**. 

A function is a set of statements that perform a task or calculate a value. 

To use a funciton, you must define it somewhere in the scope from which you call it.

## Defining functions

### Function declarations

A function declaration (also called a *function definition* or a *function statement*) consists of:

1. The ```function``` keyword.
2. The name of the function
3. A list of parameters to the function enclosed in paranthese (...) and comma-separated.
4. The JS statements that define the function, enclosed in curly brackets {...}.

The following code defines a simple function named ```square```.  The function takes one parameter (number). The function returns that parameter (number) multiplied by itself.
```
function square(number) {
    return number * number;
}
```

Primitive parameters (like numbers) are passed to functions by value. If the function changes the value of the parameter, this change is not reflected globally or in calling the function.

If object parameters (like an ```array```) are passed to the function and the function changes their properties, those changes are visible outside the function.

### Function expressions

In addition to the declarations, functions can also be created by a function expression. 

Such functions can be anonymous or be named. Here is the square function again as an anonymous function expression:
```
var square = function(number) { return number * number; };
```

Function expressions can also be named. And the name can be used inside the function itself:
```
var factorial = function fac(n) { return n < 2 ? 1 : n * fac(n-1); };
``` 

## Calling functions

**Defining** a function **does not execute** it. 

To execute a function, you must **call** it. Functions must be in scope when they are called, but if the are lower in the program, they can be hoisted (appear below the code in the program) if the are set in a function declaration.

## Function scope






