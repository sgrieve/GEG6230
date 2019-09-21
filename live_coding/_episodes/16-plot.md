---
title: Plotting Graphs
---

The mathematician Richard Hamming once said, "The purpose of computing is insight, not numbers," and
the best way to develop insight is often to visualize data. While
there is no official plotting library, `matplotlib` is the _de facto_ standard.  First, we will
import the `pyplot` module from `matplotlib` and give it the shorthand name `plt`:

~~~
import matplotlib.pyplot as plt

~~~
{: .language-python}

Before we start learning the specifics of matplotlib, we will plot our first graph!

~~~
plt.plot(data[:, 0], data[:, 1])
plt.savefig('temperatures.png')
~~~
{: .language-python}

![Max temp over time](../fig/temperatures.png)

This is cool, but it'd be better if we could see our graphs alongside our code...

> ## Some IPython Magic
>
> You'll need to execute the following command
> in order for your matplotlib images to appear
> in the notebook when `show()` is called:
>
> ~~~
> %matplotlib inline
> ~~~
> {: .language-python}
>
> The `%` indicates an IPython magic function -
> a function that is only valid within the notebook environment.
> Note that you only have to execute this function once per notebook.
{: .callout}

Let's try again, this time using `plt.show()`:

~~~
plt.plot(data[:, 0], data[:, 1])
plt.show()
~~~
{: .language-python}

![Max temp over time](../fig/temperatures.png)

Right now this graph is pretty bad, so we are going to improve it. Firstly, lets explore changing how our line looks:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
~~~
{: .language-python}

There are lots of different default colours you can choose, which can be found in the documentation [here](https://matplotlib.org/3.1.0/gallery/color/named_colors.html). Similarly, you can change the style of the line, using the information [here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle):

We can add more lines to a figure by calling `plt.plot()` as second time, with different options.

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
~~~
{: .language-python}

But which line is which? This is why we used labels, so now we can add a legend:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
~~~
{: .language-python}

We now know which line is which, but not what the values mean, lets add some labels to the axes:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
~~~
{: .language-python}

We can add a title to our plot:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001')
~~~
{: .language-python}


What if we wanted to zoom in on a particular range of days? For example, we wanted to plot the first 100 days of the dataset. There are 2 ways to do this:

~~~
plt.plot(data[:100, 0], data[:100, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:100, 0], data[:100, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001')
~~~
{: .language-python}

or, we can use matplotlib to only draw part of the graph:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001')
plt.xlim(0, 100)
plt.ylim(-7, 12)
~~~
{: .language-python}

We can also adjust the font size of any text elements using the `fotnsize` parameter:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001', fontsize=20)
plt.xlim(0, 100)
plt.ylim(-7, 12)
~~~
{: .language-python}

Now that we have finished making our first graph, we can think about saving it to use in a presentation, report or piece of coursework. We can set the file format by using the correct file extension, some options are `pdf`, `png` and `svg`:

~~~
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001', fontsize=20)
plt.xlim(0, 100)
plt.ylim(-7, 12)
plt.savefig('75001_temps_morning.png')
~~~
{: .language-python}

The image is a bit small though... lets tell matplotlib to make it bigger for us:

~~~
plt.figure(figsize=(12, 8))
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001', fontsize=20)
plt.xlim(0, 100)
plt.ylim(-7, 12)
plt.savefig('75001_temps_morning.png')
~~~
{: .language-python}

Sometimes, the graphs we are making have a lot of white space around the edges. We can tidy this up automatically by using `plt.tight_layout()`:

~~~
plt.figure(figsize=(12, 8))
plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Catchment 75001', fontsize=20)
plt.xlim(0, 100)
plt.ylim(-7, 12)
plt.tight_layout()
plt.savefig('75001_temps_morning.png')
~~~
{: .language-python}

## Saving time

Now that we have made a reasonable looking graph for one catchment, how can we make similar graphs for the others without lots of effort?

A tool python has to help us with this is called glob:

~~~
import glob
~~~
{: .language-python}

The `glob` library contains a function, also called `glob`,
that finds files and directories whose names match a pattern.
We provide those patterns as strings:
the character `*` matches zero or more characters,
while `?` matches any one character.
We can use this to get the names of all the data files we wish to plot:

~~~
print(glob.glob('data/*/*_temperatures_morning.csv'))
~~~
{: .language-python}

~~~
['data/75007/75007_temperatures_morning.csv', 'data/75006/75006_temperatures_morning.csv', 'data/75001/75001_temperatures_morning.csv', 'data/75004/75004_temperatures_morning.csv']
~~~
{: .output}

As these examples show,
`glob.glob`'s result is a list of file and directory paths in arbitrary order.
This means we can loop over it
to do something with each filename in turn.
In our case,
the "something" we want to do is generate a set of plots for each file.

~~~

filenames = glob.glob('data/*/*_temperatures_morning.csv')

for filename in filenames:

  data = numpy.loadtxt(fname=filename, delimiter=',', skiprows=1)

  plt.figure(figsize=(12, 8))
  plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
  plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
  plt.legend()
  plt.xlabel('Days')
  plt.ylabel('Temperature in Degrees Celsius')
  plt.title(filename, fontsize=14)
  plt.xlim(0, 100)
  plt.ylim(-7, 12)
  plt.tight_layout()

~~~
{: .language-python}

We need to be able to give each plot a unique name, so we can use the catchment ID stored in the filename:

~~~
filenames = glob.glob('data/*/*_temperatures_morning.csv')

for filename in filenames:

    catchment_id = filename.split('/')[2].split('_')[0]

    data = numpy.loadtxt(fname=filename, delimiter=',', skiprows=1)

    plt.figure(figsize=(12, 8))
    plt.plot(data[:, 0], data[:, 1], linestyle='--', color='orange', linewidth=1, label='Maximum Temperatures')
    plt.plot(data[:, 0], data[:, 2], linestyle='-', color='b', linewidth=1, label='Minimum Temperatures')
    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('Temperateure in Degrees Celsius')
    plt.title(filename, fontsize=14)
    plt.xlim(0, 100)
    plt.ylim(-7, 12)
    plt.tight_layout()
    plt.title('Catchment {}'.format(catchment_id))
    plt.savefig('{}_morning_temps.png'.format(catchment_id))
  ~~~
  {: .language-python}


## Grouping plots

You can group similar plots in a single figure using subplots.
This script below uses a number of new commands. The function `matplotlib.pyplot.figure()`
creates a space into which we will place all of our plots. The parameter `figsize`
tells Python how big to make this space. Each subplot is placed into the figure using
its `add_subplot` [method]({{ page.root }}/reference/#method). The `add_subplot` method takes 3
parameters. The first denotes how many total rows of subplots there are, the second parameter
refers to the total number of subplot columns, and the final parameter denotes which subplot
your variable is referencing (left-to-right, top-to-bottom). Each subplot is stored in a
different variable (`axes1`, `axes2`, `axes3`). Once a subplot is created, the axes can
be titled using the `set_xlabel()` command (or `set_ylabel()`).
Here are our three plots side by side:

~~~

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 2, 1)
axes2 = fig.add_subplot(1, 2, 2)

axes1.set_ylabel('Temperature (C)')
axes1.plot(data[:, 0], data[:, 1])
axes1.set_title('Maximum Temperature')

axes2.set_ylabel('Temperature (C)')
axes2.plot(data[:, 0], data[:, 2])
axes2.set_title('Minimum Temperature')

plt.tight_layout()
plt.suptitle('Max and Min Temps')

~~~
{: .language-python}

## Scatter plots



## Bar plots



## Histograms



## Boxplots

~~~

plt.boxplot(data[:, 1:], meanline=True, showmeans=True, labels=['Max', 'min'])

~~~
{: .language-python}

## Violin plots

~~~

plt.violinplot(data[:, 1:], showextrema=False, showmedians=True)

ax = plt.gca()
labels = ax.get_xticklabels()
labels[2] = 'Max'
labels[7] = 'Min'
ax.set_xticklabels(labels)

~~~
{: .language-python}

## Finishing touches
