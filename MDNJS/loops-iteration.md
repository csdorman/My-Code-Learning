# Loops and Iteration

Loops are a quick and easy way to do something repeatedly.

There are many different loops, but they all repeat an action x number of times (even zero). The different loop types offer different ways to determine the start and end points, and certain situations are more easily served by one loop over another.

## ```for``` statement
A ```for``` loop **repeates until a specified condition evaluates to FALSE**.

```
for ([initialExpression]; [condition];
[incrementExpression])
    statement
```

The ```for``` loop executes as follows:
1. The initializing expression (```initialExpression```), if any, is executed. This is *usually* a loop counter, but it can be any expression. It can also declare variables.
2. The ```condition``` expression is evaluated. If it is **true**, the ```statement``` executes. If **false** the ```for``` loop terminates. If the ```condition``` expression is omitted, it is *assumed to be true*.
3. The ```statement``` executes. To execute multiple statements, use a block {...} to group them.
4. The ```incrementExpression``` (if present) is executed.
5. Control returns to step 2

The following example counts the number of selected options in a scrolling list (<select> element). The ```for``` statement declares variable ```i``` and sets it to zero. It checks that ```i``` is less than the number of <select> options, performs the ```if``` statement, and increments ```i``` by one after each pass.
```
<form name="seletForm">
    <p>
        <label for="musicTypes">Choose some music types</lable>
        <select id="musicTypes" name="musicTypes" multiple="multiple">
            <option selected="selected">R&B</option>
            <option>Jazz</option>
            <option>Blues</option>
            <option>New Age</option>
            <option>Classical</option>
            <option>Opera</option>
        </select>
    </p>
    <p><input id="btn" type="button" value="How many are selected?"></p>
</form>
<script>
function howMany(selectObject) {
     var numberSelected = 0;
     for (var i = 0; i < selectObject.options.length; i++) {
        if(selectObject.options[i].selected) {
            numberSelected++;
        }
     }
     return numberSelected;
}

var btn = document.getElementById('btn');
btn.addEventListener('click', function() {
    alert('Number of options selected: ' + howMany(document.selectForm.musicTypes));
});
</script>
```

## ```do...while``` statement

Similar to a ```for``` loop, the ```do...while``` statement repeats **until a specificied condition evaluates to false**. 

```
do
    statement
while (condition);
```

The ```statement``` is **always executed once** before the condition is checked (and again until the ```while (condition)``` returns false). 

To **execute multiple statements**, use a block statement {...} to group them.

If ```condition``` is true, the ```statement``` executes again. At the **end** of every execution, the ```condition``` is checked. When it is false, the execution stops and control passes to the statement following ```do...while```.

In this example, the ```do...while``` loop iterates at least once and reiterates until *i* is no longer less than 5:

```
var i = 0;
do {
    i += 1;
    console.log(i);
} while (i < 5);
```

## ```while``` statement

A ```while``` statement **executes its statements as long as a specified condition evaluates to true**. 

```
while(condition)
    statement
```

If the ```condition``` becomes false, the ```statement``` stops executing and control passes to the statement following the loop.

The ```condition``` test happens **before ```statement``` in the loop is executed**.  

This ```while``` loop iterates as long as *n* is less than 3:
```
var n = 0;
var x = 0;
while (n < 3) {
    n++;
    x += n;
}
```

## ```labeled``` statement

A ```label``` gives a statement an identifier that lets you refer to it elsewhere in the program. This lets you use ```break``` or ```continue``` statements to control whether the program should stop or continue the execution of the loop.

```
label : 
    statement
```

The ```label``` can be any JS identifier that is not a reserved word. The ```statement`` can be any statement.

### ```break``` statement

The ```break``` statement terminates a loop, ```switch```, or is used with a ```labeled``` statement. 

- Using ```break``` *without a label* terminates the *innermost enclosing* ```while```, ```do...while```, ```for```, or ```switch``` immediately and transfers control to the following statement.
- When you use ```break``` *with a label* it terminates the labeled statement.

```
break [label];
```

### ```continue``` statement

The ```continue``` statement can be used to restart a ```while```, ```do..while```, ```for```, or ```label``` statement.

- When you use ```continue``` *without a label* it terminates the innermost enclosing ```while```, ```do..while```, or ```for``` statement and continues loop execution with the next iteration. **Unlike** the ```break``` statement, ```continue``` does not terminate the loop execution entirely.
    - In a ```while``` loop, ```continue``` jumps back to the condition. In a ```for``` loop it jumps to the ```increment-expression```.
- When you use ```continue``` *with a label* it applies to the looping statement identified with that label.

```
contine [label];
```


