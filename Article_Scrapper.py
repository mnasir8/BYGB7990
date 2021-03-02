#!/usr/bin/env python
# coding: utf-8



import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
result = requests.get('https://www.foxnews.com/politics/biden-harris-victory-speech-46th-president-united-states')


soup = BeautifulSoup(result.content, 'html.parser')



body = soup.findAll('body' , {'class':re.compile('fn article-single')})
body1= body[0].text.strip()


print(body1)


headline = soup.select('h1')
headline1 = headline[0].text.strip()
print(headline1)
print('')


# Create a dataframe
data = pd.DataFrame({'Headline': headline1, 'Body': body1}, index=[1])
data


data.to_csv('FOXNEWS_DF.csv')





