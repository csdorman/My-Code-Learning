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
for <variable> in range(<some_num_or_var>):
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

### Strings
- A sequence of case-sensitive characaters
- You can compare strings to other strings with >, <, ==
- ```len()``` is a function used to retrieve the length of the string in the parenthesis.
- Square brackets ([...]) are used to perform indexing into a string to get the value at a certain position (or index)
```
s = "abc"
s[0] = a
s[2] = c
s[3] = Index out of bounds - error
s[-1] = c
s[-3] = a
```
- You can **slice** strings using ```[start:stop:step]```
- With two numbers, ```[start:stop], step = 1``` by default
```
s = "abcdefgh"
s[3:6] = "def"
s[3:6:2] = "df"
s[::] = "abcdefgh"
s[::-1] = "hgfedbca"
s[4:1:-2] = "ec"
```
- strings are *immutable* (not able to be modified)

```
s = "hello"
s[0] = "y"  -> gives an error
s = "y" + s[1:len(s)] -> this is allowed
```

### Strings and Loops
- These two code snippets do the *same thing*
- The lower one is more "pythonic" (more easily understandable)
```
s = "abcdefgh"

for index in range(len(s)):
    if s[index] == "i" or s [index] == "u":
        print("There is an i or u")

for char in s:
    if char == "i" or char == "u":
        print("There is an i or u")
```
### Algorithms
- Finding the cube root with the *guess-and-check* method
``` 
cube = 8
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube <0:
        guess = -guess
    print("Cube root of " +str(cube)+ " is "+str(guess))
```
- Finding the cube root with the *approximate solution* method
- Start with a guess and increment by a *small* value.
- Keep guessing if ```guess**3 - cube >= epsilon``` for a small epsilon. Epsilon value = close enough to the correct answer
```
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3) - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print ("num_guesses =", num_guesses)
if abs(guess**3 - cube) >=epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
```
- Finding the cube root with *bisection search* method
- Half interval each iteration - new guess is halfway in between
```
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print("Number of guesses = " + num_guesses)
```
- Search space: 1st guess (N/2), 2nd guess (N/4), kth guess (N/2**k)
- Guess converges on the order of log2 N steps
- Bisection search works when the value of a function varies monotonically with input
- Above code only works for positive cubes > 1

 ## Lecture 4 Decomposition, Abstraction, and Functions

 **Abstraction**
 - You don't need to know *how* something works in order to know how to work it.
 In programming:
 - A piece of code is similar to a black box:
    - Cannot see details
    - Do not want/need to see details
- Abstraction is achieved with *function specifications* or *docstrings* (input, output, what it does)

 **Decomposition**
 - Different devices work together to achieve an end goal
 In programming:
- Divide code into modules that are:
    - Self-contained
    - Used to break up code
    - Intended to be reuseable
    - Help keep code organized and coherent.
- You can achieve this with *functions* and *classes*

### Functions
- Reusable chunks of code
- Functionare are not run until they are *called* or *invoked*
- Characteristics: Name, parameters (0 or more), docstring (recommended), body, returns something.
```
def is_even( i ):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("inside is_even")
    return i%2 == 0

is_even(3)
```


**Variable Scope**
- A **formal parameter** gets bound to the value of an **actual parameter** when the a function is called.
- A new scope/frame/environment is created when you enter a function
- **scope** is mapping of names to objects.
- Inside a function, you *can access* a variable defined outside, but you *cannot modify* a variable defined outside.
- You can modify global variables, but it is not recommended.

For Scope questions, check out pythontutor.com

If there is *not* a return statement at the end of a function, Python will return the value ```none``` - a special type that represents the absence of a value.

Arguments in functions can take on any type, *including other functions*
```
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()
print func_a()
print 5 + func_b(2)
print func_c(func_a)
```

## Lecture 5 Tuples, Lists, Aliasing, Mutability, & Cloning

**Tuples** - sequence of *some type of data*. It can contain *elements* that are data types (```string```, ```int```, ```float```). You can mix element types in a single tuple

Tuples are immutable (like strings). Tuples are represented by parenthesis ().

Tuples can be used to swap variables:
```(x, y) = (y, x)```
Instead of (without tuples):
```
temp = x
x = y
y = temp
```

Used to ```return``` multiple values from a single function. 
Elements in a tuple can be tuples themselves.
You can iterate over tuples.

**Lists** are similar to tuples. They can contain elements of any type.

Denoted with [].
Unlike tuples, **lists are mutable**.

When iterating through list, it's more pythonic to iterate through list elements directly. This means that:
```
L = [some list of things]
for i in L:
    total += 1
print (total)
```
is MORE Pythonic (and more readable) than:
```
for i in range(len(L)):
    total += :[i]
print (total)
```
**List Operations**
- You can *add* elements with ```L-name.append(element)```. This mutates the list - same list but with additional element.
- You can *combine* lists with the ```+``` operator. This creates a new list with the combined elemnts of both.
- You can *extend* a list with ```L-name.extend(some-list)```. This mutates the list.
- You can *delete specific elements* from a list with ```del(L-name[index])```. This mutates the list.
- You can *remove elements at the end of a list* with ```L-name.pop()```. This returns the removed elements. This mutates the list.
- You can *remove a specific element* with ```L-name.remove(element)```. If the element occurs multiple times, this only removes the first instance. If element is not in list, it gives an error. This mutates the list.
- You can *convert a string to list* with ```list(s)```. Returns a list with every character from ```s``` as an element in ```L-name```.
- You can *split a string on a character* with ```s.split()```. Will split on spaces if no parameter given.
- You can turn a *list of characters into a string* with ```''join(L-name)```. Give character in quotes to add between every element.
- Two ways to sort lists: ```sort``` and ```sorted```. ```L-name.sort()``` will mutate the list. ```sorted(L-name)``` will *not*.
- Many other ways to change lists found in python docs.

**Lists are mutable**. Since you can refer to the same list with different variables (aliases), you can also ```clone``` a list. 
- **Cloning** a list creates a new list under a different variable, but *will not* copy alterations made to the original list. You can copy by ```list = cloned_list[:]```
- To **sort** a list, you can call ```sort()```. This mutates the list, but *returns nothing*. Or you can call ```sorted()``` which does *not* mutate the list, but you must assign the result to a variable to use it.
- When *iterating over a list* (with a ```for``` loop, for example), **do not** modify the list directly in the loop. Python uses an internal counter to keep track of current element index in loop, and when length of list changes the counter *does not update*. This can skip elements.

START Reading through PS 3 details and maybe start initial coding.

## Lecture 6

### Recursion
**Recursion is the process of repeating ideas in a self-similar way**

- *Algorithmically*: a way to design solutions to problems by divide-and-conquer (or decrease-and-conquer). *Reduce a problem to a simpler version of the same problem*
- *Semantically*: a programming technique where a function calls itself. Must have 1 (or more) base cases that are easy to solve, and must solve the smae problem on some other input, with the goal of simplifying the larger problem input.

**Mathematical Induction** 

# Lesson 7: Testing, Debugging, Exceptions and Assertions

**3 types of testing**
- Unit testing:
- - Validate each piece of a program
- - Testing each function separately

- Regression testing:
- - Add tests for bugs as you find them
- - Catch reintroduced errors that were previously fixed

- Integration testing:
- - Does the overall program work?
- - We tend to rush to this too soon

## Testing approaches
- **Intuition** about natural boundries or partitions to the problem. *Works especially for numbers*.  
- **Random testing** works for some problems, although you need more random tests to ensure the program is working correctly.
- **Black box testing** assumes you have the specs for the code, and you derive tests from those doc specs. You *don't* need to see the actual code to derive tests.
- **Glass box testing** uses the code itself, and tries to find possible test cases looking at that. This kind of testing is called *path-complete* when it covers every potential path through the code. 
- **Glass box guidelines**:
- - *Branches*: must exercises all parts of a conditional
- - *For loops*: must cover: loop not entered, body of loop executed exactly 1 time, body of loop exercises more than 1 time.
- - *While loops*: must cover similar to for loops. Catch all ways to exit loop.

## Debugging Approaches
- **Study** program code
- - Don't ask *what* is wrong
- - Ask *how* did I get the unexpected result

- **Scientific method**
- - Study available data
- - Form hypothesis
- - Repeatable experiments
- - Pick simplest input to test with

## Handling Exceptions
- You can use a ```try``` block to catch potential ```exception``` errors (especially in user input).
```
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except:
    print("Bug in user input")
```
- You can raise your own exceptions if user supplies bad data input

## Assertions
- Stop errors from propogating throughout program
Use assertions to
- Check types of arguments or values
- Check that invariants on data structure are met
- Check constraints on return values
- Check for violations of constraints on procedure (no duplicates in a list).

# Lecture 8 - Oject Oriented Programming
- Python supports many different kinds of data. (interger, string, floats, lists, dictionaries, functions).
- **Everything in python is an *object***, and every object has 
    - A type
    - An *internal data representation* (primitive or composite)
    - A set of procedures for *interaction*
- With any object you can
    - *Create* new objects of some type
    - *Manipulate* objects
    - *Destroy* objects (using ``del`` or just forget about them)

## What are Objects?
- Objects are *data abstraction* that captures:
    - An *internal representation* through data attributes
    - An *interface* for interacting with objects (either through methods (procedures/functions) or through definig behaviors).

### Advantages of OOP
- *Bundle data into packages* with procedures that work on them with logical interfaces.
- *Divide and conquer* development allows testing and implemntation of classes separately. This increased modularity and reduces complexity.
- Classes make *reusing code* much easier.
    - Each class has a *separate environment* (no function name collision)

## Creating and Using Your Own Classes
- There is a distinction between *creating* a class and *using* an instance of a class.
- *Creating a class* involves:
    - Defining the class name
    - Defining the class attributes
- *Using a class* involves:
    - Creating new instances of objects
    - Doing operations on those instances

### Define Your Own Types

Use the *class* keyword to define a new type:

```
class Coordinate(object):
    # define attributes here
```
- Similar to ```def```, indent code to indicate which statements are part of the *class definition*.
- The word ```object``` means that ```Coordinate``` is a Python object and *inherits all its attributes. ```Object``` is the *most basic type* in Python.
    - ``Coordinate`` is a *subclass* of ``object``
    - ``object`` is a *superclass* of ``Coordinate``

*Attributes*
- These are data and procedures that belong to the class.
*Data Attributes*
- Think of data as other objects that make up the class
*Methods (Procedural Attributes)*
- Think of methods as functions that *only work with this class*
- This is *how to interact* with the object

### How to create an instance of a class
- You first have to define *how to create an instance of object*
- Use a special method called ```__init__``` to initialize some data attributes
```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```
The ```self``` parameter in () refers to an instance of the class.
First parameter after the __init__ is *always* (by convention) named self.  
*Creating the first example*
```
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x) #prints out "3" (x value for c)
print(origin.x) #prints out "0" (x value for origin)
```
- Data attributes of an instance are called *instance variables*
- *Don't provide argument for ``self``*,Python does the automatically.

### Adding Methods to a Class
- Methods are procedural attributes - functions that work only with this class
- The "." operator is used to access any attribute (data or method attribute)
**Defining a Method**
```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other)
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
```
Other than the ``self`` parameter and dot notation, methods behave just like functions.

Resume Lecture 8 at 22:20

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-8-object-oriented-programming/

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
