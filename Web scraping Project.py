#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests


# In[5]:


URL="https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())


# In[6]:


job_elements = results.find_all("div", class_="card-content")


# In[7]:


for job_element in job_elements:
    print(job_element, end="\n"*2)


# In[10]:


for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

