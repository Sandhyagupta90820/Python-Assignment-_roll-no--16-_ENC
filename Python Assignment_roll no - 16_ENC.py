#!/usr/bin/env python
# coding: utf-8

# # Python Assignment _ Sandhya Gupta_16_ENC.

# #### Q.1) Write a python program to calculate the length of a string

# In[1]:


length = len(input('write a sentence:  '))
print(length)


# #### Q.2) Python program to calculate the square root.

# In[2]:


import math
number = float(input("Enter a number: "))
sqrt = math.sqrt(number)
print(f"The square root of {number} is {sqrt}")


# #### Q.3) Write a python programto convert temprature in celcius to temprature in Fahrenheit.

# In[3]:


def celsius_to_fahrenheit(c):
    f = c*9/5+32
c = float(input('temperature in celsius: '))
f = (celsius_to_fahrenheit(c))
print(f'{c} is {f}')


# #### Q.4) Write a data type needed for given data.(10,4.5,2+6j)

# In[4]:


data = (10,4.5,2+6j)
a = 10
print(type(a))
b = 4.5
print(type(b))
c = 2+6j
print(type(c))


# In[ ]:




