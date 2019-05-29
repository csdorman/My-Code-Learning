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