#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install scikit-learn


# In[14]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
import sklearn.naive_bayes



# In[15]:


dataset = pd.read_csv('Iris.csv')
print(dataset.describe())
print(dataset.head())


# In[16]:


X=dataset.iloc[:,[1,2,3,4]].values
y=dataset.iloc[:, -1].values


# In[17]:



X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)


# In[18]:


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# In[20]:


classifier = sklearn.naive_bayes.GaussianNB()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)


# In[22]:


cm = confusion_matrix(y_test,y_pred)
ac = accuracy_score(y_test,y_pred)
print("Confusion Matrix:")
print(cm)
print("Accuracy Score:", ac*100,'%')


# In[23]:


new_data = [[5.1,3.5,1.4,0.2],
           [6.2,3.4,5.4,2.3]]


# In[24]:


predictions = classifier.predict(new_data)
for prediction in predictions:
    print(f"predicted class:{prediction}")


# In[ ]:




