# Geospatial Analysis of Child Marriage Among Girls in Africa

## Introduction
Africa alone is home to 14 out of 20 countries with the highest rates of child marriage

In Africa, 130 million girls and women today were married before their 18th birthday, the highest incidence globally (UNICEF, 2025).

Child marriages are associated with:

•	Early pregnancies- a leading cause of adolescent deaths

•	They are more likely to leave education early

•	Suffer domestic violence

•	Contract HIV/AIDS and die due to complications during pregnancy and childbirth – their bodies simply aren’t ready.

And yet, at least 117 countries around the world allow it to happen
Concerningly, most progress in Sub-Saharan Africa has occurred amongst the wealthiest families, while in poorer communities, there has been a rise in child marriage. This perpetuates an unacceptable and deeply entrenched divide along socio-economic lines and demonstrates how governments need to focus more on prioritizing elimination of child marriage. 

This project focused on analyzing and visualizing the geographical distribution of child marriage among girls across African countries using GIS and secondary data. It examined child marriage prevalence, particularly the proportion of girls married before ages 15 and 18, and explored how prevalence varied in relation to legal marriage frameworks, poverty levels, and girls’ educational attainment.


## Main Objective

To analyze and visualize the geographical distribution and patterns of child marriage among girls across African countries using Geographic Information Systems (GIS).


### Specific Objectives

-To analyze the prevalence and geographical distribution of child marriage among girls across African countries.

-To examine the relationship between child marriage prevalence and the legal frameworks governing marriage across African countries.

-To assess the association between child marriage prevalence and poverty levels across African countries.

-To examine the relationship between child marriage prevalence and girls’ educational attainment across African countries.

-To develop interactive GIS visualizations to identify geographical patterns and areas with high prevalence of child marriage in Africa.


## Research Questions

1. What are the geographical patterns and prevalence of child marriage among girls across African countries?

2. How does child marriage prevalence vary across countries with different legal frameworks governing marriage?

3. What is the relationship between poverty levels and child marriage prevalence across African countries?

4. What is the relationship between girls’ educational attainment and child marriage prevalence across African countries?

5. Which geographical areas in Africa have the highest prevalence of child marriage?


## Methodology

1. Research Design

The study will use a quantitative, descriptive and spatial analysis design based on secondary data.

The study will use GIS to analyze the geographical distribution of child marriage and explore how prevalence varies in relation to legal frameworks, poverty, and girls’ education across African countries.

2. Data Sources

Secondary data will be obtained from publicly available sources, including:

UNICEF - child marriage prevalence

World Bank - poverty and socioeconomic indicators

International education databases - girls’ educational attainment

Legal databases/reports - minimum legal age of marriage and exceptions

Geospatial datasets - country boundaries/shapefiles for Africa

3. Data Preparation and Cleaning

The datasets will be cleaned and prepared for spatial analysis. This will involve:

Removing irrelevant records and variables

Handling missing values

Removing non-African countries

Standardizing country names

Converting variables to appropriate data types

Checking for duplicate records

Merging the different datasets using country names as the common identifier

4. Exploratory Data Analysis

Descriptive analysis will be conducted to understand the distribution of child marriage.

This will include:

Summary statistics

Frequency distributions

Bar charts

Histograms

Box plots

Country rankings

Child marriage will primarily be examined using the indicators:

Percentage of girls married by age 15

Percentage of girls married by age 18

We also created a difference measure to help compare the two indicators.

5. Geospatial Analysis

The cleaned country-level data will be joined to an African country boundary shapefile/GeoJSON using a common country identifier.

Choropleth maps will then be created to visualize:

Child marriage by age 15

Child marriage by age 18

Differences in child marriage prevalence

Legal marriage frameworks

Poverty levels

Girls’ educational attainment

Different map layers will allow geographical patterns to be compared across countries.

6. Relationship Analysis

The study will use scatter plots and correlation analysis to explore relationships between child marriage and:

Poverty
Girls’ educational attainment

For example, child marriage prevalence will be plotted against girls' educational attainment to determine whether countries with higher educational attainment tend to have lower child marriage prevalence.

Similarly, child marriage prevalence will be compared with poverty indicators.

7. Legal Framework Analysis

Legal data will be analyzed to examine differences in marriage laws across countries.

Variables such as:

Minimum legal age of marriage

Parental consent

Court exceptions

Customary exceptions

Religious exceptions

will be examined alongside child marriage prevalence.

This will allow the study to identify geographical patterns between legal frameworks and child marriage prevalence.

8. Visualization and Dashboard Development

The findings will be presented through an interactive Streamlit dashboard.

The dashboard will contain sections for:

Introduction

Aims & Research Questions

Child Marriage Prevalence

Legal Frameworks

Poverty

Girls’ Education

Country Explorer

The dashboard will allow users to select and compare countries and interact with maps and visualizations.

9. Software and Tools

The main tools used will be:

Python

Pandas - data cleaning and manipulation

GeoPandas - GIS and spatial data analysis

Matplotlib/Seaborn - visualization

Plotly - interactive visualizations

GeoJSON/Shapefiles - geographical boundaries

Streamlit - interactive dashboard development
 






















