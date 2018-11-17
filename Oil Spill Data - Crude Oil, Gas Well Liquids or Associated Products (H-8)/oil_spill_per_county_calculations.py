# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:55:41 2018

@author: cches
"""
import pandas as pd
tbl = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/county_name%20%26%20Net%20Loss.csv')

tbl = tbl.groupby(['county_name'],as_index = False).sum()



tbl.to_csv('county and net loss (grouped).csv')


tbl2 = pd.read_csv('https://raw.githubusercontent.com/chessybo/Oil-Spill-map/master/RRC_Spill_table/county_name%20%26%20fips%20%26%20net%20loss%20(ordered%20by%20district).csv')
#tbl2 = tbl2.groupby(['county_name', 'District', 'fips'],as_index = False).sum()



#tbl2.to_csv('county_name & fips & net loss (ordered by district & grouped).csv')


#tabl3 = tbl2.groupby('county_name', 'District', 'fips')['Net Loss'].agg(['sum','count'])

#tbl2.groupby('county_name', 'District', 'fips').agg({'Net Loss': ['sum','count']})




num_oilspills = tbl2.fips.value_counts()


tbl3 = tbl2.groupby(['county_name', 'District', 'fips'],as_index = False).agg({'Net Loss': ['sum','count']})

after i saved this i reorded the table by district
#tbl3.to_csv('county_name & fips & net loss & count (ordered by district & grouped).csv')
