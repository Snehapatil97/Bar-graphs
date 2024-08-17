#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data for sales by region
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
sales_by_region = [350, 250, 400, 150, 200]

# Sample data for sales by product category
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys']
sales_by_category = [500, 300, 450, 200, 150]

# Sample data for employee distribution across departments
departments = ['Sales', 'Marketing', 'IT', 'HR', 'Finance']
employees_by_department = [40, 30, 25, 20, 35]

# Set the seaborn style for a nice look
sns.set(style="whitegrid")

# 1. Bar graph for sales by region
plt.figure(figsize=(8, 5))
sns.barplot(x=regions, y=sales_by_region, palette="husl")
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

# 2. Bar graph for sales by product category
plt.figure(figsize=(8, 5))
sns.barplot(x=categories, y=sales_by_category, palette="Set2")
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales')
plt.show()

# 3. Bar graph for employee distribution across departments
plt.figure(figsize=(8, 5))
sns.barplot(x=departments, y=employees_by_department, palette="Paired")
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




