#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset - No-show appointments
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.
# 
# **‘ScheduledDay’** tells us on what day the patient set up their appointment.
# 
# **‘Neighborhood’ ** indicates the location of the hospital.
# 
# **‘Scholarship’** indicates whether or not the patient is enrolled in Brasilian welfare program Bolsa Família.
# 
# Be careful about the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up. 
# 
# 
# 

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# In[2]:


# Upgrade pandas to use dataframe.explode() function. 
get_ipython().system('pip install --upgrade pandas==0.25.0')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you **document your data cleaning steps in mark-down cells precisely and justify your cleaning decisions.**
# 
# 
# ### General Properties
# 

# In[3]:


# Load your data and print out a few lines. Perform operations to inspect data
#types and look for instances of missing or possibly errant data.
df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# In[4]:


df.head


# In[5]:


#check data types & check missing data.
df.info()


# The data columnse are 14.
# The dataset contains one dependent variable (no_show) and 13 independent variables.
# The dataset have no missing values.
# The patientId is float data type but enable to convert to int.
# There are three types od data used: float, int and object

# In[7]:


#check data type
df.dtypes


# In[8]:


#checking unique values in each column
df.nunique()


# In[56]:


#look closer to age numerical variables, age histogram
df['age'].plot(kind='hist', color='blue', figsize=(9,7))
plt.title('Patients age',fontsize=15)
plt.xlabel('Age',fontsize=14)
plt.ylabel('Frequency',fontsize=14);


# In[3]:


plt.figure(figsize=(8,6))
sns.boxplot(data['age'], color='green')
plt.title('BOX PLOT OF AGE')
plt.show()


# In[13]:


df.Age.value_counts()


# In[14]:


#finding the shape of data , rows & columns
df.shape


# There are about 110527 records and about 14 columns in the dataset

# In[15]:


#listing columns of data
list(df.columns)


# In[16]:


#converting column names to a lower case names
df.columns = [x.lower() for x in df.columns]
df.info()


# In[17]:


#check dataframe
df.describe()


# This description about No-show appointments columns: PatientId, AppointmentID, Age, Scholarship, Hypertension, Diabetes, Alcoholism, Handicap, SMS_received. In the age value it shows 115 the max.Most of patients do not have Hypertension, Diabetes, Handicaps, and Alcoholism. Above is giving info such as max, min, min and mean.

# In[18]:


df.count()


# In[19]:


#the missing values in the data set
df.isnull().sum()


# In[20]:


#check the duplicates 
df.duplicated().sum()


# In[21]:


#check  the number of pateintid unique values
df['patientid'].nunique()


# There are about 62298 unique value out of 110527

# In[22]:


df['patientid'].duplicated().sum()


# There are about 48228 od duplicated patient id

# 
# ### Data Cleaning
#     > In data cleaning: change data types, renaming names, deleting wrong values,
#  

# In[23]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.


# In[24]:


df.age.value_counts()


# In[25]:


#delete row = age -1
df=df[df['age']!= -1]
#age -1 has removed from the dataframe
df.age.value_counts()


# In[26]:


df.shape


# In[27]:


#renaming data names
df.rename(columns = {'No-show':'No_show'},inplace=True)
df.head()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > will explore and answer the research questions posed in the Introduction section,will compute statistics and produce visualizations.
# 
# 
# 

# **General data look**

# In[28]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.


# In[29]:


#exploring histogram data
df.hist(figsize=(15,11));


# **Histogram observation**
# 
# age: There are a lot of extremely young persons in the dataset, but the patients' ages are generally evenly distributed, and the number of patients sharply declines for patients above the age of 60.
# alcoholism: The majority of patients do not have alcoholism.
# diabetes: The majority of patients are not diabetes but more than alcoholics.
# handicap: The majority of the catogries does not fall under any of the handicap categories.
# hypertension: The majority of patients do not have hypertension diagnosed.
# sms_received: The majority of patients recieve sms.

# ### what are the variation of appointments with the malady?

# In[30]:


df.hist(figsize=(10,6), color='green',label='the variation of appointments with the malady', alpha=0.6)


# ### How much do handicap not show up?

# In[234]:


#how much handicap effect
df_handcap_noshow = df_noshow[['Handcap','No-show']]
df_handcap_noshow = df_handcap_noshow.loc[df_handcap_noshow['Handcap'] == 1.0]
df_handcap_noshow['No-show'] = df_handcap_noshow['No-show'].map(  {'Yes':1 ,'No':0}) 
df_handcap_noshow.groupby('No-show').count().plot(kind='barh',figsize=(5,4),title="Handicape not show up")
plt.xlabel('Number of No show ')
plt.ylabel('Handicape')
plt.show()


# Number of  handicaped do not miss appointments.

# ### Do SMS appoiments effect in fewer absences?

# In[235]:


df_sms_noshow = df_noshow[['SMS_received','No-show']]
df_sms_noshow = df_sms_noshow.loc[df_sms_noshow['No-show'] == 'Yes']
df_sms_noshow.groupby('SMS_received').count().plot(kind='barh',figsize=(5,4),title="SMS appoimnets")
plt.xlabel('Number of No show')
plt.show()


# The small difference between SMS_received indicates that SMS appoiments do not make a significant difference.

# ### Alcoholism causes more no-shows, or vice versa?

# In[9]:


df.shape


# In[11]:


df.groupby(["No-show", "SMS_received"]).size()


# 9784 patients showed up for their appointments, compared to 25698 individuals who did not.
# Patients' attendance at appointments was unaffected by receiving texts.

# <a id='conclusions'></a>
# ## Conclusions
# 
# I examined the dataset and fixed a few issues, including combining names, eliminating inaccurate data, and adding new features based on the data already present.The majority of the dataset's independent variables have also been looked into, and I've made a few observations comparing them to one another and to the dependent variable (no_show), as well. Most what are investigate:
# 
# >age: There are a lot of extremely young persons in the dataset, but the patients' ages are generally evenly distributed, and the number of patients sharply declines for patients above the age of 60.
# >alcoholism: The majority of patients do not have alcoholism.
# >diabetes: The majority of patients are not diabetes but more than alcoholics.
# >handicap: The majority of the catogries does not fall under any of the handicap categories.
# >hypertension: The majority of patients do not have hypertension diagnosed.
# >sms_received: The majority of patients recieve sms.
# 
# >When compared to all patients, gender doesn't significantly affect whether patients arrive for their appointments.
# >   Female have the maximum percentage of no-shows about 64%.
# > Both gender in general  are no_show about 20 %
# Appointment cancellations seem to be more common among certain age groups.
# 
# >Number of handicaped do not miss appointments
# 
# >9784 patients showed up for their appointments, compared to 25698 individuals who did not. Patients' attendance at appointments was unaffected by receiving texts.
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[15]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:





# In[ ]:




