#!/usr/bin/env python
# coding: utf-8

# In[4]:


from matplotlib import pyplot as plt 
y = [1,2,11,8,4,1,10,8,3]
plt.plot(y) 
plt.show()


# In[9]:


x = [-4,-6,-3,-2,-1,0,1,2,3,6,4]
y = [i**2 for i in x]
plt.plot(x,y)
plt.show()


# In[12]:


import numpy as np
import math

x = np.arange(-1,1.1,0.1).tolist()
y = [i**2 + 5 for i in x] 
print(x)
print(y)

plt.plot(x,y) 
plt.show()


# In[6]:


from matplotlib import pyplot as plt 
import numpy as np
x = np.arange(0,8,0.1)
y = np.sin(x) 
print(x)
print(y)
plt.plot(x,y)
plt.scatter(x,y)
plt.xlabel('angle') 
plt.ylabel('sin') 
plt.title('sin wave') 
plt.show()


# In[7]:


from matplotlib import pyplot as plt 
import numpy as np
x = np.arange(0,8,0.1)
y = np.sin(x) 
print(x)
print(y)
plt.plot(x,np.sin(x), 'b+', label='sin') 
plt.plot(x,np.cos(x) ,'y--', label='cos') 
plt.ylabel('sin/cos')
plt.title('sin/cos wave')
plt.ylim(-2,2) 
plt.xlim(-5,15) 
plt.legend() 
plt.show()


# In[9]:



fig, axis = plt.subplots(1,2, figsize=(10,5)) 

x = np.arange(0,10,0.1) 


axis[0].scatter(x,np.sin(x),)
axis[0].set_title('sin')
axis[0].set_xlabel('angle')
axis[0].set_ylabel('sin')


axis[1].plot(x,np.cos(x), 'r--')
axis[1].set_title('cos')
axis[1].set_xlabel('angle')
axis[1].set_ylabel('cos')


plt.show()


# In[ ]:




