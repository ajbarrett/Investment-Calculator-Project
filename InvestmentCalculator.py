#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 23:15:32 2019

@author: andre
"""
#A=Pe^(r*t)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/andre/Documents/Coding Garbage/prices.txt')
data.columns = ['price level (compared 2019 dollar)','year']
X=data['year'].values
y=data['price level (compared 2019 dollar)']

inflateVars=np.polyfit(X,y, 1, w=np.sqrt(y))
currYear=2019

p=0
e=2.7182818284590452353602874713526624
while(True):
    p=input("Enter initial investment amount. \n")
    try:
        p = float(p)
        break
    except ValueError:
        print("Please enter valid number")

r=0
while(True):
    r=input("Enter interest rate (in decimal form). \n")
    try:
        r = float(r)
        break
    except ValueError:
        print("Please enter valid number")
        
t=0
while(True):
    t=input("Enter number of years. \n")
    try:
        t = float(t)
        break
    except ValueError:
        print("Please enter valid number")

amount= p*(e**(r*t))
print("\nYour investment will be worth ${} after {} years. \n That is a ${}, or {}% increase!".format(amount,t,amount-p,(amount-p)*100/p))
# Pie chart
labels = ['Initial Investment', 'Interest']
sizes = [p/amount,(amount-p)/amount]
explode = (0, 0.1)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()

endYear=int(currYear+t)
#y=mx+b
m=inflateVars[0]
b=inflateVars[1]
inflateEquate= m*endYear + b

import seaborn as sb
sb.scatterplot(X,y)

purchasingPower=1/inflateEquate
adjustedAmount=amount*purchasingPower
adjustedP=p*purchasingPower
changeInPurchasingPower=100*(adjustedAmount-amount)/amount
changeInPurchasingPower=abs(int(changeInPurchasingPower))
print("The purchasing power of the dollar will likely decrease by about {}% by {}, making your investment worth ${} in today's market \n".format(changeInPurchasingPower,endYear,adjustedAmount))
print("However, by {}, your initial investment of ${} would only have the purchasing power of ${} in today's market. It's always smart to invest!".format(endYear,p,adjustedP))
