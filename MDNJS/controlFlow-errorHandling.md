
##Block statements

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
