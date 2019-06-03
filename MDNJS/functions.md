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

Variables *defined in a function* cannot be accessed from anywhere outside the function, since the variable is defined only in the scope of the function.

However, a function can access *all variables and functions* defined inside the scope in which it is defined.

A functioned defined in the global scope can access all variables defined in the global scope. A function defined inside another function can access all variables defined in its parent function **and** any other variable to which its parent function has access.  

## Scope and the function stack

### Recursion

A function can refer to and call itself. This is called recursion.

There are three ways for a function to refer to itself:
1. The function's name
2. ```arguments.callee```
3. An in-scope variable that refers to the function

In this example:

```
var foo = function bar(){
    //statement goes here
};
```

These are all three equivalent:
1. ```bar()```
2. ```arguments.callee```
3. ```foo()```

Recursive functions are similar to a loop. Both execute the same code multiple times, and both require a condition to avoid an infinite loop. 

Here is a loop:
```
/Loop example
var x = 0;
while (x < 10) { //loop condition "x < 10"
    //do stuff
    x++;
}
```
**Same thing as a recursive function**
```
function loop(x) {
    if (x >= 10) //exit condition x >= 10
        return;
    //do stuff
    loop(x + 1); //recursive call
}
loop(0);
```

### Nested functions

You can nest a function within a function. The inner (nested) function is private to the outer (containing) function. This forms a *closure*. A closure is an expression (usually a function) that can have free variables together with an environment that binds (or closes) the expression.

Nested functions inherit the arguments and variables of the containing function: The inner function contains the scope of the outer function.

The inner function can only be accessed from statements in the outer function.



