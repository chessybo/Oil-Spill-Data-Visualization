# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:56:10 2018

@author: cches
"""
import pandas as pd

df2009 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2009%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2010 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2010%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2011 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2011%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2012 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2012%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2013 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2013%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2014 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2014%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2015 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2015%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2016 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2016%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2017 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2017%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2018 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/H8%20Loss%20Reports/h8s-2018%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df1 = pd.concat([df2010, df2011, df2012], ignore_index=True)
df2 = pd.concat([df2013, df2014, df2015], ignore_index=True)
df3 = pd.concat([df2016, df2017, df2018], ignore_index=True)
df4 = pd.concat([df1, df2, df3], ignore_index=True)
df = pd.concat([df4, df2009], ignore_index=True)


df_year = df.groupby('MasterYear')['Net Loss'].agg(['sum','count'])

dfproduction = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-Data-Visualization/master/production%20data/Crude%20Oil%20Production%20and%20Well%20Counts%20(raw%20source%20data)%20(since%201935).csv', encoding='utf8')

df_production_yr = df_year.merge(dfproduction, on='MasterYear')

df_production_yr['barrels of oil produced per barrel of net oil spilled annually(Lost)'] = df_production_yr['Crude Oil Production BBL']/df_production_yr['sum']
df_production_yr['barrels of oil produced per spill annually'] = df_production_yr['Crude Oil Production BBL']/df_production_yr['count']
#df_production_yr.to_csv(r'E:\Documents\Wild Catters\Data Analysis\Oil Spills\Data\Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)\rrc_spill_production_yr.csv')

import matplotlib.pyplot as plt
import numpy as np

annual = df_production_yr['MasterYear'].astype(int)
index = np.arange(len(annual))
ydata = df_production_yr['barrels of oil produced per barrel of net oil spilled annually(Lost)'] 
plt.bar(index, ydata, align='center')
plt.xticks(index, annual)
plt.ylabel('barrels of oil produced per barrel of net oil spilled')
plt.title('Barrels of Oil Produced per Barrel of Net Oil Spilled Annusally (Lost)')
plt.show()

annual = df_production_yr['MasterYear'].astype(int)
index = np.arange(len(annual))
ydata = df_production_yr['barrels of oil produced per spill annually'] 
plt.bar(index, ydata, align='center')
plt.xticks(index, annual)
plt.ylabel('barrels of oil produced per spill')
plt.title('Barrels of Oil Produced per Spill Annually')
plt.show()