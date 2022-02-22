# COVID-19 County Mask Mandate Analysis

## Team: Red Zone

**Members:** Jimmy Greer, Ben Altshur, TeKisha Sampson &amp; Jason Goddard


**Objective:** Did counties with mask mandates see fewer COVID-19 cases / deaths than those without?  Can we find other more relevant features that suggest a relation between factors and death rate?  The analysis will be a function of the cases / deaths as a percentage of the population.  

**Intro Deck:** [Red Zone's COVID-19 Mask Mandate Intro](https://docs.google.com/presentation/d/16n0RSISNJ638HoVZlOlderMXyFtMTKz3fehBtG4oSqQ/edit#slide=id.p "Red Zone's COVID-19 Mask Mandate Intro") 

## ***Datasets***

| CSV | Keys | Summary | *OTHER?* | 
| :---: | :---: | :---: | :---: | 
| *co-est2020.csv* | FIPS | population in 2020 by county in the United States | XXX | 
| *us-counties.csv* | FIPS | the cumulative daily 2020 cases and deaths by county taken on the last day of the year | XXX | 
| *county_mask_mandate_data.csv* | county_fips state_fips | mask mandates in counties in the United States defined by whether a mask mandate was implemented | XXX | 
| *elec_results_2020.csv* | state_fips | designation of red/blue states by 2020 presidential election | XXX | 


## ***Requirement***

BEN A : Panda, Python, Tableau.... 

## ***EDA***
Pandas used to clean datasets.

- **County Mask Mandate** <br>
&nbsp;&nbsp;-dropping multiple columns <br>
&nbsp;&nbsp;-*county_start_date* to 1 or 0 <br>
&nbsp;&nbsp;-add column for duration 

- **US Counties** <br>
&nbsp;&nbsp;-dropping multiple columns <br>
&nbsp;&nbsp;-groupby *counties* to get sum of cases and deaths

- **Co Est2020** <br>
&nbsp;&nbsp;-concantenate state and county codes into *fips*


- **Election Results** <br>
&nbsp;&nbsp;-ETL strip <br>
&nbsp;&nbsp;-merge by category into County Mask Mandate data on *state_fips*

![alt_text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/READ.ME/Resources/Flow_Chart.png)

## ***SQL***

Merging on *fips* keys

*While much of the merging was done in Python, the below shows a simple ERD of the mapping that we could work from.*  
![alt text](https://github.com/Jimmygjr10/Covid19_Mask_Mandate/blob/main/database_covid_rev2.png)

## ***Machine Learning***
We will cluster counties based on mandate and deaths using a classification model, Logistic Regression, in an effort to see how communties fared across the state (does the data group by **state (string would have to be converted (perhaps red/blue on last election, east/west or size on median)** or county size, or were the counties simply grouped by the mandate).  Because of the manageable size of the data, we believe that we can employ **(TBD)** from the start.  


We ran Logistical Regression on *Deaths* and *Cases*, and as expected Cases made more sense for our research and our goals.  

## ***Additonal Analysis***
Without an accurate Machine Learning model, we took a more simplified approach with linear association.  The results closely matched what we perceived in the data visualization.  

![alt text]()
![alt text]()

## ***Dashboard***

[2020 COVID-19 Analysis.  Cases, Deaths & Mandates via Tableau](https://public.tableau.com/app/profile/jason.goddard/viz/COVID-19MaskMandateFP/Story1?publish=yes "Red Zone's COVID-19 Mask Mandate Intro")

## ***Exported CSV***
- *POPULATION_TEST.csv* <br>
&nbsp;&nbsp;-via XXXX <br>

- *mega_merged_df.csv* <br>
&nbsp;&nbsp;-via XXX 
