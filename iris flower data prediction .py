#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[3]:


iris_data = pd.read_csv("E:\IRIS.csv")


# In[4]:


iris_data.head()


# In[5]:


iris_data.shape


# In[6]:


iris_data.info()


# In[7]:


iris_data.describe()


# In[9]:


iris_data['species'].value_counts()


# In[10]:


iris_data.isnull().sum()


# In[11]:


iris_data['sepal_length'].hist()


# In[13]:


iris_data['sepal_width'].hist()


# In[14]:


iris_data['petal_length'].hist()


# In[15]:


iris_data['petal_width'].hist()


# In[17]:


colors = ['orange', 'blue', 'red']
species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']


# In[23]:


for i in range(3):
    X = iris_data[iris_data['species'] == species[i]]
    plt.scatter(X['sepal_length'], X['sepal_width'], c = colors[i], label=species[i])
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.legend()
    


# In[24]:


for i in range(3):
    X = iris_data[iris_data['species'] == species[i]]
    plt.scatter(X['petal_length'], X['petal_width'], c = colors[i], label=species[i])
    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    plt.legend()


# In[25]:


for i in range(3):
    X = iris_data[iris_data['species'] == species[i]]
    plt.scatter(X['sepal_length'], X['petal_length'], c = colors[i], label=species[i])
    plt.xlabel('sepal_length')
    plt.ylabel('petal_length')
    plt.legend()


# In[26]:


for i in range(3):
    X = iris_data[iris_data['species'] == species[i]]
    plt.scatter(X['sepal_width'], X['petal_width'], c = colors[i], label=species[i])
    plt.xlabel('sepal_width')
    plt.ylabel('length_width')
    plt.legend()


# In[27]:


iris_data.corr()


# In[33]:


corr = iris_data.corr()
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax)


# In[55]:


le = LabelEncoder()
iris_data['Species'] = le.fit_transform(iris_data['Species'])
iris_data_df = pd.DataFrame.from_dict(iris_data)
iris_data_df.head()


# In[65]:


iris_data_df = pd.DataFrame.from_dict(iris_data)
X = iris_data_df.drop(columns = ['Species'])
y = iris_data_df['Species']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.30)


# In[67]:


model = LogisticRegression()


# In[68]:


model.fit(X_train, y_train)


# In[70]:


print("Accuracy: ",model.score(X_test, y_test) * 100)


# In[ ]:




