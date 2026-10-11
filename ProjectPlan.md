**1. Overview**

One of the most prevalent issues surrounding America, both in urban and rural areas, is food deserts. Food deserts are geographical locations where individuals have little or no access to healthy, nutritious food, often due to a lack of grocery stores in the neighborhood. In urban areas, this is defined as living areas where there are no groceries within a mile of the area. The city of Chicago is one of many who have food deserts. 

Our group is interested in investigating food accessibility across Chicago neighborhoods, identifying which neighborhoods are classified as food deserts, and exploring the correlation between Chicago food deserts, wealth, health, and transit information in the same neighborhoods. Having better knowledge of issues such as this makes it easier to combat these issues in the future and may move us forward to coming up with solutions. 

Before beginning the project, our group will do research on the history of food deserts and explore previous research done on their existence. From there, we will examine Chicago grocery store data by neighborhood, as well as census data, health data, and CTA transit data, linked together by the neighborhood, to determine the quality of the data and their relevance to our project's goals. From there, we will clean the datasets and map connections between the datasets for better comparison. Once we do that, we will examine what geographies are considered “food deserts" and what factors are common between them that differ from non-food desert neighborhoods. 

**2. Team**
**3. Research Question**

The primary research questions we are examining are as follows:

- Which specific Chicago neighborhoods have the lowest access to grocery stores relative to population? 

- Are food desert neighborhoods correlated to neighborhoods with poorer health?

- What demographic factors are similar across all food desert neighborhoods?

- Is there a correlation between access to public transportation and grocery store access?


**4. Datasets**
   
- Green Choice Food Catalog: The GreenChoice Food Catalog is a comprehensive food database that combines food and beverage catalogs from more than 75 of the largest food retailers in the United States. Each product is classified by its name, food type, nutrition facts, ingredient lists, allergens, and other identifying characteristics. Furthermore, each product is assigned a GreenScore, a rating from 0 to 100 that evaluates its overall health and sustainability based on factors such as ingredient processing and safety, nutritional quality, and climate impact. This dataset allows us to examine the types and nutritional quality of food products offered by major retailers operating in Chicago. By combining this information with complementary datasets on grocery store locations and the economical stance of neighborhoods, we can further investigate which Chicago neighborhoods experience the greatest barriers to grocery store access. Additionally, we can explore how the availability of nutritious food options, alongside factors such as income and food affordability, may contribute to disparities in food accessibility across Chicago communities.
https://about.greenchoicenow.com/food-data-api?utm_source=adwords&utm_term=food%20database&utm_campaign=B2B+Data+License+Leads&utm_medium=ppc&hsa_mt=p&hsa_ad=788359911272&hsa_net=adwords&hsa_src=g&hsa_kw=food%20database&hsa_tgt=kwd-313471614431&hsa_cam=23362234490&hsa_acc=3365111280&hsa_ver=3&hsa_grp=190503214055&gad_source=1&gad_campaignid=23362234490&gbraid=0AAAAAC70mCz3vzfNAtvXRVZfPJAcMdjRv&gclid=CjwKCAjw25fWBhAVEiwAMopNjudeyweY-wolrj9RcwbboCPQzB3dbFI5WlA2tI7KoKBlq77b5-FJuxoCpmkQAvD_BwE

- City of Chicago Neighborhoods: This dataset, published by data.cityofchicago.org, is a geographic dataset that includes the coordinate boundaries of 98 neighborhoods in Chicago. It is formatted in GeoJSON, meaning it contains geographic shapes rather than rows of data. Specific attributes include the primary neighborhood name, alternative or secondary name, the area coordinates, and the size of the neighborhood. Additionally, we are able to see when the record was last updated, allowing us to use the most relevant information as possible. This dataset will provide us with the geographic foundation for comparing grocery store accessibility across various neighborhoods. 
https://catalog.data.gov/dataset/neighborhoods_2012b?from_hint=eyJxIjoiYnJvd3NlciJ9

- Chicago Health Atlas: The Chicago Health Atlas is a publicly accessible data platform developed through a collaboration between the Chicago Department of Public Health and the University of Illinois Chicago School of Public Health. The platform allows users to compare health-related data across different time periods and communities throughout Chicago. The data is organized into categories such as clinical care, physical environment, socioeconomic factors, health behaviors, and demographics. This information can be visualized through scatterplots, maps, charts, and tables, allowing for comparisons across various indicators. Through the platform's "Places" tab, we can specifically look into Chicago neighborhoods, providing an opportunity to integrate this information with our City of Chicago Neighborhoods dataset. This would allow us to identify neighborhoods negatively affected by health and socioeconomic factors that may contribute to limited food accessibility. Additionally, the platform features a "Chicago Neighborhood Dashboard," organized into eight pillars with indicators like neighborhood safety and life expectancy. These measures provide further insight into broader patterns of public health and community well-being over time. We can also connect this back to our Green Choice Food Catalog to understand relational patterns between nutritional food quality, grocery store accesbiltiy, and the economic status of a neighborhood.
https://chicagohealthatlas.org/

- Transit Chicago Data: The Chicago Transit Authority (CTA) offers public data through the City of Chicago Data Portal. On their page, there are links to 20 data sets covering information like CTA bus stops, Metra train lines, bus routes, the number of monthly entries to the CTA, and more. Specifically for our project, using the dataset that records the bus stops would allow us to see which grocery stores are accessible to Chicago residents that require the use of public transport. This dataset features over 11,000 CTA bus stop data points. Other variables include a unique identifier of a Stop ID to attain bus tracker information, current stops, flag stops, and any stops that are out of service. We can further explore transportation barriers that may contribute to limited access to nutritious food, particularly in lower-income Chicago neighborhoods where residents may rely more heavily on public transportation.
https://www.transitchicago.com/data/

**5. Timeline**
**6. Constraints**

- All data sources are being compared in a reasonably similar time period (2010-2026), although some of the data from Chicago Health Atlas and Chicago Transit Authority are not as up to date (last updated in 2023 or 2024) compared to Green Choice Food Catalog or City of Chicago Neighborhood data

- Bus transit is the main form of transportation represented in this project for simplicity. (Subway Data, Taxis, Ubers, City Bikes, and other forms of transportation included would result in more accurate conclusions)

- Chicago Transit Authority’s KMZ/KML file on bus stops may not be feasible to utilize for an integrated tabular dataset without a neighborhood key attribute

- Green Choice Food Catalog data source may not be accessible in a free and timely manner

- City of Chicago Neighborhood’s GeoJSON file format may not be feasible to utilize for an integrated tabular dataset

- Neighborhood boundaries may differ across multiple datasets, possibly making comparisons more difficult. In addition, neighborhood-level analysis may hide differences in accessibility to healthy nutritious food among highly segregated areas included in a single neighborhood

- Measuring the distances of bus stops to grocery stores does not capture the full picture of grocery accessibility, as other factors, such as bus frequency and schedules, grocery store hours, and food affordability also influence residents’ ability to access nutritional and healthy food or groceries

**7. Gaps**

- Currently unable to independently produce a significant amount of the artifacts and tools listed in the course project examples (snakemake workflow automation, cleaning with OpenRefine, documenting a reproducible analysis, meaningful or complex visualizations, utilization of DCAT or Box for large data files, etc.)

- May lack the sufficient experience to seamlessly integrate all chosen datasets utilizing SQL in addition to the multiple different file formats including GeoJSON, JSON, CSV, XML, and KML/KMZ.
