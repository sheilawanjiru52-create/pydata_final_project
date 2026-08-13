# Geospatial Analysis of Child Marriage Among Girls in Africa

## Problem Statement

Child marriage remains a significant social and development challenge across Africa, particularly among girls. Marriage before the age of 18 can limit girls' educational opportunities, increase their vulnerability to early pregnancy and poor health outcomes, and restrict their economic and social participation. Despite efforts by governments and international organizations to reduce child marriage, its prevalence varies considerably across African countries, and the geographical distribution and patterns of the practice are not always easily understood.

Existing child-marriage statistics are often presented in tables or reports, which can make it difficult to identify geographical patterns, differences between countries, and changes over time. Furthermore, understanding the relationship between child marriage and girls' educational attainment may provide additional insight into factors associated with the persistence of the practice.

This project will therefore use geospatial and statistical analysis to examine the prevalence of child marriage among girls across African countries. Data from sources such as UNICEF and the World Bank will be combined with geographic boundary data to visualize the distribution of child marriage, identify countries with particularly high prevalence, examine changes over time, and investigate the relationship between child marriage and girls' educational attainment.

## AIM

To investigate where child marriage is most prevalent, how it has changed over time, and whether socioeconomic factors are associated with it.

## Main objective

To analyze and visualize the geographical distribution and trends of child marriage across Africa using Python and GIS.

### Specific objectives

1.	To determine the prevalence of child marriage among girls across African countries.
   
2.	To identify geographical areas with particularly high levels of child marriage.

3.	To examine changes in child marriage prevalence over time.
  
4.	To investigate the relationship between child marriage and girls' education.
   
5.	To use Python and GIS to visualize geographical disparities and trends in child marriage across Africa.

## Main research question

What are the geographical patterns and trends of child marriage across Africa?

### Specific research questions

1.	Which African countries have the highest prevalence of child marriage?
   
2.	How does child marriage prevalence vary geographically across Africa?
   
3.	How has the prevalence of child marriage changed across African countries over time?
   
4.	Is child marriage prevalence associated with girls' educational attainment?


## Methodology
### 1. Study Design

This study will use a quantitative, descriptive and geospatial analysis approach to examine the distribution and trends of child marriage across African countries. The study will use secondary data rather than collecting primary data.

### 2. Data Source

The main dataset will be obtained from UNICEF's Child Marriage Database, which contains nationally representative data on child marriage indicators from sources such as Demographic and Health Surveys (DHS), Multiple Indicator Cluster Surveys (MICS), and other nationally representative surveys.

The analysis will focus primarily on the percentage of women aged 20–24 who were married or in union before the age of 18, as this is a standard indicator used to measure child marriage.

Additional indicators may be incorporated where appropriate, such as:

Marriage before age 15
Marriage before age 18
Marriage before age 15 among younger women
Marriage before age 18 among younger women
Year of observation
Country
### 3. Data Preparation and Cleaning

The UNICEF Excel dataset will be imported into Python using Pandas.

The data will be examined for:

-Missing values

-Duplicate records

-Incorrect data types

-Inconsistent country names

-Unnecessary rows and columns

-Multiple header rows

-Different survey years

Relevant African countries will then be extracted from the dataset.

The data will be transformed into a structured format containing variables such as:

Country | Year | Indicator | Percentage

### 4. Data Analysis

Descriptive statistical analysis will be performed using Python.

The analysis will determine:

-Countries with the highest prevalence of child marriage

-Countries with the lowest prevalence

-Average prevalence across African countries

-Differences between marriage before age 15 and before age 18

-Changes in prevalence over time where sufficient data are available

Countries will be ranked according to child-marriage prevalence to identify areas with particularly high levels.

5. Data Visualization

Matplotlib will be used to produce visualizations such as:

-Bar charts showing countries with the highest prevalence

-Comparisons between countries

-Line graphs showing changes over time

-Charts comparing marriage before age 15 and before age 18

These visualizations will help communicate patterns and differences identified during the statistical analysis.

6. GIS Analysis

Geospatial analysis will be conducted using GeoPandas.

A geographic boundary dataset containing the boundaries of African countries will be obtained in Shapefile or GeoJSON format.

The child-marriage dataset will then be merged with the geographic boundary dataset using the country name or an appropriate country code as the common identifier.

A choropleth map will be created to display the prevalence of child marriage across Africa. Different shades will represent different levels of prevalence, allowing geographical patterns and areas with relatively high prevalence to be identified.

7. Software and Tools

The following tools will be used:

-Python — overall data analysis

-Pandas — data cleaning and manipulation

-NumPy — numerical operations where necessary

-Matplotlib — statistical visualization

-GeoPandas — GIS and spatial analysis

-Jupyter Notebook / VS Code — development environment

-Excel — initial inspection of the UNICEF dataset

## Outcomes

1. Africa child-marriage map

A GeoPandas choropleth map showing the percentage of women aged 20–24 who were married or in union before age 18.

2. Top 10 countries

A Matplotlib bar chart showing the countries with the highest prevalence.

3. Lowest 10 countries

Another chart showing countries with relatively low prevalence.

4. Change over time

Check whether countries are actually making progress toward SDG Target 5.3, which calls for eliminating harmful practices including child marriage by 2030.

5. Education relationship
   
Girls' education ↑ → Child marriage ↓?

A scatter plot to look at the relationship between secondary-school attendance/educational attainment and child marriage prevalence.



