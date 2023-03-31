---
title: Getting Data from the Web
---

We are now going to explore how we can use a python library called `requests` to make HTTP GET requests to remote web servers, and then play with the data we get back in return.

## Requests

Dealing with HTTP requests can be tricky, but like with many other tricky things, there is a nice python package we can use to make our lives easier

~~~
import requests
~~~
{: .language-python}

As we learned in the lecture, there are a number of HTTP verbs we could use. But in 99% of cases we will want to use GET, as we are requesting data from a remote server, rather than trying to store any data remotely.

~~~
requests.get('https://www.bbc.co.uk/news')
~~~
{: .language-python}

This should give us the response code 200:

~~~
<Response [200]>
~~~
{: .output}

Meaning that the get request was successful.

Lets store the result of our GET request in a variable so we can have a closer look:

~~~
bbc = requests.get('https://www.bbc.co.uk/news')
~~~
{: .language-python}

In python, we can use the command `dir()` to get a listing of all the methods and attributes of a python object. When using a new library this is a good way to find our way around

~~~
dir(bbc)
~~~
{: .language-python}

There are a lot of different entries here, but we can ignore anything that starts with a double underscore, referred to as a **dunder** in the python world, as these are default methods that all python objects have.

Some of these attributes are useful for checking our request worked correctly:

~~~
print(bbc.url, bbc.status_code, bbc.request)
~~~
{: .language-python}

~~~
if bbc.status_code == 200:
  print('It worked! Lets do something cool now!')
else:
  print('We got an error, which is status code:', bbc.status_code)
~~~
{: .language-python}

So we know that our request worked, but what did we actually get?

~~~
print(bbc.text)
~~~
{: .language-python}

That's the whole of the BBC News front page! Our web browsers know how to format all of this into the webpage you are used to seeing, but here we have all of the raw information.

Its not very easy for us to process like this, but we could do something silly like this to find an image from the page:

~~~
print(bbc.text.split('jpg')[5][-200:] + 'jpg')
~~~
{: .language-python}

But if we actually want to get useful data from the web, we need to make use of APIs that are designed to give us data.

The simplest APIs return some information without needing any parameters passed to them. These are good for learning but are rarely useful in the real world.

~~~
advice = requests.get('https://api.adviceslip.com/advice')
print(advice.text)
~~~
{: .language-python}

Does the format of this output look a little familiar? This is in JSON format, which works very similarly to a python dictionary!

~~~
advice_dict = advice.json()
print(advice_dict)
print(advice_dict['slip']['advice'])
~~~
{: .language-python}


What else can this API do? Lets check it's documentation: https://api.adviceslip.com

~~~

for i in range(1, 5):
    advice = requests.get('https://api.adviceslip.com/advice/{}'.format(i))
    advice_dict = advice.json()
    print(advice_dict['slip']['advice'])

~~~
{: .language-python}

Remember in the lecture that we talked about etiquette, and not abusing these services? HTTP requests are designed so that you can supply information about why you are making a request, which helps administrators to understand who is using their service.

~~~

myheader = {
           'User-Agent': 'QMUL Geography GEG6230',
           'From': 's.grieve@qmul.ac.uk',
           'Accept': 'application/json'
          }

joke = requests.get('https://icanhazdadjoke.com', headers=myheader)
print(joke.json()['joke'])

~~~
{: .language-python}

There are a few different ways we can construct API call urls, lets explore these by searching the joke database for some keywords:

~~~

jokes = requests.get('https://icanhazdadjoke.com/search?term={}'.format('tree'), headers=myheader)
jokes = jokes.json()

for j in jokes['results']:
    print(j['joke'])
    print('---')

~~~
{: .language-python}


~~~
jokes = requests.get('https://icanhazdadjoke.com/search?term={}'.format('bar'), headers=myheader)
jokes = jokes.json()

for j in jokes['results']:
    print(j['joke'])
    print('---')
~~~
{: .language-python}

Ok, that is too many jokes! Lets just grab the first 5:

~~~
jokes = requests.get('https://icanhazdadjoke.com/search?term={}&limit={}'.format('bar', 5), headers=myheader)
jokes = jokes.json()

for j in jokes['results']:
    print(j['joke'])
    print('---')
~~~
{: .language-python}

This is beginning to get a little messy now we are adding multiple parameters. We can make things a bit tidier by storing our URL in a variable:

~~~
url = 'https://icanhazdadjoke.com/search?term={}&limit={}'.format('bar', 5)
jokes = requests.get(url, headers=myheader)
~~~
{: .language-python}

Even with all this, it can still be quite messy to build these URLs manually. This is where the `params` argument of the `get` method comes in handy:

~~~

url = 'https://icanhazdadjoke.com/search'

myparams = {'term': 'computer', 'limit': '10'}

jokes = requests.get(url, headers=myheader, params=myparams)
print(jokes.url)

~~~
{: .language-python}

This automatically builds the url in the correct format so we don't have to worry about getting symbols in the wrong place.

## More complex data and APIs

Lets now explore the UK carbon intensity data, which is reported in grams of CO2 per kWh of power generated. A value close to 0 means near 100% renewable energy generation, and high values for the UK are in excess of 300.

~~~
url = 'https://api.carbonintensity.org.uk/intensity/{}/{}'.format('2021-08-20T12:00Z', '2021-08-30T12:00Z')
intensity = requests.get(url, headers=myheader)


intensity = intensity.json()

intensity_data = []

for values in intensity['data']:
    intensity_data.append(values['intensity']['actual'])


plt.plot(range(len(intensity_data)), intensity_data)

~~~
{: .language-python}

We can also access data about the proportion of the UK's energy that comes from different sources. Lets plot up wind generation for 10 days in August 2021:

~~~
url = 'https://api.carbonintensity.org.uk/generation/{}/{}'.format('2021-08-20T12:00Z', '2021-08-30T12:00Z')
genmix = requests.get(url, headers=myheader)

wind = []
genmix = genmix.json()

for values in genmix['data']:
    for fuel_type in values['generationmix']:
        if fuel_type['fuel'] == 'wind':
            wind.append(fuel_type['perc'])


plt.plot(range(len(wind)), wind)
~~~
{: .language-python}

And we can combine the 2 datasets to see how wind generation may correlate with carbon intensity.

~~~

plt.subplot(211)
plt.plot(range(len(intensity_data)), intensity_data, color='r', label='Intensity')
plt.legend()
plt.subplot(212)
plt.plot(range(len(wind)), wind, color='k', label='Wind')
plt.legend()

~~~
{: .language-python}

A common task we may want to perform is resolving addresses based on sometimes incomplete geographic information. This is often called **geocoding** or **reverse geocoding**.

We can use services such as https://postcodes.io/docs who use Ordinance Survey data to convert between different kinds of geographic information.

~~~

url = 'https://api.postcodes.io/postcodes'
myparams = {'lat': 51.5234, 'lon': -0.0405}

postcode = requests.get(url, headers=myheader, params=myparams)

p_json = postcode.json()
for p in p_json['result']:
    print(p['postcode'])

~~~
{: .language-python}

This gives us the postcode for the Queen's Building here at QMUL. We can also use this API to convert from a postcode to a latitude/longitude or Easting/Northing pair.

~~~
url = 'https://api.postcodes.io/postcodes/{}'.format('E1 4NS')

location = requests.get(url, headers=myheader)

loc_json = location.json()

print(loc_json['result']['latitude'], loc_json['result']['longitude'])
~~~
{: .language-python}

But if we want to do this with more than 1 postcode or location at a time, we need to explore a different HTTP verb: `POST`. Thanks to requests, using this verb is very similar to everything we have done so far:

~~~
url = 'https://api.postcodes.io/postcodes'

postcodes = {'postcodes': ['SW1P 3PA', 'SW1A 0AA', 'SE1 7PB']}

bulk = requests.post(url, data=postcodes, headers=myheader)
print(bulk.url)
~~~
{: .language-python}

The difference is that instead of adding the parameters to the URL, which gets messy when we have lots of them to send, using `POST` submits our JSON data alongside the HTTP request. This is commonly how we can access bulk data from an API, rather than making lots of individual requests.

Lets join together the results from this API call with another API to find out which of these three locations has the highest elevation.

We can do this using the OpenElevation API https://open-elevation.com/ First, we will pull the data out of the JSON we got back from our POST request:

~~~
bulk = bulk.json()
locs_dict = {}

for data in bulk['result']:

    postcode = data['result']['postcode']
    long = data['result']['longitude']
    lat = data['result']['latitude']
    locs_dict[postcode] = {'lat':lat, 'long':long}

~~~
{: .language-python}

Now lets use the Open Elevation API:

~~~
for key, value in locs_dict.items():
    print(key)
    url = 'https://api.open-elevation.com/api/v1/lookup?locations={},{}'.format(value['lat'], value['long'])
    elevation = requests.get(url, headers=myheader)
    elevation = elevation.json()
    locs_dict[key]['elevation'] = elevation['results'][0]['elevation']
~~~
{: .language-python}

We are beginning to see the power of chaining lots of APIs together! We didn't have to download DEMs or lists of postcodes and their locations, to quickly go from some postcodes to the data about them we wanted.

The UK Environment Agency has the majority of its data available via APIs. In many cases this is the only way to access their data. The structure of these APIs is in some ways complex, but they all follow the same patterns and rules, so with a bit of practice we can pull data out efficiently.

For a list of all of the data available, visit https://environment.data.gov.uk/apiportal

We will be getting some hydrology data, lets start by using the API to search for the nearest river gauge to a lat/long location:

~~~
url = 'https://environment.data.gov.uk/hydrology/id/stations?'

params = {'lat':54.566040, 'long':-3.0640310, 'dist':3.0}

station = requests.get(url, headers=myheader, params=params)

print(station.url)
print(station.json())
~~~
{: .language-python}

The data is all output in a JSON file, as we have come to expect, but, the EA also formats the data for the web, so lets copy that url and paste it into our browser. This will let us see the details for this measurement station - does it look familiar? Its in one of the catchments we used in the first assessment!

If we want to get the data for this gauge, we need to grab the unique station measurement id, which is stored as a URL. Lets go back to our JSON and store this id as a variable:

~~~
station = station.json()
measure_id = station['items'][1]['measures'][0]['@id']
~~~
{: .language-python}

We can then use this measurement ID to request a csv file of all of the data since a specified date:

~~~
date = '2023-01-01'
url = '{}/readings.csv?mineq-date={}'.format(measure_id, date)

ea_data = requests.get(url, headers=myheader)
print(ea_data.text)
~~~
{: .language-python}

This is lots of data! But csv data is tricky to work with in python when it is just a block of text. So lets save it to a file:

~~~
with open('ea_data.csv', 'w') as w:
    w.write(ea_data.text)
~~~
{: .language-python}

We can now open this csv file using excel and have a look at all our data! Or, we could load the csv file back into python so we can plot the data. Unlike the csv files we have used so far in class, this one has a mix of strings and floats, so we can't just load it using numpy. Lets use the `csv` library here instead:

~~~
import csv

dates = []
values = []

with open('ea_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader)
    for row in csvreader:
        if row[3] != 'value' and row[3] != '':
            dates.append(row[2])
            values.append(float(row[3]))
~~~
{: .language-python}

And we can use matplotlib to plot a line graph of our data, making use of the **ticker** component of matplotlib to properly format our date labels:

~~~
import matplotlib.ticker as ticker

plt.plot(dates, values)

ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(4))
~~~
{: .language-python}


## Saving Data to Files

In the above examples we have already seen how to read and write mixed csv data to and from files. But often we want to save JSON data, which may be the result of an API call, so that we can analyse the data later without calling the API again. In the real world we often pay per API call, so saving data can save a lot of money!

Saving a file uses the `json.dump` command, alongside the context manager we have seen before:

~~~
import json

with open('elevation_data.json', 'w') as w:
    json.dump(locs_dict, w, sort_keys=True, indent=4)
~~~
{: .language-python}

And loading data from a JSON file back into a python dictionary uses the `json.load` command:

~~~
with open('elevation_data.json') as elevation_json:
    elevation = json.load(elevation_json)

print(elevation)
~~~
{: .language-python}
