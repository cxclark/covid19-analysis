<img src="/img/intro.png">

---
# Table of Contents
- [Problem Statement](#Problem-Statement)
- [Executive Summary](#Executive-Summary)
- [Models Summary](#Models-Summary)
- [Key Challenges](#Key-Challenges)
- [Interactive Demo](#Interactive-Demo)
- [Conclusions](#Conclusions)
- [Future Work](#Future-Work)
- [References and Data Sources](#References-and-Data-Sources)
- [Data Dictionary](#Data-Dictionary)

# Problem Statement
Is it possible to predict COVID-19 severity using demographic data?

Studies have indicated that COVID-19 affects parts of the population more severely, such as older individuals and males <sup>[1,2]</sup>. At the same time, the World Health Organization has stated that lockdowns and other restrictive measures meant to stop the spread of the virus "can have a profound negative impact on individuals, communities, and societies by bringing social and economic life to a near stop." <sup>[3]</sup>

Though COVID-19 research is ongoing, an analysis of COVID mortality and/or case rates in combination with demographic data might provide insights into communities more or less at risk.  These insights might enable more targeted measures commensurate with a specific community's risk, thus improving the welfare of all involved.

# Executive Summary

This analysis examines county-level COVID-19 testing, case, and death data alongside county-level demographic data for five US states. Demographic data such as age, gender, race, and income per capita is collected using the U.S. Census Bureau's API. COVID-19 and other health data is gathered from the CDC and state-specific health departments.

The data is cleaned, pre-processed, and normalized for population. Features for modeling are evaluated and selected. Regression models are built to predict cases/100 people. Classification models are built to predict a class of COVID severity based on cases/100 people.

Data is modeled across five states and for each state individually. Conclusions are drawn. Possible next steps for further modeling are discussed.

# Models Summary

#### Modeling Notebooks
- [Modeling all five States](/code/06_modeling_five_states.ipynb)
- [California data modeling](/code/07_modeling_ca.ipynb)
- [Florida data modeling](/code/07_modeling_fl.ipynb)
- [Illinois data modeling](/code/07_modeling_il.ipynb)
- [New York data modeling](/code/07_modeling_ny.ipynb)
- [Texas data modeling](/code/07_modeling_tx.ipynb)

We weren't able to achieve high accuracy when we used all five states data for modeling, however, the models performed significantly better in some cases when we used state-level data for our of our models.

This variation in models' predictive accuracy between all five states and state level data can be explained by data variation from one state to another, which eventually led to disparities between state-level models in terms of predictive features importance. For instance, population density and income per capita were the two most important features in our model using data from all five states, but other features like race percentage, age groups percentage, and having health insurance were more important in models using state-level data.

| Region             | Best Regression R2 | Best Classification Accuracy | Classification Baseline |
|--------------------|--------------------|------------------------------|-------------------------|
| CA, FL, IL, NY, TX | 47%                | 63%                          | 42%                     |
| California         | 75%                | 93%                          | 66%                     |
| Florida            | 76%                | 71%                          | 71%                     |
| Illinois           | 32%                | 73%                          | 54%                     |
| New York           | 81%                | 94%                          | 81%                     |
| Texas              | 49%                | 59%                          | 40%                     |

# Key Challenges

- **COVID is an ongoing event.**
With more data being collected everyday, we are improving our understanding on how different states and counties are affected by COVID. We will try to improve our models' performance in the future as more data becomes available.

- **Widley varying state-level data.**
As we mentioned earlier, we noticed that data varies widely on state-level, which explaines why our state-level models performed better than our models using all five states data for the most part.

- **More features are needed.**
There are other factors which we didn't investigate in our models that might also be important to predict COVID severity, such as county mask wearing policies and the percentage of people wearing masks in each counties. 

# Interactive Demo

We utilized [Folium](https://python-visualization.github.io/folium/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/) to build an interactive demo app.

You can select any of the five states in the home page for a county-level visualization of COVID severity.

<img src="/img/homepage.png" width="500">

>In the image below, Texas counties are highlighted with three different shades of red that range from light to dark as COVID severity increases. 

<img src="/img/tx.png" width="500">

>When hovering overa county within the app, a window appears with a detailed breakdown of county-level demographic factors that contribute to COVID severity score.

<img src="/img/txhover.png" width="500">

>Finally, we included a predictive model that you can use to predict COVID severity for other counties in the United States.

<img src="/img/demo.png" width="425">

*In order to use our interactive demo, please download the github repo and run `app2.py` file in the [Flask](../Flask) folder.*

# Conclusions

- Demographic data can explain some of the variability in when predicting COVID severity in different US counties.
- Population density and income per capita were the two strongest predictive features we using data from all five states.
- Other predictive features were more important on a state-level, such as race, age, and having health insurance.

# Future Work

This work could be improved in the future through the following: 
- Gathering more data for both these state and others.
- Updating the interactive app to include new data and states.
- Including additional features likely to impact COVID severity in the model.

# References and Data Sources
### References
1: [Why does COVID-19 disproportionately affect older people?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7288963/)  
2: [Coronavirus: Why Men are More Vulnerable to Covid-19 Than Women?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7271824/)  
3: [Coronavirus disease (COVID-19): Herd immunity, lockdowns and COVID-19](https://www.who.int/news-room/q-a-detail/herd-immunity-lockdowns-and-covid-19)

### Data Sources
[California COVID Data](https://covid19.ca.gov/state-dashboard/)  
[Florida COVID Data](https://floridahealthcovid19.gov/)  
[Illinois COVID Data](https://www.dph.illinois.gov/covid19/covid19-statistics)  
[New York COVID Data](https://covid19tracker.health.ny.gov/views/NYS-COVID19-Tracker/NYSDOHCOVID-19Tracker-Map?%3Aembed=yes&%3Atoolbar=no&%3Atabs=n)  
[Texas COVID Data](https://dshs.texas.gov/coronavirus/additionaldata.aspx)  
[Census Datasets](https://api.census.gov/data.html)  
[Census FIPS codes](https://www2.census.gov/geo/docs/reference/codes/files/)  
[Census Geographic Data](https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2018.html)  
[CDC Obesity Data](https://gis.cdc.gov/grasp/diabetes/DiabetesAtlas.html)  
[American Community Survey 5-Year Data (2009-2018)](https://www.census.gov/data/developers/data-sets/acs-5year.html)  
[Notes on ACS Estimate and Annotation Values](https://www.census.gov/data/developers/data-sets/acs-1year/notes-on-acs-estimate-and-annotation-values.html)  
[GeoJson Data CA, IL, NY](https://github.com/codeforamerica/click_that_hood/blob/master/public/data/)  
[GeoJson Data FL](https://www2.census.gov/geo/tiger/TIGER2010/COUNTY/2010/)  
[GeoJson Data TX](https://github.com/TNRIS/tx.geojson/blob/master/counties/tx_counties.geojson)  

# Data Dictionary

|Column Label|Type|Description
|------------|----|-----------|
|health_ins_noninst_pop|int|(Discrete): Total population civilian noninstitutionalized used to calculate yes/no coverage %
|health_ins_noninst_pop_cov_no|int| (Discrete): Population civilian noninstitutionalized without health insurance coverage
|health_ins_noninst_pop_cov_yes|int|(Discrete): Population civilian noninstitutionalized with health insurance coverage
|inc_hhlds|int|(Discrete): Total households used to calculate household income %
|inc_hhlds_less_than_10_000|int|(Discrete): Households less than 10,000 income
|inc_hhlds_10_000_to_14_999|int|(Discrete): Households 10,000 to 14,999 income
|inc_hhlds_15_000_to_24_999|int|(Discrete): Households 15,000 to 24,999 income
|inc_hhlds_25_000_to_34_999|int|(Discrete): Households 25,000 to 34,999 income
|inc_hhlds_35_000_to_49_999|int|(Discrete): Households 35,000 to 49,999 income
|inc_hhlds_50_000_to_74_999|int|(Discrete): Households 50,000 to 74,999 income
|inc_hhlds_75_000_to_99_999|int|(Discrete): Households 75,000 to 99,999 income
|inc_hhlds_100_000_to_149_999|int|(Discrete): Households 100,000 to 149,999 income
|inc_hhlds_150_000_to_199_999|int|(Discrete): Households 150,000 to 199,999 income
|inc_hhlds_200_000_or_more|int|(Discrete): Households 200,000+ income
|inc_mean_hhld_inc_dol|int|(Discrete): Mean household income (dollars)
|inc_med_hhld_inc_dol|int|(Discrete): Median household income (dollars)
|inc_med_earn_female_full_yr_workers_dol|int|(Discrete): Median earnings for female full-time, year-round workers (dollars)
|inc_med_earn_male_full_yr_workers_dol|int|(Discrete): Median earnings for male full-time, year-round workers (dollars)
|inc_per_capita_inc_dol|int|(Discrete): Per capita income (dollars)
|obes_percent|float|(Continuous): Population obesity percentage
|pop_density|float|(Continuous): People per square mile
|race_pop|int|(Discrete): Total population used to calculate race demographic %
|race_pop_american_indian_and_alaska_native_alone|int|(Discrete): Population American Indian and Alaska Native
|race_pop_asian_alone|int|(Discrete): Population Asian
|race_pop_black_or_african_american_alone|int|(Discrete): Population Black or African American
|race_pop_hispanic_or_latino_of_any_race|int|(Discrete): Population Hispanic or Latino of any race
|race_pop_native_hawaiian_and_other_pacific_islander_alone|int|(Discrete): Population Native Hawaiian or other Pacific Islander
|race_pop_some_other_race_alone|int|(Discrete): Population some other race
|race_pop_two_or_more_races|int|(Discrete): Population two or more races
|race_pop_white_alone|int|(Discrete): Population White
|sex_age_median_age_in_years|float|(Continuous): Median age (years)
|sex_age_pop|int|(Discrete): Total population used to calculate sex/age demographic %
|sex_age_pop_under_5|int|(Discrete): Population under 5
|sex_age_pop_5_to_9|int|(Discrete): Population 5-9
|sex_age_pop_10_to_14|int|(Discrete): Population 10-14
|sex_age_pop_15_to_19|int|(Discrete): Population 15-19
|sex_age_pop_20_to_24|int|(Discrete): Population 20-24
|sex_age_pop_25_to_34|int|(Discrete): Population 25-34
|sex_age_pop_35_to_44|int|(Discrete): Population 35-44
|sex_age_pop_45_to_54|int|(Discrete): Population 45-54
|sex_age_pop_55_to_59|int|(Discrete): Population 55-59
|sex_age_pop_60_to_64|int|(Discrete): Population 60-64
|sex_age_pop_65_to_74|int|(Discrete): Population 65-74
|sex_age_pop_75_to_84|int|(Discrete): Population 75-84
|sex_age_pop_85_and_over|int|(Discrete): Population 85+
|sex_age_pop_female|int|(Discrete): Population females
|sex_age_pop_male|int|(Discrete): Population male
|sq_mi|float|(Continuous): Square miles