#!/usr/bin/env python
# coding: utf-8

# In[18]:


import cv2


# In[19]:


img = cv2.imread("C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_5/scenery.jpg")


# In[20]:


gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[21]:


inverted_gray_image = 255 - gray_image


# In[22]:


blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)


# In[23]:


inverted_blurred_image = 255 - blurred_image


# In[24]:


pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)


# In[25]:


cv2.imshow('Original Image', img)


# In[26]:



cv2.imshow('New Image', pencil_sketch_image)


# In[ ]:



cv2.waitKey(0)

