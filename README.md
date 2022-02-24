# COVID-19 County Mask Mandate Analysis
*See Election2_dataset.ipynb, final.csv & covidRegressionandRF.ipynb*

## Team: Red Zone

**Members:** Jimmy Greer, Ben Altshuler, TeKisha Sampson &amp; Jason Goddard

**Comm Protocol:**
- Trello for PM, Slack, Group-Text, email
- Use one of the above as heads-up on working status, new branches, major commits, new files, pull requests, and merge conflicts

**Objective:** Did counties with mask mandates see fewer COVID-19 cases than those without?  Can we find other more relevant features that suggest a relation between factors and death rate?  The analysis will be based on the cases as a percentage of the population.  

**Intro Deck:** [Red Zone's COVID-19 Mask Mandate Intro](https://docs.google.com/presentation/d/16n0RSISNJ638HoVZlOlderMXyFtMTKz3fehBtG4oSqQ/edit#slide=id.p "Red Zone's COVID-19 Mask Mandate Intro") 

## ***Datasets***

| CSV | Keys | Summary |
| :---: | :---: | :---: |
| *POPULATION_TEST.csv* | FIPS | population in 2020 by county in the United States |
| *us-counties.csv* | FIPS | the cumulative daily 2020 cases and deaths by county taken on the last day of the year |
| *county_mask_mandate_data.csv* | county_fips state_fips | mask mandates in counties in the United States defined by whether a mask mandate was implemented | 
| *elec_results_2020.csv* | state_fips | designation of red/blue states by 2020 presidential election |


## ***Requirements***

Pandas, Matplotlib, Sklearn, PostgreSQL 13.x & Numpy

## ***EDA***
Most source data in csv format. Pandas reads in from the sources as separate dataframes before being cleaned and merged. The merge of county population takes place in SQL on the Postgres instance initiated by the user. Finally, a complete csv is passed to the ML segment. 

- **County Mask Mandate** <br>
&nbsp;&nbsp;-dropping multiple columns <br>
&nbsp;&nbsp;-*county_start_date* to 1 or 0 in new column <br>
&nbsp;&nbsp;-add column for duration 

- **US Counties** <br>
&nbsp;&nbsp;-dropping multiple columns <br>
&nbsp;&nbsp;-groupby *counties* to get sum of cases and deaths

- **Population Test** <br>
&nbsp;&nbsp;-concatenate state and county codes into *fips*


- **Election Results** <br>
&nbsp;&nbsp;-ETL strip <br>
&nbsp;&nbsp;-merge by category into County Mask Mandate data on *state_fips*

![alt_text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/READ.ME/Resources/FlowChart.png)

## ***SQL***

Merging on *fips* keys to bring in population in order to fairly measure features against the percentages of cases in counties.

*Note: while much of the merging was done in Python, the below shows a simple ERD of the mapping that we could work from throughout.*  
![alt text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/READ.ME/database_covid_rev2.png)

## ***Machine Learning***
*See covidRegressionandRF.ipynb* <br>
Using a classification model, **Logistic Regression**, we'd like to see if we can predict the likelihood of infection in a county with a mask mandate.  We'd like to pinpoint correlation by adding population size & 2020 presidential election results as features.  Because of the manageable size of the data, we believe that we can employ Logistic Regression from the start.  

*Logistic Regression Classification Reports:* <br>

![alt text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/READ.ME/Resources/ClassReport.png) <br>

As you can see, with high f1-scores across the bins and a accuracy rate of 92.9%, this would be a good predictive model given that we have the mask mandate, Blue/Red State status and the population of a given county.  

Additionally, we ran a **Random Forest** model.  With an f1-score of .60, we would lean towards the **Logistic Regression** above.  

## ***Additonal Analysis***
To narrow down the causation, we took a simple approach with **linear association**.  The results closely matched what we perceived in the data visualization and gave insight into the driving feature in the dataset (mask mandate).  

![alt text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/READ.ME/Resources/CaseCorr.png)
![alt text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/READ.ME/Resources/DeathCorr.png)

## ***Dashboard***

[2020 COVID-19 Analysis.  Cases, Deaths & Mandates via Tableau](https://public.tableau.com/app/profile/jason.goddard/viz/COVID-19MaskMandateFP/Story1?publish=yes "Red Zone's COVID-19 Mask Mandate Intro")

*Consider:* <br>
&nbsp;&nbsp;-Filtering *Mask Mandates* map down to 0-5% as well as 10-29% <br>
&nbsp;&nbsp;-Highlighting *Case %* and *Death %* maps by mask mandate  <br>

These visualizations tell a story that aligns with the data analysis.  

## ***Exported CSV***
- *final.csv* <br>
&nbsp;&nbsp;-via *Election2_dataset.ipynb* <br>

