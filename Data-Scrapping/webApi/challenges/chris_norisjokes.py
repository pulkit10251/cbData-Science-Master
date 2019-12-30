#!/usr/bin/env python
# coding: utf-8

# In[102]:


import requests
import json


# In[103]:


url="https://api.icndb.com/jokes/"


# In[104]:


n=input()


# In[105]:


r=requests.get(url+n)


# In[106]:


print(r.url)


# In[107]:


type(r.content)


# In[108]:


work=json.loads(r.content)


# In[109]:


print(work)


# In[110]:


workpp=work['value']
print(workpp['joke'])


# In[111]:


with open("jokes.csv","w") as f:
    f.write(workpp['joke'])


# In[ ]:




