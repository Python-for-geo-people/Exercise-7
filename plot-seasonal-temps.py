# -*- coding: utf-8 -*-
"""plot-seasonal-temps.py

DESCRIBE WHAT CODE DOES HERE

@author: YOUR NAME - DATE
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from scipy.stats import linregress   # Used for calculating the regression lines

# Temperature conversion function
#
# FIX 1 - Define value to return for temperature function
def FahrenheitToCelsius(temperature):
    return 

# Load data files
#
# FIX 2 - Add names of files to load
summerBad = np.loadtxt(fname="", delimiter=",")
summer = np.loadtxt(fname="", delimiter=",")
winterBad = np.loadtxt(fname="", delimiter=",")
winter = np.loadtxt(fname="", delimiter=",")

# Convert temperatures to Celsius
#
# FIX 3 - Add values used to convert temperatures, done once per data file
 = FahrenheitToCelsius()
 = FahrenheitToCelsius()
 = FahrenheitToCelsius()
 = FahrenheitToCelsius()

# Calculate linear regressions for each data file
#
# FIX 4 - Add x and y data used for linear regression calculation (replace x, y below)
# (sB = Summer w/ bad values, s = Summer, wB = Winter w/ bad values, w = Winter)
sB_slope, sB_intercept, sB_r_value, sB_p_value, sB_std_err = linregress(x, y)
s_slope, s_intercept, s_r_value, s_p_value, s_std_err = linregress(x, y)
wB_slope, wB_intercept, wB_r_value, wB_p_value, wB_std_err = linregress(x, y)
w_slope, w_intercept, w_r_value, w_p_value, w_std_err = linregress(x, y)

#-- PLOT #1 - All seasonal temperatures ---
# Create figure
mpl_fig = plt.figure()

# Plot summer seasonal temperatures in red
#
# FIX 5 - Replace x and y below with data to plot
plt.plot(x, y, 'r*', label="Summer (bad)")
plt.plot(x, y, 'ro', label="Summer")

# Plot winter seasonal temperatures in blue
#
# FIX 6 - Replace x and y below with data to plot
plt.plot(x, y, 'b*', label="Winter (bad)")
plt.plot(x, y, 'bo', label="Winter")

# Set axis range
#
# FIX 7 - Set axis range to avoid overlap between plotted points and legend
plt.axis([])

# Add legend
plt.legend()

# FIX 8 - Add axis labels and a title to the plot


# Display plot #1
plt.show()

#-- PLOT #2 - "Good" seasonal temperatures w/ regression lines ---
# Create figure
mpl_fig2 = plt.figure()

# Plot summer seasonal temperatures in red
#
# FIX 9 - Replace x and y below with data to plot
plt.plot(x, y, 'ro', label="Summer")

# Calculate summer regression line using its slopt and y-intercept
#
# FIX 10 - Replace x below with plotted years
s_line = s_slope * x + s_intercept

# Plot summer regression line
#
# FIX 11 - Replace x below with plotted years
plt.plot(x, s_line, 'r-')

# Display slope on plot as text (deg/a is degrees per year)
#
# FIX 12 - Replace x and y below with location on plot where text should be displayed
# FIX 13 - Insert value of summer slope in .format()
plt.text(x, y, "Summer slope: {0:.4f} deg/a".format())

# Plot winter seasonal temperatures in blue
#
# FIX 14 - Replace x and y below with data to plot
plt.plot(x, y, 'bo', label="Winter")

# Calculate winter regression line using its slopt and y-intercept
#
# FIX 15 - Replace x below with plotted years
w_line = w_slope * x + w_intercept

# Plot winter regression line
#
# FIX 16 - Replace x below with plotted years
plt.plot(x, w_line, 'b-')

# Display slope on plot as text (deg/a is degrees per year)
#
# FIX 17 - Replace x and y below with location on plot where text should be displayed
# FIX 18 - Insert value of summer slope in .format()
plt.text(x, y, "Winter slope: {0:.4f} deg/a".format())

# Set axis range
#
# FIX 19 - Set axis range to avoid overlap between plotted points and legend
plt.axis([])

# Add legend
plt.legend()

# FIX 20 - Add axis labels and a title to the plot


# Export plot to plotly - Uncomment line below for this to work
#unique_url = py.plot_mpl(mpl_fig2, filename="Seasonal average temperatures")

# Display plot #2
plt.show()
