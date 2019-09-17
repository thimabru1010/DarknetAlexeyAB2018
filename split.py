#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


# Directory where the data will reside, relative to 'darknet.exe'
#path_data = 'imagens_original_atualizado'
path_data = 'result_img'
data_list = os.listdir(path_data)

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_validation = open('validation.txt', 'w')


# In[4]:

#Split data into train and validation
length = len(data_list)
percentage = 10.0 / 100
length_validation = int( percentage * length )
length_train = int( length - length_validation )
length_train


# In[5]:


cont = 1
# Path to main folder with all the images and txt files
# Path needed to be put into the names in train.txt and validation.txt
path_images = os.path.join( os.getcwd(), 'result_img+txt' )
print(length)
print(length_validation)
print(length_train)

for filename in data_list:
    if cont <= length_validation :
        file_validation.write( os.path.join(path_images, filename) + '\n' )
    else:
        file_train.write( os.path.join(path_images, filename) + '\n' )
    cont += 1
file_train.close()
file_validation.close()


# In[ ]:




