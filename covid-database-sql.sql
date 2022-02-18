SELECT

fmdll.state_fips,
fmdll.state_name_x,
fmdll.fips, 
fmdll.county_name_x,
fmdll.mask_mandate,
fmdll.month_started,
fmdll.mandate_duration_months,
fmdll.date,
fmdll.county,
fmdll.state,
fmdll.cases,
fmdll.deaths, 
pt.popestimate2020,
fmdll.lat,
fmdll.lng

INTO county_pop_loc_sqlmerge

FROM fmdll
LEFT JOIN pt
ON fmdll.fips = pt.fips;