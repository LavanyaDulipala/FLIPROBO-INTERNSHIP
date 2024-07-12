#!/usr/bin/env python
# coding: utf-8

# # Internship- File1- DS2406

# In[5]:


def func(a, b):
    return b if a == 0 else func(b % a, a)
print(func(30, 75))


# In[6]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))


# In[11]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3={99,22,17}

print(len(set1 + set2 + set3))


# In[ ]:


Pickle module: Serialization- Pickling- dump()
               Deserialization-Unpickling-load()
               Wb to write Binary files.


# In[7]:


captains = {
"Enterprise": "Picard",
"Voyager": "Janeway",
"Defiant": "Sisko",
}


# In[5]:


for ship,captain in captains.items():
    print(ship, captain)


# In[6]:


for ship in captains:
    print(ship, captains[ship])


# In[9]:


for ship in captains:
    print(ship, captains)


# In[18]:


captains = {dict}
print(captains)


# In[11]:


type(captains)


# In[13]:


captains.dict()


# In[16]:


captains = {}
print(captains)


# In[22]:


captains{"Enterprise" = "Picard"}
captains{"Voyager" = "Janeway"}
captains{"Defiant" = "Sisko"}
print(captains)


# In[23]:


captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"
print(captains)


# In[24]:


captains = {
"Enterprise": "Picard",
"Voyager": "Janeway",
"Defiant": "Sisko",
}
print(captains)


# In[ ]:


# Result: "Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko"


# In[25]:


captains = {
"Enterprise": "Picard",
"Voyager": "Janeway",
"Defiant": "Sisko",
"Discovery": "unknown",
}
print(captains)


# In[29]:


for item in captains.items():
    print(f"The [ship] is captained by [captain].")


# In[30]:


for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")


# In[31]:


for captain, ship in captains.items():
    print(f"The {ship} is captained by {captain}.")


# In[79]:


captains = {
"Enterprise": "Picard",
"Voyager": "Janeway",
"Defiant": "Sisko",
"Discovery": "unknown",
}
print(captains)


# In[80]:


print(captains)


# In[63]:


del captains
print(captains)


# In[64]:


captains.remove()
print(captains)


# In[81]:


del captains["Discovery"]



# In[82]:


print(captains)


# In[75]:


captains.pop("Discovery")


# In[76]:


print(captains)


# In[77]:


captains["Discovery"].pop()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




