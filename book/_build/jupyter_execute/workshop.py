#!/usr/bin/env python
# coding: utf-8

# # Live Workshop Tutorial
# 
# ## Introduction
# 
# This online tutorial was created for a live data visualization workshop held at Sydney University in May 2022.
# 
# The purpose of this tutorial is to get you up and running with simple data visualisations in Python as quickly as possible - no prior experience required!
# 
# ### How should I use this tutorial?
# 
# First we will need to initialize the Python environment for this tutorial.
# 
# You can click on any of the 3 options below:
# 
# 1. [Google Colab Notebook](https://colab.research.google.com/github/datawithdanny/dataviz-bootcamp/blob/main/book/workshop.ipynb)
# 2. [Binder JupyterHub Instance](https://mybinder.org/v2/gh/datawithdanny/dataviz-bootcamp/main?urlpath=lab/tree/book/workshop.ipynb)
# 3. <a onclick="initThebeSBT()">Make this page an interactive book</a>
# 
# :::{admonition} Danny's Recommendation
# :class: tip
# 
# This tutorial was designed with interactivity in mind so the main focus should be:
# 
# 1. Running the Python code
# 2. Try to understand what it's doing
# 3. Make changes and run it again to see what happens
# 4. Iterate and keep improving
# :::
# 
# ## Getting Help
# 
# If you have any questions or spot any errors - please [add a new GitHub issue](https://github.com/datawithdanny/dataviz-bootcamp/issues/new?title=Issue%20on%20page%20%2Fworkshop.html&body=Your%20issue%20content%20here.) directly at our repo.
# 
# We're a pretty lot but if we've got some time, we'll try our best to help provide some guidance :)
# 
# You can also support our data educational initiatives by:
# 
# * **[Adding a ⭐️ to our GitHub Repo](https://github.com/DataWithDanny/dataviz-bootcamp)**
# * **Follow us on LinkedIn!**
#     + [Danny](https://www.linkedin.com/in/datawithdanny/)
#     + [Akshaya](https://www.linkedin.com/in/akshaya-parthasarathy23/)
#     + [Leah](https://www.linkedin.com/in/ndleah/)
# * **Join us at [Data With Danny!](https://wwww.datawithdanny.com)**

# :::{admonition} Important for Google Collab
# :class: warning
# 
# On Google Colab notebooks - the version of Matplotlib package is outdated and will not work with all the code from this tutorial!
# 
# The command to update this package is:
# 
# ```base
# pip install --upgrade matplotlib==3.5.1
# ```
# 
# To run this update, you will need to uncomment the following code cell below as instructed and run it. Please follow the prompts to re-initialize the Jupyter Notebook kernel before continuing with the tutorial!
# :::

# In[1]:


# Uncomment the line below by removing the hashtag at the front - keep the `!` though!
#!pip install --upgrade matplotlib==3.5.1


# ## Import Python Packages
# 
# You will see this a lot in your future data adventures :)

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import os


# ## Getting The Data
# 
# We can run the following cell block to grab the data from a GitHub repo URL where this entire tutorial is stored!

# In[3]:


# load our video game sales dataset
df = pd.read_csv("https://raw.githubusercontent.com/DataWithDanny/dataviz-bootcamp/main/book/data/video-game-sales.csv")

# show the first 5 rows
df.head()


# ## Case Study Summary
# 
# Imagine you're an analyst at a data consultancy and we have a project with our new client - Off Switch Gaming™️
# 
# Our client is a global company and they've commissioned us to help them tell a data driven story about the transformation of video games over the past 2 decades.
# 
# In particular the Off Switch team wants us to use a particular data asset one of their team members scraped from the web.
# 
# The dataset includes the following fields:
# 
# | Column Name   | Description                      |
# | ------------- | -------------------------------- |
# | rank          | Game ranking by global sales     |
# | game          | Name of the game                 |
# | platform      | Name of the gaming platform      |
# | release_year  | Year a game was released in YYYY |
# | genre         | Game genre                       |
# | publisher     | Name of the game publisher       |
# | north_america | USA & Canada sales in $ millions |
# | europe        | Europe sales in $ millions       |
# | japan         | Japan sales in $ millions        |
# | other         | All other countries sales        |
# | total_sales   | Combined total sales             |
# 
# ## Practice Questions
# 
# Let's answer some business questions using our data. Don't worry too much about the code used for the data manipulation, we want to focus on the raw data outputs and use these to visualize our results, and eventually use this to tell our story!
# 
# ### Question 1
# 
# > How many games were released per year?
# 
# This is some Pandas code in the cell below to perform the required data manipulation.
# 
# Each line below does something, so once you're comfortable with the output - try playing around with the code below to see how your changes affect the output.

# In[4]:


# we can assign a new variable to the Python operations using `=`
# using the brackets () is known as "chaining" and makes code look nice
q1_dataset = (
    df["release_year"]
        .value_counts(sort=False)
        .reset_index(name="games_count")
        .rename(columns={"index": "release_year"})
)

# below we can just show our resulting dataset like so
q1_dataset


# Next we can do some basic plotting with `q1_dataset` - I think a basic line chart is a nice place to start.
# 
# Let's try to change some of the code below to create something a bit more meaningful.
# 
# **Note**: if you're on Google Colab and haven't yet updated the `matplotlib` using `!pip install --upgrade matplotlib==3.5.1` then the following code block will give you an error

# In[5]:


fig1, ax1 = plt.subplots(figsize=(8,6))  # set the size of the chart

plt.plot(
    q1_dataset["release_year"],  # x-values
    q1_dataset["games_count"],   # y-values
    # additional aesthetic options you can play around with
    # view all options here: 
    color='green',               
    marker='o',
    linestyle='dashed',
    linewidth=1,
    markersize=8
)
# you may want to update some of this below!
plt.grid(True)
plt.title('New Games Released Each Year', fontsize=16)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('New Games', fontsize=12)

# after plotting the data, format the labels with thousands comma separator
# yeah I know, the formatting input is x but the axis is y - deal with it...
ax1.yaxis.set_major_formatter('{x:,.0f}')
ax1.tick_params(axis='y',which='major')

# you can uncomment these next 2 lines to see what happens
# ax.xaxis.set_major_formatter('{x:,.0f}')
# ax.tick_params(axis='x',which='major')

# show the chart
plt.show()

# uncomment the code below to save the chart to a file
# you can also change the name of the file output too
# plt.savefig('yearly_game_releases.png')

# you can also uncomment the next line to create a new directory
# and save the file to a specific path
# if not os.path.exists('outputs'):
#     os.makedirs('outputs')
# plt.savefig('outputs/yearly_game_releases.png')


# ### Question 2
# 
# > What are top 5 most popular game ever based on global sales?

# In[6]:


q2_dataset = (
    df[df["rank"] <= 5]
        [["game", "rank", "total_sales"]]
        .sort_values("rank")
)

q2_dataset


# This dataset by itself is quite explanatory - however we can make the story go a little bit further.
# 
# What if we were to also calculate the percentage of all sales ever these top 5 games make up?
# 
# We can use this insight as a headline subtitle for our following simple chart to jazz things up a little.

# In[7]:


top_5_sales = q2_dataset["total_sales"].sum()
all_sales_ever =  df["total_sales"].sum()

top_5_sales_percentage = top_5_sales / all_sales_ever

# this is called f-string interpolation
top_5_insight = f"The top 5 games made ${top_5_sales:.0f}M in global sales, that's {top_5_sales_percentage:.1%} of all sales ever!"

print(top_5_insight)


# Now we can apply a simple horizontal barchart to visualise our top 5 games and their relative sales performance.

# In[8]:


fig2, ax2 = plt.subplots(figsize=(8,6))  # set the size of the chart

horizontal_barchart = plt.barh(
    q2_dataset["game"],       # bar chart categories
    q2_dataset["total_sales"] # bar chart values
)

# Changing the titles and labels of x-y axes
plt.suptitle('Top 5 Best Selling Games Ever', fontsize=20)
plt.title(top_5_insight, fontsize=10, loc="left")
plt.xlabel('Sales ($ Millions)', fontsize=12)

# We can set specific limits for our x-axis to control the width
# try commenting out the line below to see what happens
plt.xlim(0, 100)

# Set the chart order and color the top sales genre red
ax2.invert_yaxis()  # sort Y categories in reverse order from largest to smallest
horizontal_barchart[0].set_color('r')  # update the colour of the first bar

# this next step applies the label_formattr function using list comprehension
ax2.bar_label(
    horizontal_barchart,
    padding=3,  # this is the distance the label text starts from the bar
    fmt="%.1fM"
)

# show the chart
plt.show()

# uncomment the code below to save the chart to a file
# you can also change the name of the file output too
# plt.savefig('q2_top_5_games.png')

# you can also uncomment the next line to create a new directory
# and save the file to a specific path
# if not os.path.exists('outputs'):
#     os.makedirs('outputs')
# plt.savefig('outputs/q2_top_5_games.png')


# ### Question 3
# 
# > What are the top genres by sales?
# 
# Let's use the `total_sales` to apply a simple group by aggregate sum calculation and sort the values in descending order.

# In[9]:


q3_dataset = (
    df.groupby(["genre"])
        .agg(sales=("total_sales", "sum"))
        .sort_values("sales", ascending=False)
)

q3_dataset


# We can use a simple horizontal bar chart for this type of data.
# 
# The horizontal orientation let's the viewer easily read the name of the genre without needing to rotate their head 45 degrees.

# In[10]:


fig3, ax3 = plt.subplots(figsize=(8,6))  # set the size of the chart

horizontal_barchart = plt.barh(
    q3_dataset.index,    # bar chart categories
    q3_dataset["sales"] # bar chart values
)

# Changing the titles and labels of x-y axes
plt.title('Sum of Sales by Genre', fontsize=16)
plt.xlabel('Sales ($ Millions)', fontsize=12)
plt.ylabel('Genre', fontsize=12)

# Set the chart order and color the top sales genre red
ax3.invert_yaxis()  # sort Y categories in reverse order from largest to smallest
horizontal_barchart[0].set_color('r')  # update the colour of the first bar

# We can change the formatting for the x-axis with a $ and M
ax3.xaxis.set_major_formatter('${x:,.0f}M')
ax3.tick_params(axis='y',which='major')

# We can also do some more custom formatting of the data label
# First we define a function to help with custom formatted label
def label_formatter(x):
    if x > 1e3:
        return f'${x/1e3:,.2f}B'
    else:
        return f'${x:,.0f}M'

# The following is a bit of a hacky way to assign new labels
# this helps us get the barplot rectangles
container = ax3.containers[0]  
# this next step applies the label_formattr function using list comprehension
ax3.bar_label(
    container,
    padding=3,  # this is the distance the label text starts from the bar
    labels=[label_formatter(x) for x in container.datavalues]
)

# This shifts the right edge of the plot to fit the labels
plt.subplots_adjust(right=1.7)

# show the chart
plt.show()

# uncomment the code below to save the chart to a file
# you can also change the name of the file output too
# plt.savefig('q3_genre_sales.png')

# you can also uncomment the next line to create a new directory
# and save the file to a specific path
# if not os.path.exists('outputs'):
#     os.makedirs('outputs')
# plt.savefig('outputs/q3_genre_sales.png')


# For the following questions - I'll generate the dataset for you, but you'll need to write the rest of the Python plotting code to generate the charts (I'll give you some pointers to guide you however!)

# ### Question 4
# 
# > What are the average sales for each genre?
# 
# Since the average calculation is based off total sales and the total count of games in each genre - I think it'll be useful if we include these aggregated metrics also for more insights.

# In[11]:


q4_dataset = (
    df.groupby(["genre"])
        .agg(
            average_sales=("total_sales", "mean"),
            sales=("total_sales", "sum"),
            count_games=("game", "count")
        )
        .sort_values("average_sales", ascending=False)
)

q4_dataset


# Now would also be a good time to check what the top games are for that `Platform` genre - does this match with what we should expect from our knowledge of the gaming industry?

# In[12]:


(
    df[df["genre"] == "Platform"]
        .sort_values("total_sales", ascending=False)
        .head(5)
)


# Ok - now that we've got our dataset ready to go, I'll leave you alone to write up some code to visualize it!

# In[13]:


# Your data visualization code for q5 goes below here!


# ### Question 5
# 
# > Which games perform the best for each genre?
# 
# To make this a bit easier to digest, let's try to identify the top 3 games for each genre and return all of their columns so we can assess what story we can tell from the data.

# In[14]:


q5_dataset = (
    df
        .sort_values(["genre", "total_sales"], ascending=[True, False])
        .groupby(["genre"])
        .head(3)
        
)

q5_dataset


# This dataset looks really interesting as there are lots of variation in the data.
# 
# What sort of story do you want to tell with this data?

# In[15]:


# Your data visualization code for Q5 goes below here!


# ### Question 6
# 
# > What are the sales for each region?
# 
# This sort of transformation is called "melting" a dataset from wide to long - you can find more information at the Pandas documentation [here!](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html)

# In[16]:


q6_dataset = (
    pd.melt(
        df,
        ["rank","game","platform","release_year","genre","publisher"],
        ["north_america", "europe", "japan", "other"],
        "region",
        "sales"
    )
        .groupby("region")
        .agg(region_sales=("sales", "sum"))
)

q6_dataset


# In[17]:


# Your data visualization code for Q6 goes below here!


# ### Question 7
# 
# > Which games perform the best for each region?

# In[18]:


q7_dataset = (
    pd.melt(
        df,
        ["rank","game","platform","release_year","genre","publisher"],
        ["north_america", "europe", "japan", "other"],
        "region",
        "sales"
    )
        .sort_values(["region", "sales"], ascending=[True, False])
        .groupby("region")
        .head(5)
)

q7_dataset


# In[19]:


# Your data visualization code for Q7 goes below here!

