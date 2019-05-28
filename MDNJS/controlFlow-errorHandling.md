
## Block statements

The most basic statement

The block is delimited by a pair of curly braces { }

``` 
{
    statement;
    statement;
    statement;
}

```

Block statements commonly used with *control flow statements* (if, for, while):
``` 
while (x < 10) {
    x++;
}
```

Remember that **prior to ECMAScript 2015** JS does NOT have block scope. Variables introduced in a block are scoped to the containing function or script, and effects of them persist beyond the block itself.

For example: 
```
var x = 1;
{
    var x =2;
}
console.log(x)
```
This outputs 2, since both ```var x``` statements are the same in scope.

Starting in ECMAScript 2015, ```let``` and ```const``` variable declarations are block scoped.

## Conditional Statements

Two different types of conditionals are used in JS, ``` if...else ``` and ``` switch```.

### ```if...else``` statements

The ```if``` statement executes if a logical condition is TRUE.

The (optional) ```else``` statement executes if the condition is false:

```
if (condition) {
    statement-1;
} else {
    statement-2;
}
```

The initial ```condition``` can be anything that evaluates to either ```true``` or ```false```. 

```statement-1``` and ```statement-2``` can be any kind of statement, including nested ```if``` statements. 

You can else use ```else if``` to compound the number of statements and have mulitple conditions tested in sequence:

```
if(condition-1) {
    statement-1;
} else if (condition-2) {
    statement-2;
} else if (condition-3) {
    statement-3;
} else if (condition-n) {
    statement-n;
} else {
    statement-final;
}
```

In this case, ONLY THE FIRST logical condition which evaluates to TRUE will be executed. To execute multiple statments, group them WITHIN A BLOCK statement ({...}) as follows:

```
if(condition) {
    statement-1-if-true;
    statement-2-if-true
} else {
    statement-1-if-false;
    statement-2-if-false;
}
```

As a rule, don't use simple assignments in the conditional expression, since this can be confusing when looking over the code. If it is necessary to do this, enclos the statement in double parenthesis:

NO:
```
if (x=y) {
    statement-here;
}
```

SLIGHTLY BETTER (but still not great):
```
if ((x=y)) {
    statement-here;
}
```

Falsey values

These values all evaluate to false (or falsey)
- false
- undefined
- null
- 0
- NaN
- an empty string ("")

All other values (including objects) evaluate to true when passed to a conditional statement.

Do not confuse primitive boolean values (```true``` and ```false```) with the true and false values of the ```Boolean``` object!

### Switch statement

This statement attempts to match an expression's value to a case label. If a match is found, the statement of the matched case label is executed:

```
switch (expression) {
    case label-1:
        statement-1
        [break;]
    case label-2;
        statement-2
        [break;]
        ...
    default:
        statement-default
        [break;]
}
```

If there is no ```case``` label that matches the initial ```expression```, the (optional) ```default``` clase is executed.

The (optional) ```break```` statement after each ```case``` clause makes sure the that program breaks out once the ```case``` statement has been executed. If it is omitted, the program continues executing the next statement in the ```switch``` statement.

EXAMPLE:

```
switch(fruitType) {
    case 'Oranges':
        console.log('Oranges are $0.59 a pound.');
        break;
    case 'Apples':
        console.log('Apples are $0.32 a pound.');
        break;
    case 'Bananas':
        console.log('Bananas are $0.48 a pound.');
        break;
    case 'Cherries':
        console.log('Cherries are $3.00 a pound.');
        break;
    case 'Mangoes'
        console.log('Mangoes are $0.56 a pound.');
        break;
    case 'Papayas':
        console.log('Papayas are $2.79 a pound.');
        break;
    default:
        console.log('Sorry, we are out of " + fruitType + '.');
}
console.log("Is there anything else you'd like?")
```