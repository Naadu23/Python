#!/usr/bin/env python
# coding: utf-8

# ### Q1
# List the basic data types in python and give one example each.

# **Integer**  
# Example is 100
# 
# **Float**  
# Example is 55.9
# 
# **Boolean**  
# Example is TRUE
# 
# **String**  
# Example is "Naa"

# ### Q2
# Change the variable x = 4539.85 to :
# 
# (i) a string and assign it to a new variable y,
# 
# (ii) an integer and assign it to a new variable z
# 
# Print out the type of y and z.

# In[11]:


#Create variable
x = 4539.85

#Change to string
y = str(x)

#Change to integer
z = int(x)

#Show data type of variables
print(type(y))
print(type(z))


# ### Q3
# 
# What data type would you use to store
# 
# a. The price of car?  
# **Answer** : Float  
# 
# b. The age of a person  
# **Answer** : Integer
# 
# c. car plate number: plateNumber = "AV01-AFP"?  
# **Answer** : String
# 
# d. The price of fuel  
# **Answer** : Float
# 
# e. The number of students in the class  
# **Answer** : Integer
# 
# f. The weight of a person  
# **Answer** : Float
# 
# g. Check whether two figures are equal  
# **Answer** : Boolean
# 
# i. The name of a  school  
# **Answer** : String
# 
# j. The average result of the overall score of a student  
# **Answer** : Float
# 
# k. The total number of vote cast  
# **Answer** : Integer
# 

# ### Q4
# **Thomas Partey is arguably the best player in the Black Stars. He is a great addition to the team**
# 
# Split the statement above into **two statement_1** and **statement_2** such that statement_1 will be 'Thomas Partey is arguably the best player in the Black Stars' and statement_2 will be 'He is a great addition to the team'
# 
# Statement: 
# 
# - **What is the length of statment 1?**
# -**What is the length of statment 2?**
# -**Is the length of statement 1 greater than statement 2**

# In[21]:


#Create a variable
statement = str("Thomas Partey is arguably the best player in the Black Stars. He is a great addition to the team")

#Split the string by a delimeter
statements = statement.split(". ")

#Create variables to store the parts using the index
statement_1 = statements[0]
statement_2 = statements[1]

#Show
print(statement_1)
print(statement_2)

#length of string
a = len(statement_1)
print(a)

b = len(statement_2)
print(b)

#Check if the length of statement 1 greater than statement 2
c = a > b
print(c)


# ### Q5
# What values does python use to represent **True** and **False** respectively?  
# 
# **Answer**: 1 and 0 respectively

# ### Q6
# Write a code to evaluate if the following statments are True or False.
# 
# 1. 78 is greater than 46 and less than 30 which is an odd number.
# 
# 2. 8-2 is an even number or 8 is a is an odd number.
# 
# 3. The number of characters in the word 'boostrap' is 7 and that of 'sample' is 6.

# In[30]:


#Create variables
a = 78
b = 46
c = 30

#Check if 78 is greater than 46 and less than 30 which is an odd number
Question_1 = (a > b) and (a < c) and (c % 2 != 0)
print(Question_1)

#Create variables
d = 8
e = 2

#Check if 8-2 is an even number or 8 is a is an odd number
Question_2 = (d - e) % 2 == 0 or d % 2 != 0
print(Question_2)

#Create variables
text1 = "bootstrap"
text2 = "sample"

#Check if the number of characters in the word 'boostrap' is 7 and that of 'sample' is 6.
Question_3 = len(text1) == 7 and len(text2) == 6
print("Statement 3 is", Question_3)


# ### Q7
# Given the following python code,
# 
# `word='Hello, How are you?'`
# 
# Write Python code to return the following
# 
# - How
# - How are you
# - are
# - ?
# - Hello, How are you
# 
# 
#  

# In[44]:


#Create a variable
word = "Hello, How are you ?"

#Split the string
words = word.split(" ")
print(words)

string1 = words[1]
print(string1)

string2 = ' '.join(words[1:4])
print(string2)

string3 = words[2]
print(string3)

string4 = words[4]
print(string4)

string5 = ' '.join(words[0:4])
print(string5)


# ### Q8
# Given the following python code,
# 
# `sentence = "I am very excited"`
# 
# Write Python code to return 
# - Convert sentence to upper case
# - Convert sentence to lower case
# - Convert sentence to title case
# - Convert sentence to list of strings
#  

# In[49]:


#Create variable
sentence = "I am very excited"
print(sentence)

#Convert sentence to upper case
upper_case_sentence = sentence.upper()
print(upper_case_sentence)

#Convert sentence to lower case
lower_case_sentence = sentence.lower()
print(lower_case_sentence)

#Convert sentence to title case
title_case_sentence = sentence.title()
print(title_case_sentence)

#Convert sentence to list of strings
stringlist = sentence.split()
print(stringlist)


# ### Q9
# `word = 'OneThirtyEight'`
# 
# Using Python code extract the following from the variable word:
# - One
# - Thirty
# - Eight
# - OneThirty
# - ThirtyEight
# - ONETHIRTYEIGHT

# In[57]:


word = "OneThirtyEight"
B1 = word[0:3]
print(B1)

B2 = word[3:9]
print(B2)

B3 = word[9:]
print(B3)

B4 = word[0:9]
print(B4)

B5 = word[3:]
print(B5)

B6 = word.upper()
print(B6)


# ### Q10
# Turn Ault'Kelly into a string and assign it to a variable  called name.

# In[58]:


name = "Ault'Kelly"
print(type(name))

