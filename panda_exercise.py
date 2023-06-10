#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import matplotlib.pyplot as plt


# In[42]:


# read the dataset
churn_data = pd.read_csv('telecom_churn.csv')
churn_data.head()


# In[43]:


# check the dimensinality of the dataframe by printing the shape of the dataframe
churn_data.shape


# In[44]:


# check the information of the dataset
churn_data.info()


# In[45]:


# check the descriptive statistics of the dataset
churn_data.describe()


# In[46]:


# change the data type of the churn column from boolean to int64 and check the dataframe again
churn_data['Churn'] = churn_data['Churn'].astype('int64')
churn_data


# In[47]:


# get the distribution of the churn by counting how many churned and how many did not
value_count = churn_data['Churn'].value_counts()
value_count


# In[48]:


# plot the count from the result above

value_count.plot.bar()


# In[49]:


# what is the proportion of churned users in the dataframe
churn_data['Churn'].mean()*100


# In[50]:


# How much time (on average) do churned users spend on the phone during daytime?
churned_users = churn_data[churn_data['Churn'] == 1]  # Filter churned users

average_time = churned_users['Total day minutes'].mean()  # Calculate mean of Total day minutes

print("Average time spent on the phone during daytime by churned users:", average_time)


# In[51]:


# What is the maximum length of international calls among loyal users (Churn == 0) who do not have an international plan?
max_intl_call_length = churn_data.loc[(churn_data['Churn']== 0) & (churn_data['International plan'] == 'No'), 'Total intl minutes'].max()
max_intl_call_length


# In[52]:


# give the values of the first five rows in the first three columns
churn_data.iloc[0:5, 0:3]


# In[53]:


# select all the states that starts with W
mask = churn_data['State'].str.startswith('W')
selected_states = churn_data[mask]

print(selected_states)


# In[54]:


# using the map function, replace Yes and No in the International plan column to True and False
churn_data['International plan'] = churn_data['International plan'].map({'Yes': True, 'No': False})
churn_data.head()


# In[55]:


# we want to understand the total calls that have been made by customers. Total_calls is calculated as
# the sum of Total dat calls, Total eve calls, Total night calls, Total intl calls.

churn_data['Total_calls'] = churn_data['Total day calls'] + churn_data['Total eve calls'] + churn_data['Total night calls'] + churn_data['Total intl calls']

churn_data.head()


# In[56]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[58]:


# create a count plot to understand the churn of the international plan

sns.countplot(data=churn_data, x='International plan', hue='Churn')
plt.title('Churn of International Plan')
plt.xlabel('International Plan')
plt.ylabel('Count')
plt.show()


# In[ ]:




