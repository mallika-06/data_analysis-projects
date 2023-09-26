#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[74]:


data = pd.read_csv(r"E:\Project+1+-+Weather+Dataset.csv")


# In[75]:


data


# In[76]:


data.head()


# In[77]:


data.shape


# In[78]:


data.index


# In[79]:


data['Wind Speed_km/h'].unique()


# In[80]:


data.columns


# In[12]:


data.dtypes


# In[81]:


data['Rel Hum_%'].unique()


# In[82]:


data.nunique()


# In[83]:


data.count()


# In[84]:


data.value_counts()


# In[85]:


data['Rel Hum_%'].value_counts()


# In[86]:


data.info()


# In[87]:


data.head(2)


# In[88]:


data['Wind Speed_km/h'].nunique()


# In[89]:


data.nunique()


# In[91]:


data['Wind Speed_km/h'].unique()


# In[90]:


data.head(2)


# In[92]:


data.Weather.value_counts()


# In[96]:


#data.head(2)
data[data.Weather == 'Clear']


# In[97]:


data.head(3)


# In[98]:


data.groupby('Weather').get_group('Clear')


# In[99]:


data.head(2)


# In[100]:


data['Wind Speed_km/h'] == 4


# In[101]:


data[data['Wind Speed_km/h'] == 4] #Answer


# In[102]:


data.isnull()


# In[103]:


data.isnull().sum()


# In[104]:


data.notnull().sum()


# In[105]:


data.dtypes


# In[106]:


data.head(2)


# In[108]:


data.rename(columns = {'Weather' : 'Weather condition'}, inplace = True)


# In[109]:


data.head()


# In[110]:


data.head(2)


# In[112]:


data.Visibility_km.mean()


# In[113]:


data.Press_kPa.std()


# In[115]:


data['Rel Hum_%'].var()


# In[116]:


data.head()


# In[117]:


data['Weather condition'].value_counts()


# In[118]:


data['Weather condition'] == 'Snow'


# In[120]:


data[data['Weather condition'].str.contains('Snow')].head(50)


# In[122]:


data[data['Weather condition'].str.contains('Snow')].tail(50)


# In[123]:


data.head(2)


# In[126]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km'] == 25)] 


# In[129]:


data.groupby('Weather condition').mean(numeric_only=True)


# In[130]:


data.head(2)


# In[132]:


data.groupby('Weather condition').min()


# In[133]:


data.groupby('Weather condition').max()


# In[137]:


data[data['Weather condition'] == 'Fog']


# In[138]:


data.head(2)


# In[146]:


data[(data['Weather condition'] == 'Clear') | (data['Visibility_km'] > 40)].tail(50)


# In[147]:


data.head(2)


# In[148]:


data[(data['Weather condition'] == 'Clear') & (data['Rel Hum_%'] > 50 )| (data['Visibility_km']>40)]


# In[ ]:




