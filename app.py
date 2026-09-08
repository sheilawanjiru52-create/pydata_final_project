import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt


# -----------------------------
# Load data
# -----------------------------

africa_data = pd.read_csv("africa_data.csv")

africa_map = gpd.read_file("africa_map.geojson")
legal_map = gpd.read_file("africa_legal.geojson")

poverty_map = gpd.read_file("africa_poverty.geojson")
education_map = gpd.read_file("education_map.geojson")
def classify_exception(row):

    exceptions = []

    if row["Parental_Consent"] == "Yes":
        exceptions.append("Parental exception")

    if row["Court_Exception"] == "Yes":
        exceptions.append("Judicial exception")

    if row["Customary_Exception"] == "Yes":
        exceptions.append("Customary exception")

    if row["Religious_Exception"] == "Yes":
        exceptions.append("Religious exception")

    if len(exceptions) == 0:
        return "No exception"

    elif len(exceptions) == 1:
        return exceptions[0]

    else:
        return "Multiple exceptions"


legal_map["Exception_Category"] = legal_map.apply(
    classify_exception,
    axis=1
)




section = st.sidebar.radio(
    "Go to:",
    [
        "Introduction",
        "Aims & Research Questions",
        "Methodology",
        "Child Marriage Prevalence",
        "Legal Frameworks",
        "Poverty",
        "Girls' Education",
        "Interactive Maps",
        "Dashboard", 
        "Recommendations"
    ]
)


if section == "Introduction":

    st.title("Understanding Child Marriage in Africa")
    st.subheader("The Role of Law, Poverty, and Girls' Education")

    st.header("Introduction")

    st.markdown("""
    Africa alone is home to **14 out of 20 countries with the highest rates
    of child marriage globally**.

    In Africa, **130 million girls and women today were married before their
    18th birthday**, giving the continent the highest incidence globally
    (UNICEF, 2025).

    ### Child marriage is associated with:

    - **Early pregnancies** — a leading cause of death among adolescent girls.
    - **Leaving education early** — girls who marry as children are more likely to drop out of school.
    - **Domestic violence** — child brides face a greater risk of experiencing violence within marriage.
    - **HIV/AIDS** — child marriage can increase vulnerability to HIV infection.
    - **Complications during pregnancy and childbirth** — girls who marry and become pregnant at a young age face increased health risks because their bodies may not yet be fully prepared for pregnancy and childbirth.

    And yet, **at least 117 countries around the world allow child marriage
    to occur under certain circumstances**.

    Child marriage remains a major challenge across Africa, but its prevalence varies considerably between countries. 
    This raises an important question: why do some countries experience much higher levels of child marriage than others?”
    
    Child marriage in Africa persists due to a complex web of economic hardships, deeply entrenched cultural and religious traditions.
    
    In this project, I used geospatial analysis and data visualization to investigate the geographical distribution of child marriage across Africa
    and examine whether differences in legal frameworks, poverty, and girls' education are associated with child-marriage prevalence.”
    """)
    
elif section == "Aims & Research Questions":

    st.title("Aims & Research Questions")

    st.markdown("""
    ### Main Objective

    To analyze and visualize the geographical distribution and prevalence
    of child marriage across Africa using Python and Geographic Information
    Systems (GIS), and to examine its relationship with legal, economic,
    and educational factors.

    ### Specific Objectives

    1. **To determine** the prevalence of child marriage among girls across
        African countries.

    2. **To identify** geographical areas with particularly high levels of
        child marriage.

    3. **To examine** whether the strength of legal frameworks on minimum
        marriage age is associated with child-marriage prevalence among
        African countries.

    4. **To examine** whether African countries with higher extreme-poverty
        rates also tend to have higher child-marriage prevalence.

    5. **To examine** whether child-marriage prevalence is associated with
        girls' educational attainment across African countries.

    ### Main Research Question

    **What factors are associated with the prevalence and geographical
    distribution of child marriage across African countries?**

    ### Research Questions

    1. What is the prevalence of child marriage among girls across African countries?

    2. Which geographical areas in Africa have particularly high levels of child marriage?

    3. Is the strength of the legal framework on minimum marriage age associated
        with child-marriage prevalence among African countries?

    4. Do African countries with higher extreme-poverty rates also tend to have
        higher child-marriage prevalence?

    5. Is child-marriage prevalence associated with girls' educational attainment
        across African countries?
    """)
elif section == "Methodology":

    st.title("Methodology")

    st.subheader("Study Design")

    st.markdown("""
    This study used a **quantitative, cross-sectional, country-level
    analytical approach** combining geospatial analysis and exploratory
    data analysis.
    """)

    st.subheader("Data Sources and Variables")

    st.markdown("""
    The analysis combined several country-level datasets:

    - **Child Marriage:** Percentage of girls married before age 15 and
      before age 18. 
        UNICEF:
        https://data.unicef.org/resources/child-marriage-in-eastern-and-southern-africa-a-statistical-overview-and-reflections-on-ending-the-practice/


    - **Legal Frameworks:** Minimum legal age of marriage, parental consent,
      court exceptions, customary exceptions, religious exceptions, and
      details of legal exceptions. 
        World Economic Forum:
        https://www.weforum.org/stories/equity-diversity-and-inclusion/these-are-the-countries-where-child-marriage-is-legal/ 
        
        Equality Now:
        https://equalitynow.org/news/news-and-insights/to-end-child-marriage-in-southern-and-eastern-africa-governments-need-to-strengthen-laws-and-implementation/


    - **Poverty:** Percentage of the population living below
      **$3.00 per day**.
        Wikipedia:
        https://en.wikipedia.org/wiki/List_of_countries_by_percentage_of_population_living_in_poverty

    - **Girls' Education:** Percentage of girls completing
      lower-secondary education.
        World Bank:
        https://data.worldbank.org/indicator/SE.SEC.CMPT.LO.FE.ZS

    - **Geographic Data:** Country-level geographic boundaries for African
      countries used for spatial analysis.
        Natural Earth World Map:
        https://www.naturalearthdata.com/
    """)

    st.subheader("Data Cleaning and Preparation")

    st.markdown("""
    The datasets were cleaned and prepared using **Python and pandas**.

    The main preprocessing steps included:

    - Removing irrelevant records and non-country observations.
    - Handling missing values.
    - Standardizing country names across datasets.
    - Resolving differences in country naming between datasets.
    - Converting variables into appropriate numeric formats.
    - Identifying countries with missing observations.
    - Checking the consistency of variables before analysis.
    """)

    st.subheader("Data Integration")

    st.markdown("""
    The cleaned datasets were integrated using **country name as the
    common identifier**.

    """)

    st.subheader("Geospatial Analysis")

    st.markdown("""
    **GeoPandas** was used to combine the country-level indicators with
    geographic boundaries.

    Interactive choropleth maps were created to visualize:

    - Child marriage prevalence
    - Minimum legal marriage age
    - Legal exceptions to the minimum marriage age
    - Poverty
    - Girls' secondary-school completion

    """)


    st.subheader("Interactive Dashboard")

    st.markdown("""
    The final analysis was developed into an interactive **Streamlit
    dashboard**.

    The dashboard allows users to explore the findings through:

    - Interactive maps
    - Bar charts
    - Scatter plots
    - Legal-framework comparisons
    - Country-level exploration
    - Interactive comparison of child marriage, poverty, education,
      and legal indicators
    """)


elif section == "Child Marriage Prevalence":

    st.title("Child Marriage Prevalence")

    st.subheader(
        "What is the prevalence of Child Marriage Among Girls in Africa? (< 18 yrs)"
    )

   # Convert GeoDataFrame to GeoJSON
    geojson = africa_map.__geo_interface__

    # Create interactive map
    fig = px.choropleth(
        africa_map,
        geojson=geojson,
        locations=africa_map.index,
        color="Child_Marriage_18",
        color_continuous_scale="OrRd",
        hover_name="ADMIN",
        hover_data={
            "Child_Marriage_18": ":.1f"
        }
    )

    # Fit map to Africa
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    # Map appearance
    fig.update_layout(
        height=700,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar_title="Married by 18 (%)"
    )

    # Display interactive map in Streamlit
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.subheader("Key Insight")
    st.markdown("""
        
        Child marriage prevalence is highest in several countries across West and Central Africa. 
        Countries such as Niger, Chad, Burkina Faso, Mali, and the Central African Republic show particularly high levels of marriage among girls before the age of 18. 
        Indicates a concentration of high child-marriage prevalence across parts of the **Sahel and Central African** regions.

        In contrast, lower child-marriage prevalence is observed in much of **North and Southern Africa**. 
        Countries such as Algeria, Tunisia, Morocco, Namibia, and South Africa have comparatively lower proportions of girls married before age 18.
        """)
    
    
        # ==========================================
    # TOP 10 HIGHEST
    # ==========================================

    st.subheader(
        "Top 10 Countries with the Highest Child Marriage Prevalence"
    )

    top_10 = africa_data.nlargest(
        10,
        "Married_by_18"
    ).sort_values(
        "Married_by_18",
        ascending=True
    )

    fig_top = px.bar(
        top_10,
        x="Married_by_18",
        y="Country",
        orientation="h",
        text="Married_by_18",
        labels={
            "Married_by_18": "Marriage Before Age 18 (%)",
            "Country": "Country"
        },
        title="Top 10 Highest Child Marriage Prevalence"
    )

    fig_top.update_traces(
        marker_color="#B7410E",
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig_top.update_layout(
        height=600,
        xaxis_title="Marriage Before Age 18 (%)",
        yaxis_title="Country"
    )

    st.plotly_chart(
        fig_top,
        use_container_width=True
    )


    # ==========================================
    # BOTTOM 10 LOWEST
    # ==========================================

    st.subheader(
        "Top 10 Countries with the Lowest Child Marriage Prevalence"
    )

    bottom_10 = africa_data.nsmallest(
        10,
        "Married_by_18"
    ).sort_values(
        "Married_by_18",
        ascending=True
    )

    fig_bottom = px.bar(
        bottom_10,
        x="Married_by_18",
        y="Country",
        orientation="h",
        text="Married_by_18",
        labels={
            "Married_by_18": "Marriage Before Age 18 (%)",
            "Country": "Country"
        },
        title="Top 10 Lowest Child Marriage Prevalence"
    )

    fig_bottom.update_traces(
        marker_color="#3B82F6",
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig_bottom.update_layout(
        height=600,
        xaxis_title="Marriage Before Age 18 (%)",
        yaxis_title="Country"
    )

    st.plotly_chart(
        fig_bottom,
        use_container_width=True
    )
elif section == "Legal Frameworks":

    st.title("Legal Frameworks")

    # ==========================================
    # MAP
    # ==========================================

    st.subheader("What is the minimum Legal Age of Marriage in African countries?")

    geojson = legal_map.__geo_interface__

    fig_map = px.choropleth(
        legal_map,
        geojson=geojson,
        locations=legal_map.index,
        color="Legal_Age",
        color_continuous_scale="OrRd",
        hover_name="ADMIN",
        hover_data={
            "Legal_Age": True,
            "Age_Category": True
        }
    )

    fig_map.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_map.update_layout(
        height=650,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar_title="Legal Marriage Age"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )
    
    st.subheader("Key Insight")
    st.markdown("""
            
            In most African countries, the minimum age for marriage is 18 yrs for girls.
            **Sudan, South Sudan, Equatorial Guinea and Somalia** have no specific minimum age where it is permittable for a girl to get married.
            **Senegal, Gambia, Niger, Cameroon and Tanznia** have legal minimum ages of below 18 yrs.
            Some countries such as **Rwanda, Algeria and Morocco have legal ages that are above 18yrs. 
            """)

    # ==========================================
    # SCATTER PLOT
    # ==========================================

    st.subheader(
        "Legal Minimum Age vs Child Marriage Prevalence"
    )

    # Take top 10 and bottom 10 countries
    top_10 = africa_data.nlargest(
        10,
        "Married_by_18"
    )

    bottom_10 = africa_data.nsmallest(
        10,
        "Married_by_18"
    )

    top_bottom = pd.concat(
        [top_10, bottom_10]
    )

    # Add legal age
    scatter_data = top_bottom.merge(
        legal_map[[
            "Country",
            "Legal_Age"
        ]],
        on="Country",
        how="left"
    )

    # Convert legal age to numeric
    scatter_data["Legal_Age"] = pd.to_numeric(
        scatter_data["Legal_Age"],
        errors="coerce"
    )

    # Remove missing values
    scatter_data = scatter_data.dropna(
        subset=[
            "Legal_Age",
            "Married_by_18"
        ]
    )

    # Identify top and bottom groups
    scatter_data["Group"] = scatter_data[
        "Married_by_18"
    ].apply(
        lambda x:
        "Top 10 Highest"
        if x in top_10["Married_by_18"].values
        else "Bottom 10 Lowest"
    )

    # Create scatter plot
    fig_scatter = px.scatter(
        scatter_data,
        x="Legal_Age",
        y="Married_by_18",
        color="Group",
        hover_name="Country",
        hover_data={
            "Legal_Age": True,
            "Married_by_18": ":.1f",
            "Group": False
        },
        color_discrete_map={
            "Top 10 Highest": "#B7410E",
            "Bottom 10 Lowest": "#3B82F6"
        },
        labels={
            "Legal_Age":
                "Legal Minimum Age of Marriage",
            "Married_by_18":
                "Marriage Before Age 18 (%)"
        },
        title=(
            "Legal Minimum Age vs "
            "Prevalence of Marriage Before Age 18"
        )
    )

    fig_scatter.update_traces(
        marker=dict(
            size=12,
            opacity=0.7
        )
    )

    fig_scatter.update_layout(
        height=600
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )
    
    st.subheader("Key Insight")
    st.markdown("""
                
                Some countries despite having a legal minimum age 18, still have high percentages of girl child marriages.
                All countries with minimum legal ages of above 18, have very low percenteges of girl child marriages.
                """)
        # ==========================================
    # CLASSIFY LEGAL EXCEPTIONS
    # ==========================================

    def is_exception(value):

        if pd.isna(value):
            return False

        value = str(value).strip().lower()

        # Clearly indicates no exception
        if value in [
            "no",
            "none",
            "not specified in source",
            "no specific parental exception stated",
            "no specific court exception stated"
        ]:
            return False

        if value == "no criminalization":
            return False

        # Indicates an exception
        if (
            value.startswith("yes")
            or "exception" in value
            or "muslim" in value
            or "hindu" in value
            or "mohammedan" in value
        ):
            return True

        return False


    def classify_exception(row):

        exceptions = []

        # Parental exception
        if is_exception(row["Parental_Consent"]):
            exceptions.append("Parental")

        # Court exception
        if is_exception(row["Court_Exception"]):
            exceptions.append("Judicial")

        # Customary exception
        if is_exception(row["Customary_Exception"]):
            exceptions.append("Customary")

        # Religious exception
        if is_exception(row["Religious_Exception"]):
            exceptions.append("Religious")

        # No exceptions
        if len(exceptions) == 0:
            return "No exception"

        # Multiple exceptions
        if len(exceptions) > 1:
            return "Multiple exceptions"

        return exceptions[0] + " exception"


    legal_map["Exception_Category"] = legal_map.apply(
        classify_exception,
        axis=1
    )
     # ==========================================
    # INTERACTIVE EXCEPTIONS MAP
    # ==========================================

    st.subheader("Key Insight")
    st.subheader(
        "Are there exceptions that allow marriages below the Minimum legal Marriage Age?"
    )

    st.markdown(
        """
        There are countries where legal provisions may allow
        marriage below the stated minimum marriage age through parental,
        judicial, customary, or religious exceptions.
        
        """
    )

    geojson = legal_map.__geo_interface__

    fig_exceptions = px.choropleth(
        legal_map,
        geojson=geojson,
        locations=legal_map.index,
        color="Exception_Category",
        hover_name="Country",
        hover_data={
            "Legal_Age": True,
            "Exception_Category": True,
            "Parental_Consent": True,
            "Court_Exception": True,
            "Customary_Exception": True,
            "Religious_Exception": True,
        },
        color_discrete_map={
            "No exception": "#D3D3D3",
            "Parental exception": "#FECACA",
            "Judicial exception": "#FDBA74",
            "Customary exception": "#F97316",
            "Religious exception": "#DC2626",
            "Multiple exceptions": "#991B1B"
        }
    )

    fig_exceptions.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_exceptions.update_layout(
        height=700,
        margin={
            "r": 0,
            "t": 0,
            "l": 0,
            "b": 0
        },
        legend_title_text="Exception Type"
    )

    st.plotly_chart(
        fig_exceptions,
        use_container_width=True
    )
    
    
elif section == "Poverty":

    st.title("Poverty")

    # ==========================================
    # MAP
    # ==========================================

    st.subheader("Population Living Below $3.00/day")

    geojson = poverty_map.__geo_interface__

    fig_map = px.choropleth(
        poverty_map,
        geojson=geojson,
        locations=poverty_map.index,
        color="Poverty < $3.00/day (%)",
        color_continuous_scale="OrRd",
        hover_name="ADMIN",
        hover_data={
            "Poverty < $3.00/day (%)": ":.1f"
        }
    )

    fig_map.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_map.update_layout(
        height=650,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar_title="Poverty (%)"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )


    # ==========================================
    # SCATTER PLOT
    # ==========================================

    st.subheader(
        "Poverty and Child Marriage Among the "
        "Highest and Lowest Prevalence Countries"
    )

    # Top 10 and bottom 10 child-marriage countries
    top_10 = africa_data.nlargest(
        10,
        "Married_by_18"
    ).copy()

    bottom_10 = africa_data.nsmallest(
        10,
        "Married_by_18"
    ).copy()

    # Label the groups
    top_10["Group"] = "Top 10"
    bottom_10["Group"] = "Bottom 10"

    # Combine
    extreme_child_marriage = pd.concat(
        [top_10, bottom_10],
        ignore_index=True
    )

    # Add poverty data
    extreme_poverty = extreme_child_marriage.merge(
        poverty_map[
            [
                "Country",
                "Poverty < $3.00/day (%)"
            ]
        ],
        on="Country",
        how="inner"
    )

    # Remove missing values
    extreme_poverty = extreme_poverty.dropna(
        subset=[
            "Married_by_18",
            "Poverty < $3.00/day (%)"
        ]
    )

    # Interactive scatter plot
    fig_scatter = px.scatter(
        extreme_poverty,
        x="Poverty < $3.00/day (%)",
        y="Married_by_18",
        color="Group",
        hover_name="Country",
        hover_data={
            "Poverty < $3.00/day (%)": ":.1f",
            "Married_by_18": ":.1f",
            "Group": False
        },
        color_discrete_map={
            "Top 10": "#B7410E",
            "Bottom 10": "#3B82F6"
        },
        labels={
            "Poverty < $3.00/day (%)":
                "Population living below $3.00/day (%)",
            "Married_by_18":
                "Child Marriage by Age 18 (%)"
        }
    )

    fig_scatter.update_traces(
        marker=dict(
            size=12,
            opacity=0.7
        )
    )

    fig_scatter.update_layout(
        height=600
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )
    
    st.subheader("Key Insight")
    st.markdown("""
                
                Poverty appears to be an important but not universal characteristic among countries with high child-marriage prevalence. 
                
                Among the 10 countries with the highest child-marriage prevalence, approximately half have poverty rates above 50%, while the other half have poverty rates below 50%. 
                
                This suggests that although extreme poverty is common among several countries with high child-marriage prevalence, high levels of child marriage are also observed in countries where less than half of the population lives below $3.00 per day.

                In contrast, all 10 countries with the lowest child-marriage prevalence have poverty rates below 50%. 
                
                This pattern suggests a potential association between socioeconomic conditions and child marriage, while also indicating that poverty alone does not fully explain differences in child-marriage prevalence across African countries.
                """)
    
    
elif section == "Girls' Education":

    st.title("Girls' Education")

    # ==========================================
    # MAP
    # ==========================================

    st.subheader(
        "Girls' Lower-Secondary Completion Across Africa"
    )

    geojson = education_map.__geo_interface__

    fig_map = px.choropleth(
        education_map,
        geojson=geojson,
        locations=education_map.index,
        color="Girls_Secondary_Completion",
        color_continuous_scale="OrRd",
        hover_name="ADMIN",
        hover_data={
            "Girls_Secondary_Completion": ":.1f"
        }
    )

    fig_map.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_map.update_layout(
        height=650,
        margin={"r": 0, "t": 0, "l": 0, "b": 0,
        },
        coloraxis_colorbar_title="Completion (%)"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )


    # ==========================================
    # SCATTER PLOT
    # ==========================================

    st.subheader(
        "Girls' Secondary Completion and "
        "Child Marriage in Africa"
    )

    # Top 10 and bottom 10 child-marriage countries
    top_10 = africa_data.nlargest(
        10,
        "Married_by_18"
    ).copy()

    bottom_10 = africa_data.nsmallest(
        10,
        "Married_by_18"
    ).copy()

    # Label groups
    top_10["Group"] = "Top 10"
    bottom_10["Group"] = "Bottom 10"

    # Combine
    extreme_child_marriage = pd.concat(
        [top_10, bottom_10],
        ignore_index=True
    )

    # Add education data
    education_scatter = extreme_child_marriage.merge(
        education_map[
            [
                "Country",
                "Girls_Secondary_Completion"
            ]
        ],
        on="Country",
        how="inner"
    )

    # Remove missing values
    education_scatter = education_scatter.dropna(
        subset=[
            "Married_by_18",
            "Girls_Secondary_Completion"
        ]
    )

    # Create interactive scatter plot
    fig_scatter = px.scatter(
        education_scatter,
        x="Girls_Secondary_Completion",
        y="Married_by_18",
        color="Group",
        hover_name="Country",
        hover_data={
            "Girls_Secondary_Completion": ":.1f",
            "Married_by_18": ":.1f",
            "Group": False
        },
        color_discrete_map={
            "Top 10": "#B7410E",
            "Bottom 10": "#3B82F6"
        },
        labels={
            "Girls_Secondary_Completion":
                "Girls' Lower-Secondary Completion (%)",
            "Married_by_18":
                "Child Marriage by Age 18 (%)"
        },
        title=(
            "Girls' Secondary Completion "
            "and Child Marriage in Africa"
        )
    )

    # Marker size
    fig_scatter.update_traces(
        marker=dict(
            size=12,
            opacity=0.7
        )
    )

    fig_scatter.update_layout(
        height=600
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )
    
    st.subheader("Key Insight")
    
    st.markdown("""
    A clear inverse pattern is observed between **girls' secondary-school
    completion and child-marriage prevalence**.

    Almost all countries among the **10 countries with the highest
    child-marriage prevalence** have less than **50% of girls completing
    secondary education**.

    In contrast, most countries among the **10 countries with the lowest
    child-marriage prevalence** have girls' secondary-school completion rates
    above **50%**. **Djibouti and Gabon** are notable exceptions, with
    completion rates below 50% despite having relatively low child-marriage
    prevalence.

    Overall, this pattern suggests that **higher girls' educational attainment
    is associated with lower child-marriage prevalence**. However, the
    exceptions indicate that education alone does not explain all differences
    in child-marriage prevalence across African countries.
    """)


elif section == "Interactive Maps":

    st.title("Interactive Maps")

    map_choice = st.selectbox(
    "Choose a map to view:",
    [
        "Child Marriage Prevalence",
        "Legal Marriage Age",
        "Legal Exceptions",
        "Poverty Rate",
        "Girls Completing Secondary Education"
    ]
)
    # ==========================================
    # CHILD MARRIAGE PREVALENCE
    # ==========================================

    if map_choice == "Child Marriage Prevalence":

        st.subheader(
            "Prevalence of Child Marriage Among Girls Married by Age 18"
        )

        geojson = africa_map.__geo_interface__

        fig = px.choropleth(
            africa_map,
            geojson=geojson,
            locations=africa_map.index,
            color="Child_Marriage_18",
            color_continuous_scale="OrRd",
            hover_name="ADMIN",
            hover_data={
                "Child_Marriage_18": ":.1f"
            }
        )

        fig.update_geos(
            fitbounds="locations",
            visible=False
        )

        fig.update_layout(
            height=700,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            coloraxis_colorbar_title="Married by 18 (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        
    # ==========================================
    # LEGAL FRAMEWORK
    # ==========================================

    elif map_choice == "Legal Marriage Age":

        st.subheader("Minimum Legal Marriage Age")

        geojson = legal_map.__geo_interface__

        fig = px.choropleth(
            legal_map,
            geojson=geojson,
            locations=legal_map.index,
            color="Legal_Age",
            color_continuous_scale="OrRd",
            hover_name="ADMIN",
            hover_data={
                "Legal_Age": True,
                "Age_Category": True
            }
        )

        fig.update_geos(
            fitbounds="locations",
            visible=False
        )

        fig.update_layout(
            height=700,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            coloraxis_colorbar_title="Legal Marriage Age"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif map_choice == "Legal Exceptions":

        st.subheader("Legal Exceptions to Minimum Marriage Age")

        st.markdown(
            """
            Countries may have legal provisions that allow marriage below
            the stated minimum legal marriage age through parental, judicial,
            customary, or religious exceptions.
            """
        )

        geojson = legal_map.__geo_interface__

        fig_exceptions = px.choropleth(
            legal_map,
            geojson=geojson,
            locations=legal_map.index,
            color="Exception_Category",
            hover_name="Country",
            hover_data={
                "Legal_Age": True,
                "Exception_Category": True,
                "Parental_Consent": True,
                "Court_Exception": True,
                "Customary_Exception": True,
                "Religious_Exception": True,
            },
            color_discrete_map={
                "No exception": "#D3D3D3",
                "Parental exception": "#FECACA",
                "Judicial exception": "#FDBA74",
                "Customary exception": "#F97316",
                "Religious exception": "#DC2626",
                "Multiple exceptions": "#991B1B"
            }
        )

        fig_exceptions.update_geos(
            fitbounds="locations",
            visible=False
        )

        fig_exceptions.update_layout(
            height=700,
            margin={
                "r": 0,
                "t": 0,
                "l": 0,
                "b": 0
            },
            legend_title_text="Exception Type"
        )

        st.plotly_chart(
            fig_exceptions,
            use_container_width=True
        )
        st.markdown(
            """
            A high legal minimum age does not necessarily translate into low child-marriage prevalence.
            Several countries with some of the highest levels of child marriage have legislation that sets the minimum marriage age at 18 or above. For example, Niger, Central African Republic, Chad, and Côte d’Ivoire appear in legal frameworks with an 18+ minimum age for girls in some classifications, yet child-marriage prevalence remains high.
            
            The findings suggest that establishing a minimum legal marriage age of 18 or above is important but may not be sufficient on its own. 
            Legal exceptions, enforcement, social norms, poverty, and access to education may influence whether girls remain protected from child marriage in practice.
            """
                )
        
        
        # ==========================================
        # POVERTY
        # ==========================================

    elif map_choice == "Poverty Rate":

        st.subheader(
            "Percentage of Population Living Below $3.00 per Day"
        )

        geojson = poverty_map.__geo_interface__

        fig = px.choropleth(
            poverty_map,
            geojson=geojson,
            locations=poverty_map.index,
            color="Poverty < $3.00/day (%)",
            color_continuous_scale="OrRd",
            hover_name="ADMIN",
            hover_data={
                "Poverty < $3.00/day (%)": ":.1f",
                "Poverty Data Year": True
            }
        )

        fig.update_geos(
            fitbounds="locations",
            visible=False
        )

        fig.update_layout(
            height=700,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            coloraxis_colorbar_title="Poverty (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ==========================================
    # GIRLS' EDUCATION
    # ==========================================

    elif map_choice == "Girls Completing Secondary Education":

        st.subheader(
            "Girls Completing Secondary Education"
        )

        geojson = education_map.__geo_interface__

        fig = px.choropleth(
            education_map,
            geojson=geojson,
            locations=education_map.index,
            color="Girls_Secondary_Completion",
            color_continuous_scale="OrRd",
            hover_name="Country",
            hover_data={
                "Girls_Secondary_Completion": ":.1f"
            }
        )

        fig.update_geos(
            fitbounds="locations",
            visible=False
        )

        fig.update_layout(
            height=700,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            coloraxis_colorbar_title="Girls completing secondary (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
    st.subheader("SUMMARY")
        
    st.markdown("""
    **1. Child marriage varies considerably across Africa**.
    
    The geographical analysis shows substantial differences in prevalence between countries. The highest levels are concentrated mainly in West and Central Africa, with Niger, Chad, Central African Republic, Burkina Faso, and Mali among the countries with particularly high prevalence.
    
    **2. Child marriage prevalence is generally lower in parts of North and Southern Africa**.
    
    Countries such as Algeria, Tunisia, Morocco, Namibia, and South Africa show comparatively lower levels of marriage before age 18.
    
    3. Legal protection does not always mean that child marriage is completely prohibited.
    
    Although many countries have established a minimum legal marriage age of 18 or above, the legal-exceptions analysis shows that some countries have provisions involving parental consent, judicial/court approval, customary law, religious law, or combinations of these exceptions. 
    This demonstrates that the statutory minimum age alone does not necessarily provide complete protection from marriage before age 18.
    
    **4. Poverty appears to be associated with child-marriage prevalence, but the relationship is not absolute**.
    
    Among the 10 countries with the highest child-marriage prevalence, approximately half had poverty rates above 50%, while the other half were below 50%. 
    In contrast, the 10 countries with the lowest child-marriage prevalence all had poverty rates below 50%. This suggests that economic vulnerability may be an important contributing factor, but poverty alone does not explain differences in child-marriage prevalence.
    
     5. Girls' secondary education shows a stronger observable pattern.
    
    Most of the countries with the highest child-marriage prevalence had girls' secondary-school completion rates below 50%. 
    
    Conversely, most countries with the lowest child-marriage prevalence had secondary-school completion rates above 50%.
    
    The findings suggest that child marriage is a multidimensional issue.
    
    The maps and scatter plots indicate that child marriage cannot be understood solely through legislation or poverty. Geography, legal frameworks and exceptions, economic conditions, and girls' educational attainment all provide important perspectives for understanding differences in prevalence across African countries.
    """)
elif section == "Dashboard":

    st.title("Child Marriage in Africa")
    st.subheader(
        "A Geographical, Legal, Economic and Educational Analysis"
    )

    st.markdown("""
    This dashboard brings together the key findings from the analysis
    of child marriage prevalence across African countries and its
    relationship with legal frameworks, poverty and girls' education.
    """)
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Countries Analyzed",
        africa_data["Country"].nunique()
    )

    col2.metric(
        "Highest Prevalence",
        f"{africa_data['Married_by_18'].max():.1f}%"
    )

    col3.metric(
        "Lowest Prevalence",
        f"{africa_data['Married_by_18'].min():.1f}%"
    )

    col4.metric(
        "Average Prevalence",
        f"{africa_data['Married_by_18'].mean():.1f}%"
    )
    st.divider()

    st.header("Child Marriage Prevalence")

    st.markdown("""
    The map and charts below show the geographical distribution of
    child marriage among girls married before age 18 across Africa.
    """)

    # Interactive child marriage map
    geojson = africa_map.__geo_interface__

    fig_map = px.choropleth(
        africa_map,
        geojson=geojson,
        locations=africa_map.index,
        color="Child_Marriage_18",
        color_continuous_scale="OrRd",
        hover_name="Country",
        hover_data={
            "Child_Marriage_18": ":.1f"
        }
    )

    fig_map.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_map.update_layout(
        height=600,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar_title="Married by 18 (%)"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )
    st.subheader("Countries with the Highest and Lowest Prevalence")

    top_10 = (
        africa_data
        .nlargest(10, "Married_by_18")
        .sort_values("Married_by_18")
    )

    bottom_10 = (
        africa_data
        .nsmallest(10, "Married_by_18")
        .sort_values("Married_by_18")
    )
    col1, col2 = st.columns(2)

    with col1:

        fig_top = px.bar(
            top_10,
            x="Married_by_18",
            y="Country",
            orientation="h",
            title="Top 10 Countries with Highest Child Marriage",
            labels={
                "Married_by_18": "Marriage Before Age 18 (%)",
                "Country": ""
            }
        )

        fig_top.update_traces(
            marker_color="firebrick"
        )

        fig_top.update_layout(
            height=500
        )

        st.plotly_chart(
            fig_top,
            use_container_width=True
        )

    with col2:

        fig_bottom = px.bar(
            bottom_10,
            x="Married_by_18",
            y="Country",
            orientation="h",
            title="Top 10 Countries with Lowest Child Marriage",
            labels={
                "Married_by_18": "Marriage Before Age 18 (%)",
                "Country": ""
            }
        )

        fig_bottom.update_traces(
            marker_color="steelblue"
        )

        fig_bottom.update_layout(
            height=500
        )

        st.plotly_chart(
            fig_bottom,
            use_container_width=True
        )
    st.subheader("Legal Minimum Age and Child Marriage")

    # Get the 10 highest and 10 lowest prevalence countries
    legal_top = africa_data.nlargest(
        10, "Married_by_18"
    ).copy()

    legal_bottom = africa_data.nsmallest(
        10, "Married_by_18"
    ).copy()

    legal_extremes = pd.concat(
        [legal_top, legal_bottom],
        ignore_index=True
    )

    # Add legal age information
    legal_extremes = legal_extremes.merge(
        legal_map[
            ["Country", "Legal_Age"]
        ],
        on="Country",
        how="left"
    )

    # Convert legal age to numeric
    legal_extremes["Legal_Age"] = pd.to_numeric(
        legal_extremes["Legal_Age"],
        errors="coerce"
    )

    # Identify Top 10 and Bottom 10
    legal_extremes["Group"] = "Bottom 10"

    legal_extremes.loc[
        legal_extremes["Country"].isin(
            legal_top["Country"]
        ),
        "Group"
    ] = "Top 10"

    # Remove missing values
    legal_extremes = legal_extremes.dropna(
        subset=[
            "Legal_Age",
            "Married_by_18"
        ]
    )

    # Create interactive scatter plot
    fig_legal = px.scatter(
        legal_extremes,
        x="Legal_Age",
        y="Married_by_18",
        color="Group",
        hover_name="Country",
        hover_data={
            "Legal_Age": True,
            "Married_by_18": ":.1f",
            "Group": True
        },
        color_discrete_map={
            "Top 10": "firebrick",
            "Bottom 10": "blue"
        },
        labels={
            "Legal_Age": "Legal Minimum Age of Marriage",
            "Married_by_18": "Marriage Before Age 18 (%)"
        },
        title="Legal Minimum Age vs Child Marriage Prevalence"
    )

    fig_legal.update_layout(
        height=550
    )

    st.plotly_chart(
        fig_legal,
        use_container_width=True
    )
    st.subheader("Poverty and Child Marriage")

    # Get the 10 highest and 10 lowest prevalence countries
    poverty_top = africa_data.nlargest(
        10, "Married_by_18"
    ).copy()

    poverty_bottom = africa_data.nsmallest(
        10, "Married_by_18"
    ).copy()

    poverty_extremes = pd.concat(
        [poverty_top, poverty_bottom],
        ignore_index=True
    )

    # Add poverty information
    poverty_extremes = poverty_extremes.merge(
        poverty_map[
            [
                "Country",
                "Poverty < $3.00/day (%)"
            ]
        ],
        on="Country",
        how="left"
    )

    # Identify Top 10 and Bottom 10
    poverty_extremes["Group"] = "Bottom 10"

    poverty_extremes.loc[
        poverty_extremes["Country"].isin(
            poverty_top["Country"]
        ),
        "Group"
    ] = "Top 10"

    # Remove missing values
    poverty_extremes = poverty_extremes.dropna(
        subset=[
            "Poverty < $3.00/day (%)",
            "Married_by_18"
        ]
    )

    # Create interactive scatter plot
    fig_poverty = px.scatter(
        poverty_extremes,
        x="Poverty < $3.00/day (%)",
        y="Married_by_18",
        color="Group",
        hover_name="Country",
        hover_data={
            "Poverty < $3.00/day (%)": ":.1f",
            "Married_by_18": ":.1f",
            "Group": True
        },
        color_discrete_map={
            "Top 10": "firebrick",
            "Bottom 10": "blue"
        },
        labels={
            "Poverty < $3.00/day (%)":
                "Population Living Below $3.00/day (%)",
            "Married_by_18":
                "Marriage Before Age 18 (%)"
        },
        title="Poverty and Child Marriage"
    )

    fig_poverty.update_layout(
        height=550
    )

    st.plotly_chart(
        fig_poverty,
        use_container_width=True
    )
    st.subheader(
        "Girls' Secondary Education and Child Marriage"
    )

    # Get the 10 highest and 10 lowest prevalence countries
    education_top = africa_data.nlargest(
        10, "Married_by_18"
    ).copy()

    education_bottom = africa_data.nsmallest(
        10, "Married_by_18"
    ).copy()

    education_extremes = pd.concat(
        [education_top, education_bottom],
        ignore_index=True
    )

    # Add education information
    education_extremes = education_extremes.merge(
        education_map[
            [
                "Country",
                "Girls_Secondary_Completion"
            ]
        ],
        on="Country",
        how="left"
    )

    # Identify Top 10 and Bottom 10
    education_extremes["Group"] = "Bottom 10"

    education_extremes.loc[
        education_extremes["Country"].isin(
            education_top["Country"]
        ),
        "Group"
    ] = "Top 10"

    # Remove missing values
    education_extremes = education_extremes.dropna(
        subset=[
            "Girls_Secondary_Completion",
            "Married_by_18"
        ]
    )

    # Create interactive scatter plot
    fig_education = px.scatter(
        education_extremes,
        x="Girls_Secondary_Completion",
        y="Married_by_18",
        color="Group",
        hover_name="Country",
        hover_data={
            "Girls_Secondary_Completion": ":.1f",
            "Married_by_18": ":.1f",
            "Group": True
        },
        color_discrete_map={
            "Top 10": "firebrick",
            "Bottom 10": "blue"
        },
        labels={
            "Girls_Secondary_Completion":
                "Girls' Secondary Completion (%)",
            "Married_by_18":
                "Marriage Before Age 18 (%)"
        },
        title="Girls' Secondary Completion and Child Marriage"
    )

    fig_education.update_layout(
        height=550
    )

    st.plotly_chart(
        fig_education,
        use_container_width=True
    )
elif section == "Recommendations":

    st.title("Recommendations")

    st.subheader(
        "Recommendations for Reducing Child Marriage in Africa"
    )

    st.markdown("""
    ### 1. Strengthen and enforce minimum-age marriage laws

    African countries should strengthen and consistently enforce laws
    establishing **18 years as the minimum legal age of marriage**, while
    addressing legal loopholes that permit marriage below this age.

    Particular attention should be given to **parental, customary, religious,
    and court exceptions**, which can allow girls to marry before the age of
    18 despite the existence of a statutory minimum age.

    ### 2. Keep girls in school

    The analysis indicates that countries with high levels of child marriage
    often also have low levels of girls' secondary-school completion.
    Governments and development partners should therefore invest in
    keeping girls in school through:

    - scholarships and financial support
    - safe and accessible schools
    - reduction of school-related costs
    - menstrual health support
    - prevention of school dropout
    - programmes supporting girls who are already married or have children
      to return to education.

    ### 3. Target poverty and economic vulnerability

    Child marriage should be addressed as part of broader poverty-reduction
    strategies. Programmes should provide vulnerable families with economic
    support and livelihood opportunities so that financial hardship does not
    increase pressure to marry girls at an early age.

    ### 4. Prioritize high-prevalence regions

    Resources should be targeted towards countries and regions with the
    highest observed levels of child marriage, particularly areas in
    **West and Central Africa** where the analysis identified substantial
    prevalence.

    The African Union (AU) should continue coordinating continental action 
    through its commitment to gender equality, girls' empowerment and the 
    elimination of harmful practices under Agenda 2063. 
    Agenda 2063; identifies poverty reduction, education, women's and girls' 
    empowerment, and the elimination of violence and discrimination against women
    and girls as continental priorities

    ### 5. Strengthen community awareness and engagement

    Community-based programmes should emphasize the benefits of girls'
    education, the risks associated with early marriage and pregnancy, and
    girls' rights and access to protection services.

    ### 6. Improve data collection and monitoring

    Several countries had missing data for some indicators used in this
    analysis.

    Better and more consistent data would allow policymakers to identify
    vulnerable populations and evaluate whether interventions are working.

    ### 7. Use integrated interventions

    The findings suggest that child marriage should not be addressed through
    legislation alone. Effective prevention requires a combination of
    **legal protection, education, poverty reduction, community engagement,
    and support services for girls**.
    """)
    
    
        





