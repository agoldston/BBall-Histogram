#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

years = range(1950, 2025)
url_link = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

for year in years:
  url = url_link.format(year)
  print(url)


# In[19]:


df = pd.read_html(url, header = 0)
df


# In[21]:


len(df)


# In[22]:


df[0]


# In[23]:


df2024 = df[0]


# In[26]:


df2024[df2024.Age == 'Age']


# In[27]:


len(df2024[df2024.Age == 'Age'])


# In[29]:


df = df2024.drop(df2024[df2024.Age == 'Age'].index)
df.shape


# In[30]:


import seaborn as sns


# In[39]:


sns.distplot(df.PTS, 
             kde=False)


# In[40]:


sns.distplot(df.PTS, 
             kde=False,
             hist_kws=dict(edgecolor="black", linewidth=2))


# In[41]:


sns.distplot(df.PTS,
             kde=False,
             hist_kws=dict(edgecolor="black", linewidth=2),
             color='#00BFC4')


# In[ ]:




