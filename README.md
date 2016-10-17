# Exercise 7: Plotting in Python

### Due dates
 
 - 100 % of point total if you return your solution within 1 week (due date 31.10.2016)
 - 85 % of point total if your return your solution within 2 weeks (due date 7.11.2016)
   - Detailed hints provided
 - 50 % of point total if you return your solution within 3 weeks (due date 14.11.2016)
   - Full solution provided

## Problem 0: Feedback for the first half of the courses
Having completed the first half of our courses, we would again ask your to complete [this feedback form](https://elomake.helsinki.fi/lomakkeet/73950/lomake.html) to help us to continue developing and improving the courses.

## Problem 1: Simple scatter plot using random

The aim of this task is to create a simple scatter plot using random numbers and save an image of that plot into your personal 
GitHub repository for this exercise. Write your codes into a `test_plot.py` -script and save it to your personal repository. 
The end result should look something like this:
 
 ![Example figure](img/problem1_example.png)
 
### Steps:
 - create 1000 random points using numpy's `np.random.rand()` -function that is useful for creating these kind of test plots.
    - create separate numpy arrays for x and y numbers that you will use for plotting the points
 - create a numpy array of 1000 random colors (which is basically an array full of random numbers) so that we get a little bit of sweeter looking plot as a result.
 - create a scatter plot of points (point-size=50) with random colors using `plt.scatter()` -function.
   - you can modify the size of a point using parameter `s` 
   - you can set the colors for the points using parameter `c`
 - add a title and x and y -labels to your plot as shown in the figure above. 
 - save your plot as a .png file into your repository

## Problem 2: Plotting temperature data and reusing code
For this exercise we'll be using the data and results from Exercises 5 and 6 to make plots of the seasonal average temperatures with and without the "bad" data values, and calculating the long-term average changes in temperature for the data.
We know that Exercises 5 and 6 were quite challenging, so we have opted to provide a [starter script](plot-seasonal-temps.py) for this week's exercise.
The main changes to be made are indicated with `FIX #` in the script, where `#` is the number of the change to make.
The starter script is incomplete, but will provide the structure for the different parts of the exercise, as well as introducing the new functions used for this week's exercise.

Your modified [starter script](plot-seasonal-temps.py) should:

1. Load in your summer and winter seasonal average temperature data files both with and without the "bad" data.
2. Convert the temperature values from Fahrenheit to Celsius using a function you've created.
3. Calculate a linear regression line for the data (one for each data file - 4 total).
4. Create 2 plots:
  - Plot one should be the seasonal average temperatures for winter and summer with and without the "bad" data.
  - Plot two should be the seasonal average temperatures without the "bad" data and including 2 linear regression lines, one for each season.
    - This plot should also have the slope value displayed as text on the plot.
  - All plots should include a title, axis labels, and legend.
5. Export the second plot to plotly.
  - For the exported plot, make 3 changes to the style of the plot in plotly and save them in plotly.

### Optional task(s) for Problem 2
- **Add the daily temperature data to your plots**
  - Note that in order to do this you will need to handle the date values in a nice way that will convert them into some fractional value of the year.
  There are several ways in which you might be able to do this.
  For example, if the date in the data file is `19260101` (the first day of January 1926), the value used for plotting the date could be `1926` + `1/365` = `1926.00274`
  In this way, if you plot your seasonal average temperatures by year, the daily data could be plotted as well.
  Note that for your seasonal averages, you may want to shift the years by +0.5 for the summer seasonal averages.
- **Calculate seasonal average temperatures for other locations**
  - If you'd like to see how the seasonal temperatures have changed in other areas, you're welcome to visit the [US National Oceanographic and Atmospheric Administration (NOAA) climate database](https://www.ncdc.noaa.gov/cdo-web/) and download your own data files.
    - The climate data site is currently undergoing maintenance, so instructions on how to download your own climate data will be added to the [hints for this week's exercise](https://github.com/Python-for-geo-people/Lesson-7-Plotting/blob/master/Lesson/hints.md).
    - It may be interesting to download data for one of the following regions: San Diego, California; Albuquerque, New Mexico; Houston, Texas; Nome, Alaska; Honolulu, Hawaii

### Questions for Problem 2
1. **Add a copy of plot #1 to the [Answers section of this document](#answers) with a caption describing what is plotted**.
Can you see any difference in the seasonal temperature values you plotted in plot 1?
Is the difference in the plotted values consistent?
For instance, does one dataset consistently plot above or below the other?
What could be the cause of this difference in the plotted values?
2. Do you see any clear signs of the "bad" data in plot 1?
What might make it difficult to detect "bad" data in this case?
3. Is there anything surprising about the temperature data plotted in plot 1?
If so, what was surprising to you?
4. **Add a copy of plot #2 to the [Answers section of this document](#answers) with a caption describing what is plotted**.
In plot 2, what is the benefit of the regression line?
Is there anything useful about knowing the slope of that line?
With the information you have available, how much different would you predict temperatures to be in 100 years at this location, assuming the current data is a good predictor of the future temperatures?
Is this value surprising?
5. **Add a link to the plotly version of your plot #2 to the [Answers section of this document](#answers)**.
What did you modify to create this version of the plot?
Do you find it easier to make changes to the format of the plot in plotly or using matplotlib?

## Hints
If you get stuck, have a look at the [hints for this week's exercise](https://github.com/Python-for-geo-people/Lesson-7-Plotting/blob/master/Lesson/hints.md).

# Answers
This is some text.
You can make it **bold** or use *italics*.
You can also display images, as shown below.

![A sine curve](img/sine-curve.png)<br/>
*Figure 1. A sine curve*.
