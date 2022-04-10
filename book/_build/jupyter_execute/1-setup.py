#!/usr/bin/env python
# coding: utf-8

# # Welcome!
# 
# ## Introduction
# 
# This online book was created for a live data visualization workshop for Sydney University held in May 2022.
# 
# This series of Jupyter Notebooks were designed to help learners dive into the basics of Python data visualization using real datasets.
# 
# > **How should I use this book?**
# 
# If you're new to all this, it's recommended to read this book in sequential order or search for a specific topic using the sidebar.
# 
# All code blocks can be executed directly in the browser and additional buttons are available to open up any notebook in Google Colab or in a JupyterLab environment using a technology called Binder.
# 
# > **I have questions, how can I get help?**
# 
# If you have any questions or spot any errors - please add a new issue directly at our GitHub repo.
# 
# ## Getting Started
# 
# coming soon!

# In[1]:


import pandas as pd


# In[2]:


# load our video game sales dataset
df = pd.read_csv("data/video-game-sales.csv")

# show the first 5 rows
df.head()


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)

# ## Business Case Study
# 
# Our client Off Switch Gaming is a global company who wants to understand the transformational journey that video games have experienced over the past 2 decades.
# 
# In particular our client wants us understand a particular data asset one of their analysts created.
# 
# The dataset includes the following fields:
# 
# | Column Name   | Description                      |
# | ------------- | -------------------------------- |
# | rank          | Game ranking by global sales     |
# | name          | Name of the game                 |
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
# ### Exploratory Data Analysis
# 
# * How many games were released per year?
# * What are most popular game ever based on global sales?
# * What are the top genres by sales?
# * What are the average sales for each genre?
# * Which games perform the best for each genre?
# * What are the sales for each region?
# * Which games perform the best for each region?
