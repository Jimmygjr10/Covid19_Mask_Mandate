# %%
import pandas as pd
import datetime as dt
df = "Resources/us-counties.csv"
df1 = pd.read_csv(df)
file = "Resources/county_mask_mandate_data.xlsx"
df2 = pd.read_excel(file)

# %% [markdown]
# ## Read in Both Datasets

# %%
df1.head()

# %%
#Shows the data types for the df1
df1.dtypes

# %%
# count the number of rows with empty columns
count = df1['fips'].isna().sum()
print(count)

# %%
#count the number of rows with data in each column
df1.count()

# %%
# Drop the rows with blank data creating a new dataframe
df1_clean = df1.dropna()

# %%
# count the number of rows with data in each column from the clean dataframe
df1_clean.count()

# %%
#change fips from float64 to int64 to match datatype of df1_clean "county_fips"
df1_clean['fips'].astype('int64')

# %%
# change deaths from float64 to int64 to match datatype of df1_clean "deaths"
df1_clean['deaths'].astype('int64')

# %%
df1_clean['cases'].astype('int64')

# %%
# Group by county to get the total_cases for each county, read the last day of 2020 as the total number of cases and deaths
df1_total = df1_clean.loc[df1_clean['date'] == "2020-12-31"]
df1_total.head()

# %%
# Drop duplicates so only county shows once
df1_total = df1_total.drop_duplicates(subset=["fips"])
df1_total.head()

# %%
df1_total.describe

# %% [markdown]
# ## DataSet 2 Mask Mandate

# %%
df2.head()

# %%
df2.dtypes

# %%
df2.count()

# %%
# Drop the unneeded columns 
df2_clean1 = df2.drop(['escalation', 'defiance', 'county_conditions', 'county_source', 'county_start_edate', 'state_start_edate', 'earliest_start_edate', 'county_fips_string', 'state_conditions', 'state_source'], axis=1)

df2_clean1.head()

# %%
# Create our mask_mandate column with binary values Yes or No
no_mandate_df = df2_clean1[df2_clean1.county_start_date.isnull()]
mandate_df = df2_clean1[df2_clean1.county_start_date.notnull()]

# %%
# Create mask_mandate column
no_mandate_df["mask_mandate"] = "0"
mandate_df["mask_mandate"] = "1"
merged_df = no_mandate_df.append(mandate_df)

# %% [markdown]
# Show duration of mask mandate in 2020 only

# %%
# Create a null and not null dataset based on county start date
duration_df = merged_df[merged_df.county_start_date.notnull()]
duration_df1 = merged_df[merged_df.county_start_date.isnull()]
# Create a column that keeps up with month started 
duration_df['month_started'] = pd.DatetimeIndex(duration_df['county_start_date']).month
duration_df1['month_started'] = "0"


# %%
# Create a new column that is the difference between month started and total months in a year
duration_df["mandate_duration_months"] = (12 - duration_df.month_started)
duration_df1["mandate_duration_months"] = 0
final_df = duration_df.append(duration_df1)

# %%
final_df

# %% [markdown]
# Attempting Outer Merge on FIPS number

# %%
final_df_fips = final_df.rename(columns={'county_fips': 'fips'})

final_df_fips.dtypes

# %%
final_df_fips.duplicated(subset='fips')

# %%
final_df_fips.dtypes

# %%
df1_total.dtypes

# %%
df1_total.astype({'fips': 'int64'}).dtypes

# %%
final_df.head

# %%
## full_merged_df = final_df_fips.join(df1_total, on='fips')

full_merged_df = pd.merge(final_df_fips, df1_total, on='fips', how='outer')
full_merged_df


# %%
##full_merged_df.to_csv('full_merged_df.csv', index=False)

# %% [markdown]
# Joining Full Df with Population csv

# %%
population_df = pd.read_csv('POPULATION_TEST.csv')
population_df.head()


# %%
population_df = population_df.rename(columns={'FIPS': 'fips'})

# %%
##NEED TO ENABLE THIS MERGE
##full_merged_df['fips'].isin(population_df['fips']).value_counts()

# %%
## Join the population df with the merged_final for a mega_dataframe

mega_merged_df = pd.merge(full_merged_df, population_df, on='fips', how='outer')



# %%
mega_merged_df.head()

# %%
## mega_merged_df.to_csv('mega_merged_df.csv')

# %% [markdown]
# ## Join ELECTION CSV

# %%
# Read in election csv
csv =  "Resources/elec_results_2020.csv"
elec_df = pd.read_csv(csv)
elec_df.head()

# %%
elec_df.state_name.dtype

# %%
# Turn dataframe into a dictionary
election_series = elec_df[["state_name", "red_blue_2020"]]
key_value = election_series.set_index('state_name')['red_blue_2020'].to_dict()
print(key_value)

# %%
# Map the value of dictionary to mega_merged_df 1 for Rep 0 for Dem
mega_merged_df["elec_result"] = mega_merged_df["state_name"].map(key_value)

# %%
# Show merged_df with elec results
mega_merged_df.head()



