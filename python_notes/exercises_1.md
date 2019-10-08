---
title: "GEG6230 Python Exercises"
author: Stuart Grieve
...

# Python exercises


### Range

Python has a built-in function called `range` that generates a sequence of numbers. `range` can accept 1, 2, or 3 parameters.

- If one parameter is given, `range` generates a sequence of that length, starting at zero and incrementing by 1. For example, `range(3)` produces the numbers `0, 1, 2`.

- If two parameters are given, `range` starts at the first and ends just before the second, incrementing by one. For example, `range(2, 5)` produces `2, 3, 4`.

- If `range` is given 3 parameters, it starts at the first one, ends just before the second one, and increments by the third one. For example, `range(3, 10, 2)` produces `3, 5, 7, 9`.

Using `range`, write a loop that uses range to print the first 3 natural numbers:

```
1
2
3
```

### Reverse a String

Knowing that two strings can be joined together (concatenated) using the `+` operator, write a loop that takes a string and produces a new string with the characters in reverse order, so `'Newton'` becomes `'notweN'`.


### Turn a String Into a List
Use a for-loop to convert the string “hello” into a list of letters:

```
["h", "e", "l", "l", "o"]
```

Hint: You can create an empty list like this:

```
my_list = []
```

### Loops inside loops

Given a nested list containing lists of ingredients:

```
food = [['pepper', 'zucchini', 'onion'], ['cabbage', 'lettuce', 'garlic'], ['apple', 'pear', 'banana']]
```

Use 2 for loops to reproduce the following output:

```
pepper
zucchini
onion
---
cabbage
lettuce
garlic
---
apple
pear
banana
---
```

### Cubing numbers

As well as the usual mathematical operations we have already seen, Python has an easy way to compute powers `**`. For example we can square a value as follows: `myval ** 2`.

Create a list containing the cubes of the values 1 through 9.
