---
title: Making Choices
---

Now that we can get the computer to repeat things, we need to be able to create rules for what to do in given situations. For example we may need to apply a different formula depending on the type of input data we receive.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an `if` statement:

~~~
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
~~~
{: .language-python}

~~~
not greater
done
~~~
{: .output}

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the set of lines indented underneath it) is executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](../fig/python-flowchart-conditional.png)

Conditional statements don't have to include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

~~~
num = 53
print('before conditional...')
if num > 100:
    print(num,' is greater than 100')
print('...after conditional')
~~~
{: .language-python}

~~~
before conditional...
...after conditional
~~~
{: .output}

We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.

~~~
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is negative')
~~~
{: .language-python}

~~~
-3 is negative
~~~
{: .output}

Note that to test for equality we use a double equals sign `==`
rather than a single equals sign `=` which is used to assign values.

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

~~~
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')
~~~
{: .language-python}

~~~
at least one part is false
~~~
{: .output}

while `or` is true if at least one part is true:

~~~
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
~~~
{: .language-python}

~~~
at least one test is true
~~~
{: .output}

> ## `True` and `False`
> `True` and `False` are special words in Python called `booleans`,
> which represent truth values. A statement such as `1 < 0` returns
> the value `False`, while `-1 < 0` returns the value `True`.
{: .callout}

## Checking Data For Errors

Now that we've seen how conditionals work, we can use them to check for the suspicious features in datasets.

Imagine we have some rain gauge measurements (in mm), stored in a list:

~~~
rainfall = [1.3, 3.1, 6.5, 9.9, -4.8, 6.2, 8.6, 6038.1, 2.4, 3.0]
~~~
{: .language-python}


Based on what we know about the rain gauge, it has a maximum capacity of 100 mm. Lets use a `for loop` and an `if` statement to test this:


~~~
for measurement in rainfall:
    if measurement > 100:
        print('Value too large:', measurement)
~~~
{: .language-python}

~~~
Value too large: 6038.1
~~~
{: .output}

What about negative values? We know a rain gauge cannot record a value of less than zero. Lets check for that:

~~~
for measurement in rainfall:
    if measurement < 0:
        print('Negative rainfall:', measurement)
~~~
{: .language-python}

~~~
Negative rainfall: -4.8
~~~
{: .output}

We have 2 values that don't look right. Lets make a new list containing only the data we are confident in:

~~~
good_data = []
for measurement in rainfall:
    if measurement > 100 or measurement < 0:
        pass
    else:
        good_data.append(measurement)

print(good_data)        
~~~
{: .language-python}

~~~
[1.3, 3.1, 6.5, 9.9, 6.2, 8.6, 2.4, 3.0]
~~~
{: .output}

This is a common thing that we need to do when working with data, we can't always trust data we are given!

> ## How Many Paths?
>
> Consider this code:
>
> ~~~
> if 4 > 5:
>     print('A')
> elif 4 == 5:
>     print('B')
> elif 4 < 5:
>     print('C')
> ~~~
> {: .language-python}
>
> Which of the following would be printed if you were to run this code?
> Why did you pick this answer?
>
> 1.  A
> 2.  B
> 3.  C
> 4.  B and C
>
> > ## Solution
> > C gets printed because the first two conditions, `4 > 5` and `4 == 5`, are not true,
> > but `4 < 5` is true.
> {: .solution}
{: .challenge}

> ## What Is Truth?
>
> `True` and `False` booleans are not the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
>
> ~~~
> if '':
>     print('empty string is true')
> if 'word':
>     print('word is true')
> if []:
>     print('empty list is true')
> if [1, 2, 3]:
>     print('non-empty list is true')
> if 0:
>     print('zero is true')
> if 1:
>     print('one is true')
> ~~~
> {: .language-python}
{: .challenge}

> ## That's Not Not What I Meant
>
> Sometimes it is useful to check whether some condition is not true.
> The Boolean operator `not` can do this explicitly.
> After reading and running the code below,
> write some `if` statements that use `not` to test the rule
> that you formulated in the previous challenge.
>
> ~~~
> if not '':
>     print('empty string is not true')
> if not 'word':
>     print('word is not true')
> if not not True:
>     print('not not True is true')
> ~~~
> {: .language-python}
{: .challenge}


> ## Sorting a List Into Buckets
>
> In our `data` folder, we have a series of data files:
> ~~~
> files = ['75001_temperatures_evening.csv', '75001_landcover.csv',
>         '75001_rainfall.csv', '75001_daily_flow.csv',
>         '75001_temperatures_morning.csv']
> ~~~
> {: .language-python}
>
> We would like to split this list of files into a list of temperature files, `temps` and a list of everything else `others`.

> Add code to the template below to do this. Note that the string method
> [`startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith)
> returns `True` if and only if the string it is called on starts with the string
> passed as an argument, that is:
>
> ~~~
> "String".startswith("Str")
> ~~~
> {: .language-python}
> ~~~
> True
> ~~~
> {: .output}
> But
> ~~~
> "String".startswith("str")
> ~~~
> {: .language-python}
> ~~~
> False
> ~~~
> {: .output}
>Use the following Python code as your starting point:
> ~~~
> files = ['75001_temperatures_evening.csv', '75001_landcover.csv',
>         '75001_rainfall.csv', '75001_daily_flow.csv',
>         '75001_temperatures_morning.csv']
>
> temps = []
> others = []
> ~~~
> {: .language-python}
>
> Your solution should:
>
> 1.  loop over the names of the files
> 2.  figure out which group each filename belongs
> 3.  append the filename to that list
>
> In the end the two lists should be:
>
> ~~~
> temps = ['75001_temperatures_evening.csv', '75001_temperatures_morning.csv']
> others = ['75001_landcover.csv', '75001_rainfall.csv', '75001_daily_flow.csv']
> ~~~
> {: .language-python}
>
> > ## Solution
> > ~~~
> > for file in files:
> >     if file.startswith('75001_temp'):
> >         temps.append(file)
> >     else:
> >         others.append(file)
> >
> > print('temps:', temps)
> > print('others:', othes)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Counting Vowels
>
> 1. Write a loop that counts the number of vowels in a character string.
> 2. Test it on a few individual words and full sentences.
> 3. Once you are done, compare your solution to your neighbor's.
>    Did you make the same decisions about how to handle the letter 'y'
>    (which some people think is a vowel, and some do not)?
>
> > ## Solution
> > ~~~
> > vowels = 'aeiouAEIOU'
> > sentence = 'Mary had a little lamb.'
> > count = 0
> > for char in sentence:
> >     if char in vowels:
> >         count += 1
> >
> > print("The number of vowels in this string is " + str(count))
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

{% include links.md %}
