#Importing the library and the dataset

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
data=pd.read_csv(r"C:\Users\GREAT\Documents\bike_sheet.csv")

data

data.head(2)

data.shape

#checking the total null value in the dataset

data.isnull().sum()
#checking the statical summary

data.describe()
#names of the column

data.columns
#sales by year

Sales_by_Year=data.groupby('Year')['Total_Sales'].sum()
Sales_by_Year
#Graphical representation of sales by year

Sales_by_Year.plot(kind='line',figsize=(6,4))
#sales by product categories

Sales_by_Pro_Cat=data.groupby('Product_Category')['Total_Sales'].sum()
Sales_by_Pro_Cat
#pie chart graphical representation of sales by product category

plt.pie(Sales_by_Pro_Cat,labels=Sales_by_Pro_Cat.index,autopct="%1.1f%%")
#sales by country

Sales_by_Country= data.groupby('Country')['Total_Sales'].sum()
Sales_by_Country
#Graphical representation for sales by country

Sales_by_Country.plot(kind='bar',figsize=(5,3))
#profit trend by Year

Profit_by_year = data.groupby('Year')['Profit'].sum()
Profit_by_year

#graphical represetation of profit by year

Profit_by_year.plot(kind='line',figsize=(7,5))
# gender distribution 

data.Customer_Gender.value_counts()
#quantities by gender

data.groupby('Customer_Gender')['Order_Quantity'].sum()
data.head(2)
#quantities sold to male by year

male=data[(data.Customer_Gender=='M')&(data.Order_Quantity>0)][['Year','Order_Quantity']]
male=male.groupby('Year').count().reset_index()
male

#quantities sold to female by year

female=data[(data.Customer_Gender=='F')&(data.Order_Quantity>0)][['Year','Order_Quantity']]
female=female.groupby('Year').count().reset_index()
female
#checking the list of countries
data.Country.unique()
#total quantity in canada by year

canada=data[(data.Country=='Canada')&(data.Order_Quantity>0)][['Year','Order_Quantity']]
canada=canada.groupby('Year').count().reset_index()
canada
#total quantity in Australia by year

Australia=data[(data.Country=='Australia')&(data.Order_Quantity>0)][['Year','Order_Quantity']]
Australia=Australia.groupby('Year').count().reset_index()
Australia
#total quantity in United State by year

USA=data[(data.Country=='United States')&(data.Order_Quantity>0)][['Year','Order_Quantity']]
USA=USA.groupby('Year').count().reset_index()
USA
data.head(2)
#Top ten product by quantity order

Top_10_Product = data.groupby('Product')['Order_Quantity'].sum().head(30).sort_values(ascending=False).head(10)
Top_10_Product
# graphical representation of top ten product

Top_10_Product.plot(kind='bar',figsize=(5,3))
data.head(2)
#Top ten product in canada base on sales

Canada=data.query('Country=="Canada"')
Canada.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
#Top ten product in Australia base on sales

Australia=data.query('Country=="Australia"')
Australia.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
#Top ten product in Germany base on sales

Germany=data.query('Country=="Germany"')
Germany.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
#Top ten product in France base on sales

France=data.query('Country=="France"')
France.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)