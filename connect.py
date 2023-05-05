#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os

def sky_v():
    file_path = os.path.join(os.getcwd(), "root", "giraffe.txt")
    try:
        with open(file_path, "r") as f:
            key = f.read().strip()
        return key
    except FileNotFoundError:
        print(f"Error: file not found at path {file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

