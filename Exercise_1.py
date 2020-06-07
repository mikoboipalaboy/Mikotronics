# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:43:39 2020

@author: AcerUser
"""

import pandas as pd
import os


# Declare the path of the interface files %%
files = [file for file in os.listdir('C:/Users/AcerUser/Desktop/TestPyProject/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data')]

# Create blank data frame %%
all_months_data = pd.DataFrame()

# Reading all the interface files in the path %%
for file in files:
    df = pd.read_csv('C:/Users/AcerUser/Desktop/TestPyProject/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data, df])
    
all_months_data.to_csv("all_data.csv", index=False)

all_data = pd.read_csv("all_data.csv")

# Filter Blanks values in dataframe%%


all_data = all_data.dropna(how='all')

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Converting data types from Char to Numeric in the DF %%
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

# Create a new variable in the dataframe %%
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

# Calculations of Varaibles in the DF %%
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

# Calculations of Varaibles in the DF and groupy %%
all_data.groupby('Month').sum()

# Indexing to get a string %%
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

def get_zipcode(address):
    return address.split(',')[2].split(' ')[2]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) +  ' ' + get_state(x))

#all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})") ##

all_data['Zip Code'] = all_data['Purchase Address'].apply(lambda x: get_zipcode(x))

# Converting char to datetime feature %%
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute


# Duplicate validation %%
df_dup = all_data[all_data['Order ID'].duplicated(keep=False)]

df_dup['Items Ordered Together'] = df_dup.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df_dup = df_dup[['Order ID', 'Items Ordered Together']].drop_duplicates()

from itertools import combinations
from collections import Counter

count = Counter()

for row in df_dup['Items Ordered Together']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

for key, value in count.most_common(100):
    print(key,value)
    
prod_grp = all_data.groupby('Product')
quantity_ordered = prod_grp.sum()['Quantity Ordered']

Products = [Product for Product, df in prod_grp]
Prices = all_data.groupby('Product').mean()['Price Each']

# Print obs %%
df_dup.head(20)

# Graph report or plot %%
import matplotlib.pyplot as plt

results = all_data.groupby('Month').sum()
results = all_data.groupby('City').sum()

months = range(1,13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Months As of 2019')
plt.show()

# Graph report or plot %%
import matplotlib.pyplot as plt

results = all_data.groupby('Month').sum()
results = all_data.groupby('City').sum()

# Cities = all_data['City'].unique() ##
Cities = [city for city, df in all_data.groupby('City')]

plt.bar(Cities, results['Sales'])
plt.xticks(Cities, rotation='vertical', size=8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('US Cities Top Sales')
plt.show()

# Graph report or plot %%
import matplotlib.pyplot as plt

# Cities = all_data['City'].unique() ##
Hours = [Hour for Hour, df in all_data.groupby('Hour')]

plt.plot(Hours, all_data.groupby(['Hour']).count())
plt.xticks(Hours)
plt.xlabel('Best Time to Sell Products')
plt.ylabel('Number of Orders')
plt.grid()
plt.show()

# Graph report or    
import matplotlib.pyplot as plt 

Products = [Product for Product, df in prod_grp]


plt.bar(Products, quantity_ordered)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.xticks(Products, rotation='vertical', size=8)
plt.show()

# Graph report or    
import matplotlib.pyplot as plt

Products = [Product for Product, df in prod_grp]
Prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(Products, quantity_ordered, color='g')
ax2.plot(Products, Prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(Products, rotation='vertical', size=8)

plt.show()

py -3 --version



import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))