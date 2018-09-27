# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:44:27 2018

@author: cches
"""
import plotly.plotly as py
from plotly.figure_factory._county_choropleth import create_choropleth
import numpy as np
import pandas as pd

dffips = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/all-geocodes-v2016.csv')
#only three dataframes can be concat at a time
df2009 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2009%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2010 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2010%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2011 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2011%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2012 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2012%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2013 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2013%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2014 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2014%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2015 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2015%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2016 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2016%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2017 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2017%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df2018 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/Oil%20Spill%20Data%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products%20(H-8)/h8s-2018%20-%20Crude%20Oil%2C%20Gas%20Well%20Liquids%20or%20Associated%20Products.csv')
df1 = pd.concat([df2010, df2011, df2012], ignore_index=True)
df2 = pd.concat([df2013, df2014, df2015], ignore_index=True)
df3 = pd.concat([df2016, df2017, df2018], ignore_index=True)
df4 = pd.concat([df1, df2, df3], ignore_index=True)
df = pd.concat([df4, df2009], ignore_index=True)
df.to_csv(r'E:\Documents\Wild Catters\Data Analysis\Oil Spills\Data\Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)\rrc_spill_data.csv')

df['County'] = df['County'].str.lower()
dffips['County'] = dffips['County'].str.lower()
dffips['County'] = dffips['County'].str.replace(r' county', '')

dffips['fips_county'] = dffips['fips_county'].astype(str).str.zfill(3)
dffips['fips'] = dffips[['fips_state','fips_county']].astype(str).apply(lambda x: ''.join(x), axis=1)

df = df.merge(dffips)
df.to_csv(r'E:\Documents\Wild Catters\Data Analysis\Oil Spills\Data\Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)\rrc_spill_data_fips.csv')

df_fips = df.groupby(['fips'], as_index=False).sum()
df_fips.to_csv(r'E:\Documents\Wild Catters\Data Analysis\Oil Spills\Data\Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)\rrc_spill_data_fips-consolidated.csv')


colorscale = ['hsl(244.0, 100.0%, 86%)', 'hsl(244.0, 100.0%, 84%)', 
               'hsl(244.0, 100.0%, 82%)', 'hsl(244.0, 100.0%, 80%)', 
               'hsl(244.0, 100.0%, 78%)', 'hsl(244.0, 100.0%, 76%)', 
               'hsl(244.0, 100.0%, 74%)', 'hsl(244.0, 100.0%, 72%)', 
               'hsl(244.0, 100.0%, 70%)', 'hsl(244.0, 100.0%, 68%)', 
               'hsl(244.0, 100.0%, 66%)', 'hsl(244.0, 100.0%, 64%)', 
               'hsl(244.0, 100.0%, 63%)', 'hsl(244.0, 100.0%, 62%)', 
               'hsl(244.0, 100.0%, 61%)', 'hsl(244.0, 100.0%, 60%)', 
               'hsl(244.0, 100.0%, 59%)', 'hsl(244.0, 100.0%, 58%)', 
               'hsl(244.0, 100.0%, 57%)', 'hsl(244.0, 100.0%, 56%)', 
               'hsl(244.0, 100.0%, 55%)', 'hsl(244.0, 100.0%, 54%)', 
               'hsl(244.0, 100.0%, 53%)', 'hsl(244.0, 100.0%, 52%)', 
               'hsl(244.0, 100.0%, 51%)', 'hsl(244.0, 100.0%, 50%)', 
               'hsl(244.0, 100.0%, 49%)', 'hsl(244.0, 100.0%, 48%)', 
               'hsl(244.0, 100.0%, 47%)', 'hsl(244.0, 100.0%, 46%)', 
               'hsl(244.0, 100.0%, 45%)', 'hsl(244.0, 100.0%, 44%)', 
               'hsl(244.0, 100.0%, 43%)', 'hsl(244.0, 100.0%, 42%)', 
               'hsl(244.0, 100.0%, 41%)', 'hsl(244.0, 100.0%, 40%)', 
               'hsl(244.0, 100.0%, 39%)', 'hsl(244.0, 100.0%, 38%)', 
               'hsl(244.0, 100.0%, 37%)', 'hsl(244.0, 100.0%, 36%)', 
               'hsl(244.0, 100.0%, 35%)', 'hsl(244.0, 100.0%, 34%)', 
               'hsl(244.0, 100.0%, 33%)', 'hsl(244.0, 100.0%, 32%)', 
               'hsl(244.0, 100.0%, 31%)', 'hsl(244.0, 100.0%, 30%)', 
               'hsl(244.0, 100.0%, 29%)', 'hsl(244.0, 100.0%, 28%)', 
               'hsl(244.0, 100.0%, 27%)', 'hsl(244.0, 100.0%, 26%)', 
               'hsl(244.0, 100.0%, 25%)', 'hsl(244.0, 100.0%, 24%)', 
               'hsl(244.0, 100.0%, 23%)', 'hsl(244.0, 100.0%, 22%)', 
               'hsl(244.0, 100.0%, 21%)', 'hsl(244.0, 100.0%, 20%)', 
               'hsl(244.0, 100.0%, 18%)', 'hsl(244.0, 100.0%, 16%)', 
               'hsl(244.0, 100.0%, 14%)', 'hsl(244.0, 100.0%, 12%)', 
               'hsl(244.0, 100.0%, 10%)']

        
endpts = list(np.linspace(60, 6100, len(colorscale) - 2))
fips = df_fips['fips'].tolist()
values = df_fips['Net Loss'].tolist()
#x=values

fig = create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    round_legend_values=True,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    scope=['TX'], 
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    state_outline={'width': 3},
    asp=2.9, title='Oil Spills from 2009 to 2018',
    legend_title='Net spill Volume BBL')

#this puts them side by side.
#df['text'] = [str(a)+" District: "+str(b) for a,b in zip(df['number_of_oil_spills'], df['District'])]
#this doesnt work right, only shows for some counties, and shows the wrong numbers, doesnt remove fips

        
#hover_trace = [t for t in fig['data'] if 'text' in t][0]
#for i, label in enumerate(hover_trace['text']):
    # Remove FIPS
#    if(i<len(fips)):
#        new_label = label.replace("FIPS: %s<br>" % fips[i], "")

        # Add a new value
#        new_label +=  "<br>Num of Spills: %d" % df['number_of_oil_spills'][i]

        # Add a new value
#        new_label +=  "<br>District: %s" %df['District'][i]

        # Update trace text
#        hover_trace['text'][i] = new_label        

fig['layout']['legend'].update({'x': 0})
fig['layout']['annotations'][0].update({'x': -0.12, 'xanchor': 'left'})
py.plot(fig, filename='oil spill net loss (all years)')