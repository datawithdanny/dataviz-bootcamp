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
# COMING SOON

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.ion()


# In[2]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# In[3]:


# load our video game sales dataset
df = pd.read_csv("data/video-game-sales.csv")
df.head()


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)

# ## Business Case Study
# 
# Imagine that we are running an online blog which reports on video games throughout the years.
# 
# We've discovered this dataset and we want to describe the transformational journey that video games have experienced over the past 2 decades.
# 
# In particular we want to try to answer a few questions about our dataset:
# 
# 1. How many records do we have?
# 2. What was the most popular game ever based on total sales?
# 3. How many years' of data do we have and how many games were released per year?
# 4. Which region has the most sales? How does it compare to the others?
# 5. Show the releases and total sales for each genre - is there any relationship?
# 6. Were there specific genres which experienced explosive growth in releases over time?
# 

# 
