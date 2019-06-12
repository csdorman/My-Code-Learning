# Intro to Comp Sci

## Lecture 1 What is Computation

Computers know two kinds of knowledge:
- Declarative: statement of fact
- Imperative: recipe or "how-to"

A *recipe* consists of 3 things:
1. A *sequence* of simple steps
2. A *flow of control* that specifies when each step is executed
3. A way to determine *when to stop*

Creating recipes
- A programming langue provides a set of *primitive operations*
- An *expression* is a complex combination of primitive in any programming language
- Expressions and computations have *values* and *meanings* in a programming language

Aspects of programming language
### Syntax
Similar to English:
- "cat dog boy" are all three words, but this collection is not a valid sentence. "Cat hugs boy" is syntatically correct.
- ' "hi"5 ' is not syntatically valid in a programming language, but '3.2*5' is.
*Static semantics* is which syntactically valid strings have meaning:
- "I are hungry" in syntactically valid but a static semantic error in English.
- ' 3+"hi" ' is syntactically valid but a static semantic error in a Python.
*Semantics* is the meaning associated with a syntactically correct string of symbols with no static semantic errors.
- English can have different meanings: "Flying planes can be dangerous"
- Programmin languages have only one meaning but may *not* be what programmer intended.
*Where things go wrong*
- **syntatic errors**: common and easily caught
- **static semantic errors**: some languages check for these before running program. They can sometimes cause unpredictable  behavior.
- **no errors but *different meaning from what programmer intended* **: Program crashes, stops running, keeps running forever, or it gives an answer different than expected.

### Python Programs
A *program* is a sequence of definitions (evaluated) and commands (executed).
*Commands* are statements that instruct interpreter to do something. They can be typed directly into a shell or stored in a file that is read in the the shell and executed.

In Python, everything is an *object*

### Objects
- Programs manipulate *data objects*
- Objects have a *type* that defines the kind of things that programs can do to them.
- Objects are scalar (cannot be subdivided) or non-scalar (have internal structre and can be subdivided)

**Scalar objects**
- ```int```: intergers, ex. 5
- ```float```: real numbers, ex. 3.27
- ```bool```: Boolean values ```True``` and ```False```
- ```NoneType```: special ad has one value, ```none```
- can use ```type()``` to see the type of an object.

### Expressions
- Combine *objects* and *operators* to form expressions
- An expression has a *value*, which has a *type*
- Syntax for a simple expression is: ```<object> <operator> <object>```
**Operators for ```int``` and ```float```
- '+' : addition
- '-' : subtraction
- '*' : multiplication
- '/' : division
For the '+', '-', and '* ' operations, if *both* numbers are ```int``` the result is an ```int```. If either or both are ```float```, the result is ```float```. The result of '/' is *always* a float.
- '%' : remainder
- '**': exponent

### Binding Variables and Values
- The '=' is a sign of *assigning* a variable name to a value.
- This value is stored in the computer's memory, and binds the name to the value.
- You can retrieve the value associated with the variable by *invoking* the name.
- You can *re-bind* variable names using new assignment statements.

## Lecture 2 Branching and Iteration

### Strings
- Letters, special characters, spaces, and digits
- Enclose thing in *double* (" ") or *single* (' ') quotes
- You can concatenate (combine) strings:
``` 
hi = "hello there"
name = "ana"
greet = hi + name
greeting = hi + " " + name
```

### I/O  
**```print()```**
- Used to *output* to console.
- format is: ```print(stuff-to-display-goes-here)```
- You can print out strings (enclose in quotes), or variables (no quotes.)
- Concatenating with commas (,) will automatically insert space. Using a plus (+) will not add a space.
- You can use commas with strings, or number objects. All objects must be strings to use plus. (Use ```str()``` to convert numbers to strings.)

**```input("")```**
- Prints the string enclosed in quotes, and creates a text input for the user
- Once the user types in something and hits enter, that input is bound to a variable:
```text = input("Type anything...")
print(5*text)
```
- ```input``` returns a string, so if you want to do math operations, you must convert it into a number using ```int()``` or ```float()```:
``` num = int(input("Type a number..."))
print(5*num)
```

**comparison operators** on ```int```, ```float```, ```string```
- Comparisons below evaluate to a Boolean type:
- i > j
- i >= j
- i < j
- i <= j
- i == j
- i != j
- Cannot compare a ```string``` to ```int``` or ```float`` types.

**logic operators** on Boolean values
- ```not a``` : True if ```a``` is False. False if ```a``` is True
- ```a``` and ```b``` : True if *both* ```a``` and ```b``` are True
-```a``` or ```b```: True if either or both are true

### Branching
- Let programs make "decisions"
- The ```<condition>``` has a value of ```True``` or ```False```
- The indented code block is run only if the ```<condition> is ```True```

**```if```**
```
if <condition>
    <expresssion>
```

**```if - else```**
```
if <condition>
    <expression>
else:
    <expression>
```

**```else - if ```**
```
if <condition>
    <expression>
elif <condition>
    <expression>
else: 
    <expression>
```

**Indentation matters in Python**
- Indendtation is how you denote blocks of code

**```while``` Loops**
```
while <condition>:
    <expresssion>
```
- ```<condition>``` evalutates to Boolean
- If ```True```, the steps inside the code block are run
- The ```<condition>``` steps are checked again
- This pattern is repeated until ```<condition>``` is ```False```

**Iterating numbers with ```while``` and ```for``` loops**
- More complicated with a ```while``` loop:
```
n = 0
while n < 5:
    print(n)
    n = n+1
```
- ```for``` loop is much shorter:
```
for n in range(5):
    print(n)
```
**```for``` loop**
```
for <variable> in range(<some_num>):
    <expression>
```
The ```range()``` parameter can take extra arguments
- ```range(start, stop, step)```
- Default value for ```start```= 0 and ```step```= 1
- ```range``` loops until it reaches ```stop``` - 1

**```break``` statement**
- Immediately exists whatever loop it is in
- Skips remaining expressions in the code block
- Only exits the *innermost* loop (not all loops)

##Lecture 3: String Manipulation, Guess & Check, Approximations, Bisection

