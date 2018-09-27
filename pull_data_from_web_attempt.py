# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:51:24 2018

@author: cches
"""

#import fips geocodes from government website
dffipsxsl = pd.read_excel('https://www2.census.gov/programs-surveys/popest/geographies/2016/all-geocodes-v2016.xlsx')

#wrangle fips data
dffipsxsl.to_csv('dffips.csv', encoding='utf-8', index=False)
dffips = pd.read_csv('dffips.csv', encoding='utf-8')
dffips = dffips.drop([0, 1, 2])
dffips.columns = dffips.iloc[0]
dffips = dffips.drop(3)
dffips = dffips.drop(columns=['Summary Level', 'County Subdivision Code (FIPS)', 'Place Code (FIPS)', 'Consolidtated City Code (FIPS)'])
new_columns = dffips.columns.values
new_columns[0] = 'fips_state'
new_columns[1] = 'fips_county'
new_columns[2] = 'County'
dffips.columns = new_columns

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

df['County'] = df['County'].str.lower()
dffips['County'] = dffips['County'].str.lower()
dffips['County'] = dffips['County'].str.replace(r' county', '')

dffips['fips_county'] = dffips['fips_county'].astype(str).str.zfill(3)
dffips['fips'] = dffips[['fips_state','fips_county']].astype(str).apply(lambda x: ''.join(x), axis=1)

df = df.merge(dffips)

df_fips = df.groupby(['fips'], as_index=False).sum()
