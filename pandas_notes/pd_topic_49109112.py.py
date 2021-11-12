#!/usr/bin/env python
# coding: utf-8

# ## Name: Li-Hsuan 
# 
# ## UM ID: 49109112

# ## Pandas Aggregation (agg)

# ### An essential piece of analysis in large dataset is efficient summarization
# 
# ### There are a few aggregation operations in Pandas that are useful
# 
# 
# - sum()
# 
# - mean()
# 
# - median()
# 
# - min()
# 
# - max()

# In[ ]:


### Aggregate using one or more operations over the specified axis


# In[ ]:


# create df
df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])
df


# In[ ]:


# sum and min aggregation operation
df.agg(['sum', 'min'])


# ### Normally, it is used hand in hand with group_by to find the aggregation on groups
# 
# - first specify the column (group) and then apply agg

# In[ ]:


# create example df
data1 = {'Name':['Max', 'Bill', 'Max', 'Princi', 
                 'Gaurav', 'Bill', 'Princi', 'Tom'], 
        'salary(K)':[80, 78, 56, 110, 
               78, 87, 150, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['MS', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'Phd', 'MA', 'MS']}
df = pd.DataFrame(data1)
df


# In[ ]:


# group by Name
df.groupby(['Name']).mean()


# In[ ]:


df.groupby(['Name','Qualification']).sum()


# - multiple aggregrations
# - use {Column:Operation} to specify the group and which operations to use

# In[ ]:


df.groupby('Name').agg({'salary(K)':['min', 'max']})

