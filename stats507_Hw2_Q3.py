#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import statistics
import timeit


# In[2]:


# load the datasets
dat_g = pd.read_sas("DEMO_G.XPT")
dat_h = pd.read_sas("DEMO_H.XPT")
dat_i = pd.read_sas("DEMO_I.XPT")
dat_j = pd.read_sas("DEMO_J.XPT")

# Add an additional column identifying to which cohort each case belongs
dat_g['cohort'] = '11-12'
dat_h['cohort'] = '13-14'
dat_i['cohort'] = '15-16'
dat_j['cohort'] = '17-18'

# append multiple dataframes to one
frames = [dat_g, dat_h,dat_i,dat_j]
pd_all = pd.concat(frames)


# In[3]:


# subset columns
df_all = pd_all[["cohort","SEQN","RIDAGEYR","RIDRETH3","DMDEDUC2",
               "DMDMARTL","RIDSTATR","SDMVPSU","SDMVSTRA","WTMEC2YR",
               "WTINT2YR"]]


# In[4]:


# turn off pandas chained assignment
pd.options.mode.chained_assignment = None 

# create a list that has the categorical datatype columns
categpry_cols = ['cohort','SEQN','RIDRETH3','DMDEDUC2','DMDMARTL']

# create a list that has the integer datatype columns
integer_cols = ['RIDAGEYR','RIDSTATR','SDMVPSU','SDMVSTRA']

# use for loops tp convert the data to category type and int32 type
for col in categpry_cols:
    df_all[col] = df_all[col].astype('category')
for col in integer_cols:
    df_all[col] = df_all[col].astype('int64')


# In[5]:


# rename columns to literal name
df_all.rename(columns={'SEQN': 'id', 
                   'RIDAGEYR': 'age',
                   'RIDRETH3':'race and ethnicity',
                   'DMDEDUC2':'education',
                   'DMDMARTL':'marital status'
                    }, inplace=True)


# In[6]:


# save dataframe to pickle format
df_all.to_pickle("nhanes.pkl")


# ### b

# In[7]:


# load the datasets
dat_teeth_g = pd.read_sas("OHXDEN_G.XPT")
dat_teeth_h = pd.read_sas("OHXDEN_H.XPT")
dat_teeth_i = pd.read_sas("OHXDEN_I.XPT")
dat_teeth_j = pd.read_sas("OHXDEN_J.XPT")

# create a column to identify to which cohort each case belongs.
dat_teeth_g['cohort'] = '11-12'
dat_teeth_h['cohort'] = '13-14'
dat_teeth_i['cohort'] = '15-16'
dat_teeth_j['cohort'] = '17-18'

# concatenate 4 dataframes to one dataframe
frames = [dat_teeth_g, dat_teeth_h,dat_teeth_i,dat_teeth_j]
pd_teeth_all = pd.concat(frames)

# save dataframe to pickle format
pd_teeth_all.to_pickle("nhanes_teeth.pkl")

# Use regex to subset columns
df_subset = pd_teeth_all.filter(regex='(cohort)|(SEQN)|(OHDDESTS)|(OHX)[0-9]{2}(TC)|(OHX)[0-9]{2}(CTC)')


# In[8]:


# turn off pandas chained assignment
pd.options.mode.chained_assignment = None 

# create a list that contains "CTC" in a column name
ctc_col = [i for i in df_subset.columns if "CTC" in i]

# create a list that has the categorical datatype columns
categpry_cols = ['cohort','SEQN'] + ctc_col

# create a list that has the integer datatype
integer_cols = [i for i in df_subset.columns if i not in categpry_cols]


# In[9]:


# fill the missing values to -1
df_subset = df_subset.fillna(-1)

# use for loops tp convert the data to category type and int32 type
for col in categpry_cols:
    df_subset[col] = df_subset[col].astype('category')
for col in integer_cols:
    df_subset[col] = df_subset[col].astype('int')


# In[10]:


# rename the column names
df_subset.rename(columns={'SEQN': 'id'}, inplace=True)
df_subset.head(1)

# save it to pickle format
df_subset.to_pickle("tooth.pkl")


# ### C

# In[11]:


df_all.shape[0]


# In[12]:


df_subset.shape[0]


# In[ ]:




