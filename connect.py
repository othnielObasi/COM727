#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import csv
import os
os.getcwd()


def get_api_key():
    api_key = os.environ.get('API_KEY')
    if api_key:
        return api_key
    else:
        with open('api_key.txt') as f:
            reader = csv.reader(f)
            api_key = next(reader)[0]
            return api_key

