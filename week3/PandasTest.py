# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:05:25 2021

@author: Alvin
"""
import pandas as pd

# In[1]
Rows = ["Row1", "Row2", "Row3"]
Columns = ["Column1", "Column2"]

dfList = pd.DataFrame([[1, 2], [3, 4], [5, 6]], index=Rows, columns=Columns)
print(dfList)

dfDict = pd.DataFrame({"Column1": [1, 3, 5], "Column2": [2, 4, 6]}, index=Rows)
print(dfDict)

# In[2]
dfCSV = pd.read_csv("CarSales.csv")
print(dfCSV)

print(dfCSV["Country"].mode())
print(dfCSV["Age"].median())
print(dfCSV["Salary"].mean())

# In[3]
dfHTML = pd.read_html("http://www.stockq.org/market/asia.php")

asia_stocks = dfHTML[7].iloc[2:, :6]  # 欄位index 不包含上界 
# asia_stocks = dfHTML[7].loc[2:, :5]  # 欄位名稱 包含上界
print(asia_stocks)

# In[4]
ary = asia_stocks.to_numpy()
# ary = asia_stocks.values  # same as last line
print(ary)

# In[5]
stocks_table = dfHTML[7].loc[2:, [0, 1, 2, 4, 5]]
condition = stocks_table[2].astype('float64') > 0
print(stocks_table[condition])