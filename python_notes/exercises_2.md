---
title: "GEG6230 Python Exercises 2"
author: Stuart Grieve
...

### Missing values

Write a loop that prints only even numbers between 0 and 20.

**Hint:** You use use `%` to calculate the modulus (remainder) of a division as follows:

```
print(10%3)
print(10%2)
```
will output:
```
1
0
```

### Counting Vowels

Write a loop that counts the number of vowels in a character string.
Test it on a few individual words and full sentences.

### Checking temperatures

We need to make sure that our maximum temperature values are bigger than our minimum temperature values.

```
max_temps = [10, 15, 13, 18, 8, 19, 16]
min_temps = [6, 3, 8, 11, 14, 16, 15]
```

Write a loop that compares each pair of values and warns us if the minimum is greater than the maximum.
