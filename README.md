# Oil Spill Data Visualization

This project takes [data collected](http://www.rrc.state.tx.us/about-us/resource-center/research/online-research-queries/) in Texas and/or the [Permian Basin](https://upload.wikimedia.org/wikipedia/en/4/4e/Active_wells_on_the_Permian_Basin.jpg) (This includes Oil & Gas Districts 8, 8A, & 7C) by the Texas Rail Road Commission through various reports oil & gas companies are obligated to submit. 


## Insights
- [a map of volume and number of oil spills by county](presentable/oil_spill_net_loss_2009_2018.png) [(interactive)](https://plot.ly/~chessybo/12/oil-spills-from-12116-51418/)
- [Annual Number of Operators in the Permian Basin](<presentable/Number of Operators Annually in the Permian Basin.png>) 
- [Oil Produced vs Oil Spilled](presentable/Oil_Produced_vs_Oil_Spilled.png)
- [Average Size of Oil Spills](presentable/oil_spills.png) and their [Causes](presentable/oil_spill_causes.png)


## Data Sources
- [Annual Number of Operators in Permian Basin](<production data/anuual_Operators_by_District.xlsx>): Texas Rail Road Commission Oil & Gas Data Query - [General Production Query](http://webapps2.rrc.texas.gov/EWA/productionQueryAction.do) 
  - Searching the production data by year long intervals for each district  ([8](https://github.com/chessybo/Oil-Spill-Data-Visualization/tree/master/production%20data/District%208), [8A](https://github.com/chessybo/Oil-Spill-Data-Visualization/tree/master/production%20data/District%208A), & [7C](https://github.com/chessybo/Oil-Spill-Data-Visualization/tree/master/production%20data/District%207C)), one can see the [number of operators producing oil in a given year](<production data/anuual_Operators_by_District.xlsx>).
- [a map of volume and number of oil spills by county](plot_rrc_data.py): Texas RRC - [Crude Oil, Gas Well Liquids or Associated Products (H-8) Loss Reports](http://www.rrc.state.tx.us/oil-gas/compliance-enforcement/h-8/)
  -	[Code](<Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)/oil_spill_per_county_calculations.py>) to determined the [oil spill data](<Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)/oil_spill_per_county.csv>) for each county.
- [Oil Produced vs Oil Spilled](oil_produced_and_oil_spilled.py): Texas Rail Road Commission - [Crude Oil Production and Well Counts (since 1935)](http://www.rrc.state.tx.us/oil-gas/research-and-statistics/production-data/historical-production-data/crude-oil-production-and-well-counts-since-1935/)
- [Average Size of Oil Spills and their Causes](<Oil Spill Data - Crude Oil, Gas Well Liquids or Associated Products (H-8)/oilspill_data_analysis.xlsx>): Texas Rail Road Commission - [Crude Oil, Gas Well Liquids or Associated Products (H-8) Loss Reports](http://www.rrc.state.tx.us/oil-gas/compliance-enforcement/h-8/)


## Future Work
annual water injected: an analysis of cumulative, "H-10 Annual Disposal/Injection Well Monitoring Reports" of all operators would provide a market insight as to the demmand for water treatment systems. This would require a data extraction method to pull the data from the individual H-10 reports on the [RRC website](http://webapps.rrc.state.tx.us/H10/h10PublicMain.do) that are in PDF format. However, the Texas RRC [states](http://www.rrc.state.tx.us/about-us/resource-center/research/online-research-queries/), 
> If the query system detects that data is being retrieved using an automated tool, the Railroad Commission of Texas will end the session for that user.

Total number of unique operators to ever operate in the permian basin: such a figure would be simple to produce, using the operator


a map of volume and number of oil spills by county: an analysis could be furthered by determining which county has the largst/smallest sized oil spills.

(wasnt there somethigns i wanted like the spills per operator?)

## Comments
This is an original data analysis of this Texas Rail Road Commission data. The reason this analysis has not been done previously is likely due to the limited scope of the available data compared to other states such as Oklahoma with stricter reporting and better data management [citation]

*UPDATE: a company had done similar work to that contained in this project. they collected data unstructed data such as injection volume data (Report W-14) manually from the RRC database (yes it took them a long time). However due to a lack in demmand the discontinued the work and pursued an alternate direction.

