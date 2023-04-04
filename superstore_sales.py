#!/usr/bin/env python
# coding: utf-8

# <h1> Objective:
# 
#     
#     
# - What is the overall sales trend?
# -What are the top 10 products by sales? 
# -What are the most selling products?
# -What is the most preferred ship mode?
# -Which are the most profitable categories and sub categories?

# <h4> Importing Required Libraries

# In[66]:


#Data Manipulation
import pandas as pd

#Data Vizualization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# <h4> Importing the dataset

# In[2]:


df=pd.read_excel('superstore_sales.xlsx')


# <h4> Data Audit

# In[3]:


#First five rows of dataset
df.head()


# In[4]:


#Last five rows of the dataset
df.tail()


# In[6]:


#Shape of dataset
df.shape


# In[7]:


#Columns in dataset
df.columns


# In[9]:


#Summary of dataset
df.info()


# In[11]:


#Check for missing values
df.isnull().sum()


# In[12]:


#Getting descriptive statitiscs summary
df.describe()


# <h1> Exploratory Data Analysis

# <h4> What is the overall sales trend?

# In[15]:


df['order_date'].min()


# In[16]:


df['order_date'].max()


# In[17]:


#Getting the month and year from the dataset
df['month_year']=df['order_date'].apply(lambda x: x.strftime('%Y-%m'))


# In[21]:


#Grouping month year from the dataset
df_trend=df.groupby('month_year').sum()['sales'].reset_index()


# In[25]:


#Setting the figure size
plt.figure(figsize=(15,6))
plt.plot(df_trend['month_year'],df_trend['sales'])
plt.xticks(rotation='vertical',size=8)
plt.show()


# Overall pattern shows sales are increasing 

# <h4> What are the top 10 products by sales?

# In[52]:


#Grouping product name column
prod_sales=pd.DataFrame(df.groupby('product_name').sum()['sales'])


# In[77]:


#Sorting product sales in descending order
prod_sales.sort_values('sales',ascending=False).head(10)


# <h4> What are the most selling products?

# In[40]:


#Grouping product name
most_sold_prod=pd.DataFrame(df.groupby('product_name').sum()['quantity'])


# In[46]:


# Sorting the most dold products
most_sold_prod=most_sold_prod.sort_values('quantity',ascending=False)


# In[47]:


most_sold_prod[:10]


# <h4> What is the most preferred ship mode?

# In[72]:


#Setting figure size
plt.figure(figsize=(10,8))
#Plotting shipmode
sns.countplot(df['ship_mode'])
plt.show()


# Standard class is the most preferred ship mode.

# <h4> What are the most profitable category and sub-category?

# In[74]:


#Grouping category and sub-category
cat_subcat_profit=pd.DataFrame(df.groupby(['category','sub_category']).sum()['profit'])


# In[75]:


#Sorting the values
cat_subcat_profit.sort_values(['category','profit'],ascending=False)


# In[ ]:




