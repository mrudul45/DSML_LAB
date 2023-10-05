#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
m=np.array([7,9,17,28,])
print(m)


# In[2]:


print (type(m))


# In[3]:


print(m.shape)


# In[5]:


p=np.array([[7,9],[17,28]])
print(p)
print(p.shape)


# In[8]:


t=np.array([[1+0.j,2+3.j],[2+2.j,4+1.j]])
print(t)
print(t.shape)


# In[9]:


q=np.zeros((3,4))
print(q)
print(q.shape)
r=np.ones((2,3))
print(r)
print(r.shape)


# In[12]:



h=np.eye(4,5)
print(h)
print(h.shape)


# In[13]:


k=np.arange(10)
print(k)
print(k.shape)


# In[14]:


l=np.arange(4,20)
print(l)
print(l.shape)


# In[16]:


o=np.arange(2,15,4)
print(o)
print(o.shape)


# In[25]:


x=np.linspace(5,20,5)
print(x)


# In[26]:


s=np.random.random((3,3))
print(s)


# In[32]:


i=np.random.random((5,4))
print(i.reshape(2,2,5))


# In[33]:


print(k)
print(k[5])
print(k[-1])
print(k[::2])
print(k[3:])
print(k[2::])
print(k[-4:])
print(k[2:-2])


# In[34]:


n=np.arange(1,26)
print(n)
n=n.reshape((5,5))
print(n)
print(n[:3,:3])
print(n[2:-1,1:-1])
print(n[:,:-1])
print(n[:,-1])
print(n[::,::2])
print(n[1::2,1::2])
print(n[::3])


# In[ ]:




