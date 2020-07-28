"""In this project, you will act as a data visualization developer at Yahoo Finance!
You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data.
In finance, a _stock profile_ is a series of studies, visualizations, and analyses
that dive into different aspects a publicly traded company's data.

For the purposes of the project, you will only visualize data for the year of 2017.

After you complete your visualizations, you'll be creating a presentation to share the
images with the rest of the Netflix Stock Profile team.

Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/) """


# Step 1
# Import the modules that you'll be using in this project:

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Step 2
# Let's load the datasets and inspect them.
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted
# for both dividends and splits. This means this is the true closing stock price for
# a given business day.

netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks)

# Note: You can learn more about why the Dow Jones Industrial Average is a industry
# reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).

dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks)


netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head())


# Step 3
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker
# symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted
# for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry
# reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).

# + Is the data represented by days, weeks, or months?
# + In which ways are the files different?
# + What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?

# Data is represented by days.
# Data from NFLX.csv and DJI.csv corresponds only to the first day of the month, while NFLX_daily_by_quarter.csv has
# different days per month (not necessary the first day!).
# Column names are very similar, except 'Quarter' which is included solely in NFLX_daily_by_quarter.csv

# Step 4
# Great! Now that we have spent sometime looking at the data.

print(netflix_stocks.head())

# What do you notice? The first two column names are one word each, and the only one that is not
# is `Adj Close`! The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation.
# In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
# This means this is the column with the true closing price, so these data are very important.
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work
# with the data. Remember to use `inplace=True`.
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.

netflix_stocks.rename(columns={'Adj Close': 'Price'},inplace=True)
print(netflix_stocks.head())

netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'},inplace=True)
print(netflix_stocks_quarterly.head())

dowjones_stocks.rename(columns={'Adj Close': 'Price'},inplace=True)
print(dowjones_stocks.head())

# Step 5

# In this step, we will be visualizing the Netflix quarterly data!
# We want to get an understanding of the distribution of the Netflix quarterly stock
# prices for 2017. Specifically, we want to see in which quarter stock prices flucutated
# the most. We can accomplish this using a violin plot with four violins, one for each business quarter!

# General figure styling.
sns.set_context('poster', rc ={'axes.titlesize': 15, 'axes.labelsize':13, 'xtick.labelsize': 15, 'ytick.labelsize':15 })
sns.set_style('whitegrid')
sns.set_palette('Reds')

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')
sns.despine(right=True, left=True, top=True, bottom=True)
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
ax.set_ylabel('Closing Stock Price (US$)')
ax.set_xlabel('Business Quarters in 2017')
# plt.savefig('Netflix_stocks_capstone/graphs/Distribution of 2017 Netflix Stock Prices by Quarter.png')
plt.show()

# Statistics calculations
# netflix_stocks_quarterly.Price.mean() #165.37426305976095
# netflix_stocks_quarterly.Price.std() #21.29564144539733
# netflix_stocks_quarterly.groupby('Quarter').max() #202.679993
# netflix_stocks_quarterly.Price.min() #127.489998

# Most of the prices fall through the price range between 140 and 180.

# Step 6
# Next, we will chart the performance of the earnings per share (EPS) by graphing the
# estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters.
# We will accomplish this using a scatter chart.

#Initial data
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

# General figure styling
fig, _ = plt.subplots(figsize=(8, 8))
sns.set_style('white')
sns.set_context('poster', rc ={'axes.titlesize': 15, 'axes.labelsize':13, 'xtick.labelsize': 15, 'ytick.labelsize':15 })

# Plot
plt.scatter(x=x_positions, y=earnings_actual, color='#e33c1b', alpha=0.5, marker='o', linewidths=0)
plt.scatter(x=x_positions, y=earnings_estimate, color='#1b65e3', alpha=0.5, marker='s', linewidths=0)
sns.despine(right=True, top=True)
plt.legend(['Actual','Estimate'], prop={'size':15}, loc=4)
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')
plt.ylabel('Estimaded and Actual Earnings per share (US$)')
plt.xlabel('Business Quarters in 2017')
# plt.savefig('Netflix_stocks_capstone/graphs/Actual reported quarterly earnings per
# share (EPS) vs the estimated quarterly EPS.png')
plt.show()

# In the second and fourth quarters, both the estimated and actual EPS were the same.

# Step 7

# Next, we will visualize the earnings and revenue reported by Netflix by mapping
# two bars side-by-side. We have visualized a similar chart in the second Matplotlib
# lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# General figure styling.
fig, _ = plt.subplots(figsize=(8, 8))
sns.set_context('poster', rc ={'axes.titlesize': 15, 'axes.labelsize':13, 'xtick.labelsize': 15, 'ytick.labelsize':15 })
sns.set_style('white')
sns.despine(right=True, top=True)
sns.set_palette('Reds')

# Plot
## Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = len(revenue_by_quarter) # Number of sets of bars
w = 1 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars1_x, revenue_by_quarter)

## Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = len(earnings_by_quarter) # Number of sets of bars
w = 1 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars2_x, earnings_by_quarter)

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]

labels = ['Revenue', 'Earnings']
plt.legend(labels, prop={'size':15}, loc=2)
plt.xticks(middle_x, quarter_labels)
plt.ylabel('Billions of dollars (US$)')
plt.xlabel('Business Quarters 2017-18')
plt.title('Earnings vs. revenue \n 2Q17 - 1Q18')
# plt.savefig('Netflix Stocks Capstone/Earnings and revenue reported 2017-18.png')
plt.show()

earnings_ratio = [(x / y) * 100 for x, y in zip(earnings_by_quarter, revenue_by_quarter)]
print(earnings_ratio)
# Output: [2.3512544802867383, 4.348657718120806, 5.638905775075988, 7.8410810810810805]

# Revenue follows an increasing trend similar to the Earnings.

# Step 8
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017.
# We will accomplish this by plotting two line charts side by side in one figure.
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align
# vertically side by side.

# General figure styling.
fig, _ = plt.subplots(figsize=(8, 8))
sns.set_context('poster', rc ={'axes.titlesize': 15, 'axes.labelsize':13, 'xtick.labelsize': 12, 'ytick.labelsize':13 })
sns.set_style('white')
sns.despine(right=True, top=True)
sns.set_palette('Reds')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xticklabels(months, rotation=90)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price (US$)')

# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dow Jones')
ax2.set_xticklabels(months, rotation=90)
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price (US$)')
plt.subplots_adjust(wspace=.5)
# plt.savefig('Netflix_stocks_capstone/graphs/Netflix vs. Dow Jones.png')
plt.show()

# Step 9
# It's time to make your presentation! Save each of your visualizations as a png file
# with `plt.savefig("filename.png")`. As you prepare your slides, think about the answers
# to the graph literacy questions. Embed your observations in the narrative of your slideshow!
