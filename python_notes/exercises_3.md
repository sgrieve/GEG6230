---
title: "GEG6230 Python Exercises 3"
author: Stuart Grieve
...

### Correcting our data

We discover that the file `75006_daily_flow.csv` has an error, as the flow meter was calibrated incorrectly. Every flow value needs to be multiplied by 1.23 to correct them. Load this data, and apply this correction, making sure not to change the day numbers.

### Temperature data

What is the maximum temperature recorded in the first 31 days of each of the 4 catchment evening temperature datasets?

### Thin slices

The expression `element[3:3]` produces an empty string, i.e., a string that contains no characters.

If `data` holds our array of temperature data, what does `data[3:3, 4:4]` produce?

What about `data[3:3, :]`?

### January vs January

Calculate the daily difference in precipitation between two Januarys in the `75007_rainfall.csv` dataset.

**Hint:** January has 31 days, and a year has 365 days (we're ignoring leap years for now...), so the end of the second January will be day number 365 + 31.
