#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
result = requests.get('https://www.foxnews.com/politics/biden-harris-victory-speech-46th-president-united-states')


# In[2]:


soup = BeautifulSoup(result.content, 'html.parser')


# In[3]:


body = soup.findAll('body' , {'class':re.compile('fn article-single')})
body1= body[0].text.strip()


# In[4]:


print(body1)


# In[5]:


headline = soup.select('h1')
headline1 = headline[0].text.strip()
print(headline1)
print('')


# In[7]:


# Create a dataframe
data = pd.DataFrame({'Headline': headline1, 'Body': body1}, index=[1])
data


# In[8]:


data.to_csv('FOXNEWS_DF.csv')


# In[ ]:





# In[ ]:




