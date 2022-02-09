# COVID Mandated County Analysis

## Team: Red Zone

**Members:** Jimmy Greer, Ben Altshur, TeKisha Sampson &amp; Jason Goddard


**Objective:** Did counties with mask mandates see fewer COVID-19 cases / deaths than those without?  The analysis will be a function of the cases / deaths as a percentage of the population.  

## ***Data Sets***
*co-est2020.csv:*   population in 2020 by county in the United States <br>
*us-counties.csv:*  the cumulative daily 2020 cases and deaths by county taken on the last day of the year <br>
*county_mask_mandate_data.csv:*   mask mandates in counties in the United States defined by whether a mask mandate was implemented <br>
*elec_results_2020.csv:*.  designation of red/blue states by 2020 presidential election 

## ***EDA***
Pandas used to clean datasets.

- County Mask Mandate <br>
&nbsp;&nbsp;-dropping multiple columns <br>
&nbsp;&nbsp;-*county_start_date* to 1 or 0 <br>
&nbsp;&nbsp;-add column for duration 

- US Counties <br>
&nbsp;&nbsp;-dropping multiple columns <br>
&nbsp;&nbsp;-groupby *counties* to get sum of cases and deaths

- Co Est2020 <br>
&nbsp;&nbsp;-concantenate state and county codes into *fips*

- Election Results <br>
&nbsp;&nbsp;-merge by category into County Mask Mandate data on *state_name*

## ***SQL***

Merging on *fips*

## Machine Learning
We will cluster counties based on mandate and deaths using **(a Classification model / Logistical Regression TBD)** in an effort to see how communties fared across the state (does the data group by **state (string would have to be converted (perhaps red/blue on last election, east/west or size on median)** or county size, or were the counties simply grouped by the mandate).  Because of the manageable size of the data, we believe that we can employ **(TBD)** from the start.  

## Exported CSV
