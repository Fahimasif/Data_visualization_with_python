#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Home work 2


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


df = pd.read_csv("hyundai.csv")
display(df.head())
display(df.tail())


# In[3]:


df.info()


# Pie chart

# In[4]:


df["transmission"].value_counts().plot(kind="pie", 
                                       autopct='%1.1f%%', 
                                       startangle=180)
plt.ylabel("")
plt.show()


# In[ ]:


This pie chart is not a good visualizaton tool in here because it has 4 class and datas are overlaping.


# Bar Plot

# In[5]:


df_fuelType = pd.DataFrame(df["fuelType"].value_counts())
df_fuelType = df_fuelType.reset_index()
df_fuelType = df_fuelType.rename(columns={"index":"fuelType",
                                          "fuelType":"no_of_cars"})

df_fuelType["% of cars"] = (df_fuelType["no_of_cars"]/df.shape[0])*100

df_fuelType = df_fuelType.round(2)
display(df_fuelType)


# In[7]:


sns.barplot(x="fuelType", 
            y="% of cars", 
            data=df_fuelType, 
            color="blue",
            alpha=0.8)

plt.xlabel("Types of fuel")
plt.ylabel("% of cars")
plt.title("Percentage of cars present in each fuelType")

plt.yticks(np.arange(0,101,10))

plt.show()


# Home work 3

# In[12]:


plt.figure(figsize=(20,16))

plt.subplot(2, 1, 1)
sns.scatterplot(x="mileage", y="price", data=df)

plt.subplot(2, 1, 2)
sns.scatterplot(x="mpg", y="price", data=df)


plt.tight_layout()
plt.show()


#  regression plot

# In[30]:


plt.figure(figsize=(20,16))
plt.subplot(2, 1, 1)
sns.regplot(x="mileage", y="price", data=df, line_kws={"color":"red"})

plt.subplot(2, 1, 2)
sns.regplot(x="mileage", y="price", data=df, scatter_kws={"color":"orange", "edgecolor":"white"})

plt.tight_layout()
plt.show()


# Pair plot

# In[29]:


sns.pairplot(df, corner=True)
plt.show()


# Pair plot is inconvinent here because there is large amount of data.

# In[ ]:




