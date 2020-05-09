#!/usr/bin/env python
# coding: utf-8

# # EXTRACTING CSV FILE USING SQL COMMAND
# ## SQL COMMAND I USED :
# 
# ### 1. select * from city_list where country='India' (to get the city nearby)
# ### 2. select * from city_data where city='Haora' and avg_temp is not null (to ensure that no null value is extracted)
# ### 3. select * from global_data where avg_temp is not null

# In[1]:


#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


#installing csv file

haora_data=pd.read_csv(r"E:\Data_Science\Haora_Data.csv")
global_data=pd.read_csv(r"E:\Data_Science\Global_Temp.csv")


# In[44]:


#variable for useful data

global_year=global_data['year']
global_temp=global_data['avg_temp']

haora_year=haora_data['year']
haora_temp=haora_data['avg_temp']


# In[90]:


#ploting global tempreture over years in line plot

fig=plt.figure(figsize=(30,8))
plt.plot(global_year,global_temp)
plt.ylim(0,12)
plt.grid()
plt.xlabel('year',fontsize=25)
plt.ylabel('tempreture in C',fontsize=25)
plt.title('Global Tempreture over years',fontsize=30)
plt.show()


# In[89]:


#ploting Haora city tempreture over years in line plot 

fig=plt.figure(figsize=(30,8))
plt.plot(haora_year,haora_temp,color='red')
plt.grid()
plt.xlabel('year',fontsize=25)
plt.ylabel('tempreture in C',fontsize=25)
plt.title('Haora City tempreture over years',fontsize=30)
plt.ylim(15,30)
plt.show()


# In[84]:


#ploting global and Haora city tempreture in same plot
fig=plt.figure(figsize=(30,10))
plt.plot(global_year,global_temp,label='global temp',color='blue')
plt.plot(haora_year,haora_temp,label='haora temp',color='red')
plt.legend(loc=4,fontsize=20)
plt.ylim(0,30)
plt.grid()
plt.xlabel('year',fontsize=25)
plt.ylabel('tempreture in C',fontsize=25)
plt.title('Glabal and Haora City tempreture over year',fontsize=30)
plt.show()


# In[83]:


#ploting plot in 5 years of rolling window

fg=plt.figure(figsize=(30,10))
global_ma=pd.DataFrame(global_temp.rolling(window=5).mean())
haora_ma=pd.DataFrame(haora_temp.rolling(window=5).mean())
plt.plot(global_year,global_ma,color='blue',label='global data')
plt.plot(haora_year,haora_ma,color='red',label='haora data')
plt.legend(loc=4,fontsize=20)
plt.ylim(0,30)
plt.xlabel('year',fontsize=25)
plt.ylabel('tempreture in C',fontsize=25)
plt.grid()
plt.title('global and Haora city tempreture over year with 5 year moving average',fontsize=30)
plt.show()


# In[91]:


#ploting global and haora city tempreture over year with 10 year moving average 

fg=plt.figure(figsize=(30,10))
global_ma=pd.DataFrame(global_temp.rolling(window=10).mean())
haora_ma=pd.DataFrame(haora_temp.rolling(window=10).mean())
plt.plot(global_year,global_ma,label='global data')
plt.plot(haora_year,haora_ma,label='haora data')
plt.legend(loc=4,fontsize=20)
plt.ylim(0,30)
plt.grid()
plt.xlabel('year',fontsize=25)
plt.ylabel('tempreture in C',fontsize=25)
plt.title('globla and haora city tempreture over year with 10 year moving average',fontsize=30)
plt.show()


# # TOOLS USED:
# 
# I used python as programming language. For this project, NumPy, Pandas and Matplotlib libraries has been used. SQL is used for extracting data from the global_data, city_data, city_list table.

# # PROCESS:
# 
# 1. Firstly all the useful data i.e. year and avg_temp for both Haora City and Global were given a variable name.
# 2. Plotted the graph individually for both GLobal and Haora City.
# 3. To calculate the moving average for avg_temp in global_data and Haora_data, pandas rolling method is used with 5 years and 10 years window value.
# 4. Plotted the line graph in same plot to take observations.

# # OBSERVATIONS:
# 
# 1. Line graph with 1 Year window was a bit rough to take obseravtion. 5 Year moving average line graph was a bit smooth to take observation but 10 Year moving average line graph was more smoother.
# 2. Global tempreture is increasing continously from last few hundred years.
# 3. Haora City tempreture was significantly low in mid of 19th century and started increasing.
# 4. Before 1870 tempreture was balanced but after that Global as well as Haora city tempreture started increasing consistently.
