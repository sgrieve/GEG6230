---
title: Analyzing Catchment Data
---

Here we will learn how to work with the catchment data files provided on QMplus for assignment 1 and 2.

While a lot of powerful, general tools are built into Python,
specialized tools built up from these basic units live in
[libraries]({{ page.root }}/reference/#library)
that can be called upon when needed.

## Loading data into Python
In order to load our catchment data, we need to access
([import]({{ page.root }}/reference/#import) in Python terminology) a library called
[NumPy](http://docs.scipy.org/doc/numpy/ "NumPy Documentation") which stands for Numerical Python.
In general you should use this library if you want to do things with collections of numbers. We can import NumPy using:

~~~
import numpy
~~~
{: .language-python}

Importing a library is like getting a piece of lab equipment out of a storage locker and setting it
up on the bench. Libraries provide additional functionality to the basic Python package, much like
a new piece of equipment adds functionality to a lab space. Just like in the lab, importing too
many libraries can sometimes complicate and slow down your programs - so we only import what we
need for each program.

Once we've imported the library, we can ask the library to read our data file for us:

~~~
numpy.loadtxt(fname='data/75001/75001_temperatures_morning.csv', delimiter=',', skiprows=1)
~~~
{: .language-python}

~~~
array([[1.000e+00, 5.600e+00, 4.400e+00],
       [2.000e+00, 7.200e+00, 4.800e+00],
       [3.000e+00, 1.080e+01, 9.300e+00],
       ...,
       [1.093e+03, 1.340e+01, 8.800e+00],
       [1.094e+03, 1.290e+01, 9.600e+00],
       [1.095e+03, 7.100e+00, 3.900e+00]])
~~~
{: .output}

The expression `numpy.loadtxt(...)` is a [function call]({{ page.root }}/reference/#function-call)
that asks Python to run the [function]({{ page.root }}/reference/#function) `loadtxt` which
belongs to the `numpy` library. This [dotted notation]({{ page.root }}/reference/#dotted-notation)
is used everywhere in Python: the thing that appears before the dot contains the thing that
appears after.

As an example, John Smith is the John that belongs to the Smith family.
We could use the dot notation to write his name `smith.john`,
just as `loadtxt` is a function that belongs to the `numpy` library.

`numpy.loadtxt` has two [parameters]({{ page.root }}/reference/#parameter): the name of the file
we want to read and the [delimiter]({{ page.root }}/reference/#delimiter) that separates values on
a line. These both need to be character strings (or [strings]({{ page.root }}/reference/#string)
for short), so we put them in quotes.

Since we haven't told it to do anything else with the function's output,
the notebook displays it.
In this case,
that output is the data we just loaded.
By default,
only a few rows and columns are shown
(with `...` to omit elements when displaying big arrays).
To save space,
Python displays numbers as `1.` instead of `1.0`
when there's nothing interesting after the decimal point.

> ## Importing libraries with shortcuts
>
> In this lesson we use the `import numpy` [syntax]({{ page.root }}/reference/#syntax) to import NumPy.
> However, shortcuts such as `import numpy as np` are frequently used.  Importing NumPy this way means that after the
> inital import, rather than writing `numpy.loadtxt(...)`, you can now write `np.loadtxt(...)`. Some
> people prefer this as it is quicker to type and results in shorter lines of code - especially for libraries
> with long names! You will frequently see Python code online using a NumPy function with `np`, and it's
> because they've used this shortcut. It makes no difference which approach you choose to take, but you must be
> consistent as if you use `import numpy as np` then `numpy.loadtxt(...)` will not work, and you must use `np.loadtxt(...)`
> instead. Because of this, when working with other people it is important you agree on how libraries are imported.
{: .callout}

Our call to `numpy.loadtxt` read our file
but didn't save the data in memory.
To do that,
we need to assign the array to a variable. Just as we can assign a single value to a variable, we
can also assign an array of values to a variable using the same syntax.  Let's re-run
`numpy.loadtxt` and save the returned data:

~~~
data = numpy.loadtxt(fname='data/75001/75001_temperatures_morning.csv', delimiter=',', skiprows=1)
~~~
{: .language-python}

This statement doesn't produce any output because we've assigned the output to the variable `data`.
If we want to check that the data have been loaded,
we can print the variable's value:

~~~
print(data)
~~~
{: .language-python}

~~~
[[ 0.  0.  1. ...,  3.  0.  0.]
 [ 0.  1.  2. ...,  1.  0.  1.]
 [ 0.  1.  1. ...,  2.  1.  1.]
 ...,
 [ 0.  1.  1. ...,  1.  1.  1.]
 [ 0.  0.  0. ...,  0.  2.  0.]
 [ 0.  0.  1. ...,  1.  1.  0.]]
~~~
{: .output}

Now that the data are in memory,
we can manipulate them.
First,
let's ask what [type]({{ page.root }}/reference/#type) of thing `data` refers to:

~~~
print(type(data))
~~~
{: .language-python}

~~~
<class 'numpy.ndarray'>
~~~
{: .output}

The output tells us that `data` currently refers to
an N-dimensional array, the functionality for which is provided by the NumPy library.
These data correspond to daily minimum and maximum temperature values.
The rows are the individual days, and the columns are the temperature measurements.

> ## Data Type
>
> A Numpy array contains one or more elements
> of the same type. The `type` function will only tell you that
> a variable is a NumPy array but won't tell you the type of
> thing inside the array.
> We can find out the type
> of the data contained in the NumPy array.
>
> ~~~
> print(data.dtype)
> ~~~
> {: .language-python}
>
> ~~~
> float64
> ~~~
> {: .output}
>
> This tells us that the NumPy array's elements are
> [floating-point numbers]({{ page.root }}/reference/#floating-point number).
{: .callout}

With the following command, we can see the array's [shape]({{ page.root }}/reference/#shape):

~~~
print(data.shape)
~~~
{: .language-python}

~~~
(1095, 3)
~~~
{: .output}

The output tells us that the `data` array variable contains 1095 rows and 3 columns. When we
created the variable `data` to store our data, we didn't just create the array; we also
created information about the array, called [members]({{ page.root }}/reference/#member) or
attributes. This extra information describes `data` in the same way an adjective describes a noun.
`data.shape` is an attribute of `data` which describes the dimensions of `data`. We use the same
dotted notation for the attributes of variables that we use for the functions in libraries because they have the same part-and-whole relationship.

If we want to get a single number from the array, we must provide an
[index]({{ page.root }}/reference/#index) in square brackets after the variable name, just as we have done with lists, however, our data now has two dimensions, so
we will need to use two indices to refer to one specific value:

~~~
print('first value in data:', data[0, 0])
~~~
{: .language-python}

~~~
first value in data: 1.0
~~~
{: .output}

~~~
print('minimum temperature on day 100:', data[99, 2])
~~~
{: .language-python}

~~~
minimum temperature on day 100: -3.8
~~~
{: .output}

The expression `data[99, 2]` accesses the element at row 99, column 2. While this expression may not surprise you, `data[0, 0]` might.
Programming languages like Fortran, MATLAB and R start counting at 1
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because it represents an offset from the first value in the array (the second
value is offset by one index from the first value). This is closer to the way
that computers represent arrays (if you are interested in the historical
reasons behind counting indices from zero, you can read
[Mike Hoye's blog post](http://exple.tive.org/blarg/2013/10/22/citation-needed/)).
As a result,
if we have an M×N array in Python,
its indices go from 0 to M-1 on the first axis
and 0 to N-1 on the second.
It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.

![Zero Index](../fig/python-zero-index.png)

> ## In the Corner
>
> What may also surprise you is that when Python displays an array,
> it shows the element with index `[0, 0]` in the upper left corner
> rather than the lower left.
> This is consistent with the way mathematicians draw matrices
> but different from the Cartesian coordinates.
> The indices are (row, column) instead of (column, row) for the same reason,
> which can be confusing when plotting data.
{: .callout}

## Slicing data
An index like `[99, 2]` selects a single element of an array,
but we can select whole sections as well.
For example,
we can select the first ten days (columns) of values like this:

~~~
print(data[0:10, 1:3])
~~~
{: .language-python}

~~~
[[ 5.6  4.4]
 [ 7.2  4.8]
 [10.8  9.3]
 [10.   9.2]
 [ 9.7  9.1]
 [ 9.9  4.1]
 [ 9.5  8.9]
 [10.4  9.5]
 [ 4.1 -1. ]
 [ 2.5  0.1]]
~~~
{: .output}

The [slice]({{ page.root }}/reference/#slice) `0:10` means, "Start at index 0 and go up to, but not
including, index 10." Again, the up-to-but-not-including takes a bit of getting used to, but the
rule is that the difference between the upper and lower bounds is the number of values in the slice.

We don't have to start slices at 0:

~~~
print(data[500:510, 0:3])
~~~
{: .language-python}

~~~
[[501.   16.3   6.2]
 [502.   14.1   8.6]
 [503.   16.4  11.3]
 [504.   19.9   8.1]
 [505.   15.   10.5]
 [506.   13.2   8.3]
 [507.   10.5   3.6]
 [508.   10.    7.1]
 [509.   14.4   8.4]
 [510.   13.6   8.7]]
~~~
{: .output}

We also don't have to include the upper and lower bound on the slice.  If we don't include the lower
bound, Python uses 0 by default; if we don't include the upper, the slice runs to the end of the
axis, and if we don't include either (i.e., if we just use ':' on its own), the slice includes everything:

~~~
small = data[:10, 1:]
print('small is:')
print(small)
~~~
{: .language-python}
The above example selects rows 0 through 9 and columns 1 and 2.

~~~
small is:
[[ 5.6  4.4]
 [ 7.2  4.8]
 [10.8  9.3]
 [10.   9.2]
 [ 9.7  9.1]
 [ 9.9  4.1]
 [ 9.5  8.9]
 [10.4  9.5]
 [ 4.1 -1. ]
 [ 2.5  0.1]]
~~~
{: .output}

Arrays also know how to perform common mathematical operations on their values.  The simplest
operations with data are arithmetic: addition, subtraction, multiplication, and division.  When you
do such operations on arrays, the operation is done element-by-element.  Thus:

~~~
doubledata = data * 2.0
~~~
{: .language-python}

will create a new array `doubledata`
each element of which is twice the value of the corresponding element in `data`:

~~~
print('original:')
print(data[:5, :])
print('doubledata:')
print(doubledata[:5, :])
~~~
{: .language-python}

~~~
original:
[[ 1.   5.6  4.4]
 [ 2.   7.2  4.8]
 [ 3.  10.8  9.3]
 [ 4.  10.   9.2]
 [ 5.   9.7  9.1]]
doubledata:
[[ 2.  11.2  8.8]
 [ 4.  14.4  9.6]
 [ 6.  21.6 18.6]
 [ 8.  20.  18.4]
 [10.  19.4 18.2]]
~~~
{: .output}

If, instead of taking an array and doing arithmetic with a single value (as above), you did the
arithmetic operation with another array of the same shape, the operation will be done on
corresponding elements of the two arrays.  Thus:

~~~
tripledata = doubledata + data
~~~
{: .language-python}

will give you an array where `tripledata[0,0]` will equal `doubledata[0,0]` plus `data[0,0]`,
and so on for all other elements of the arrays.

~~~
print('tripledata:')
print(tripledata[:5, :])
~~~
{: .language-python}

~~~
tripledata:
[[ 3.  16.8 13.2]
 [ 6.  21.6 14.4]
 [ 9.  32.4 27.9]
 [12.  30.  27.6]
 [15.  29.1 27.3]]
~~~
{: .output}

In many cases, it is useful to separate the day count from the actual temperature data. The index values allow us to work out the day number directly from our dataset, so we can create a new NumPy array:


~~~
tempdata = data[:, 1:]
print(tempdata.shape)
~~~
{: .language-python}

~~~
(1095, 2)
~~~
{: .output}


Often, we want to do more than add, subtract, multiply, and divide array elements.  NumPy knows how
to do more complex operations, too.  If we want to find the average minimum and maximum temperature on
all days, for example, we can ask NumPy to compute `data`'s mean value:

~~~
print(numpy.mean(tempdata))
~~~
{: .language-python}

~~~
8.374383561643835
~~~
{: .output}

`mean` is a [function]({{ page.root }}/reference/#function) that takes
an array as an [argument]({{ page.root }}/reference/#argument).

> ## Not All Functions Have Input
>
> Generally, a function uses inputs to produce outputs.
> However, some functions produce outputs without
> needing any input. For example, checking the current time
> doesn't require any input.
>
> ~~~
> import time
> print(time.ctime())
> ~~~
> {: .language-python}
>
> ~~~
> Sat Mar 26 13:07:33 2016
> ~~~
> {: .output}
>
> For functions that don't take in any arguments,
> we still need parentheses (`()`)
> to tell Python to go and do something for us.
{: .callout}

NumPy has lots of useful functions that take an array as input.
Let's use three of those functions to get some descriptive values about the dataset.
We'll also use multiple assignment,
a convenient Python feature that will enable us to do this all in one line.

~~~
maxval, minval, stdval = numpy.max(tempdata), numpy.min(tempdata), numpy.std(tempdata)

print('maximum temperature:', maxval)
print('minimum temperature:', minval)
print('standard deviation:', stdval)
~~~
{: .language-python}

Here we've assigned the return value from `numpy.max(tempdata)` to the variable `maxval`, the value
from `numpy.min(tempdata)` to `minval`, and so on.

~~~
maximum temperature: 28.3
minimum temperature: -7.6
standard deviation: 5.434688722915133
~~~
{: .output}

> ## Mystery Functions in IPython
>
> How did we know what functions NumPy has and how to use them?
> If you are working in IPython or in a Jupyter Notebook, there is an easy way to find out.
> If you type the name of something followed by a dot, then you can use tab completion
> (e.g. type `numpy.` and then press tab)
> to see a list of all functions and attributes that you can use. After selecting one, you
> can also add a question mark (e.g. `numpy.cumprod?`), and IPython will return an
> explanation of the method! This is the same as doing `help(numpy.cumprod)`.
{: .callout}


So far, we have lumped together both our minimum and maximum temperature values when calculating those statistics. It'd make more sense to get the mean maximum and mean minimum temperature. One way to do this is to create a new temporary array of the data we want,
then ask it to do the calculation:

~~~
minimums = tempdata[:, 1] # every row, only column 1 (minimum temperature)
print('Highest minimum temperature:', numpy.max(minimums))
~~~
{: .language-python}

~~~
Highest minimum temperature: 16.9
~~~
{: .output}

Everything in a line of code following the '#' symbol is a
[comment]({{ page.root }}/reference/#comment) that is ignored by Python.
Comments allow programmers to leave explanatory notes for other
programmers or their future selves.

We don't actually need to store the row in a variable of its own.
Instead, we can combine the selection and the function call:

~~~
print('Lowest maximum temperature:', numpy.min(tempdata[:, 0]))
~~~
{: .language-python}

~~~
Lowest maximum temperature: -2.8
~~~
{: .output}

What if we need the temperature range for each day (as in the
next diagram on the left) or the average for the minimum and maximum columns (as in the
diagram on the right)? As the diagram below shows, we want to perform the
operation across an axis:

![Operations Across Axes](../fig/python-operations-across-axes.png)

To support this functionality,
most array functions allow us to specify the axis we want to work on.
If we ask for the average across axis 0 (rows in our 2D example),
we get:

~~~
print(np.mean(tempdata, axis=0))
~~~
{: .language-python}

~~~
[10.67789954  6.07086758]
~~~
{: .output}

If we average across axis 1 (columns in our 2D example), we get:

~~~
print(numpy.mean(tempdata, axis=1))
~~~
{: .language-python}

~~~
[ 5.    6.   10.05 ... 11.1  11.25  5.5 ]
~~~
{: .output}

which is the average of the max and min temperature across all days.

As a quick check, we can ask this array what its shape is:

~~~
print(numpy.mean(tempdata, axis=1).shape)
~~~
{: .language-python}

~~~
(1095,)
~~~
{: .output}

The expression `(1095,)` tells us we have an N×1 vector, which has the same number of values as we have days of data in this dataset.

A more useful thing than the average of the min and max temperatures would be to calculate the temperature range:

~~~
print(numpy.diff(tempdata, axis=1))
~~~
{: .language-python}

~~~
[[-1.2]
 [-2.4]
 [-1.5]
 ...
 [-4.6]
 [-3.3]
 [-3.2]]
~~~
{: .output}

But why are all the values negative? This is because `numpy.diff` calculates the difference between the current value and the next value in the array as data[i] - data[i + 1], in our case that is the minimum minus the maximum. We can fix this with another NumPy command, which removes negative signs from values in arrays:

~~~
print(numpy.abs(numpy.diff(tempdata, axis=1)))
~~~
{: .language-python}

~~~
[[1.2]
 [2.4]
 [1.5]
 ...
 [4.6]
 [3.3]
 [3.2]]
~~~
{: .output}

> ## Check Your Understanding
>
> ## Slicing Strings
>
> A section of an array is called a [slice]({{ page.root }}/reference/#slice).
> We can take slices of character strings as well:
>
> ~~~
> element = 'oxygen'
> print('first three characters:', element[0:3])
> print('last three characters:', element[3:6])
> ~~~
> {: .language-python}
>
> ~~~
> first three characters: oxy
> last three characters: gen
> ~~~
> {: .output}
>
> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> > ## Solution
> > ~~~
> > oxyg
> > en
> > oxygen
> > ~~~
> > {: .output}
> {: .solution}
>
> What is `element[-1]`?
> What is `element[-2]`?
>
> > ## Solution
> > ~~~
> > n
> > e
> > ~~~
> > {: .output}
> {: .solution}
>
> Given those answers,
> explain what `element[1:-1]` does.
>
> > ## Solution
> > Creates a substring from index 1 up to (not including) the final index,
> > effectively removing the first and last letters from 'oxygen'
> {: .solution}
{: .challenge}

> ## Thin Slices
>
> The expression `element[3:3]` produces an [empty string]({{ page.root }}/reference/#empty-string),
> i.e., a string that contains no characters.
> If `data` holds our array of temperature data,
> what does `data[3:3, 4:4]` produce?
> What about `data[3:3, :]`?
>
> > ## Solution
> > ~~~
> > array([], shape=(0, 0), dtype=float64)
> > array([], shape=(0, 40), dtype=float64)
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
