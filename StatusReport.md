***Milestone 3: Interim Status Report***

**Overview:**

 No update has been made to the overview. The project will still focus on food deserts in Chicago neighborhoods, and comparing grocery store access to health and transportation.

**Team:**

Team responsibilities have largely remained the same, with some additional tasks added as necessary.
Fiona - Providing thorough descriptions of the datasets, understanding what variables are most important to our research questions, assisting in preparing data sets, and keeping track of the timeline and deliverables needed from each team member
Maggie - Devising project overview and research questions, introducing external research to the topic, examining relevant information that may assist in research, and preparing datasets for cleaning and research, merging datasets by key indicators
Panth - Researching possible data visualizations and how to prepare data to implement them, identifying quality of datasets during cleaning stages, keeping track of steps taken during the project to write a data reproducibility section 
Tina - Documenting challenges encountered, identifying current known constraints, predicting future gaps, formatting in citations and references, and projecting further opportunities for future research

**Research or Business Questions:**

No changes have been made to the research questions for this project at the moment. They are being rewritten below for clarity. It is possible we are going to narrow the questions down after the datasets are properly merged and we can determine what can be answered with the most accuracy.

Which specific Chicago neighborhoods have the lowest access to grocery stores relative to population? 
Are food desert neighborhoods correlated to neighborhoods with poorer health?
What demographic factors are similar across all food desert neighborhoods?
How does wealth affect grocery store density, and are there certain grocery stores that only appear in wealthier/less wealthy neighborhoods?
Is there a correlation between access to public transportation and grocery store access?


**Datasets:**

One particular change made for our project was utilizing a different dataset for nutritious food vs. Chicago neighborhoods. Our old dataset was primarily composed of different products and their nutritional factors, which we found is difficult to work with for the purpose of this project. It was more tailored to individuals who wished to find more nutritional options within grocery stores and compare different, similar products to one another. We decided to replace this dataset with “Number of Grocery Stores per Neighborhood Area” by the City of Chicago database. This dataset  clearly shows each Chicago neighborhood, followed by the number of grocery stores present within the particular neighborhood. Not only will this dataset be easier to combine with Chicago health data, but it is more relevant to our topic of food deserts, rather than just nutritional food options. The link for the new dataset is below: https://data.cityofchicago.org/Community-Economic-Development/Number-of-Grocery-Stores-per-Neighborhood-Area/693r-hjdi

We left our other datasets alone, including our Chicago Health Atlas, City of Chicago Neighborhoods, and CTA transportation, as they are relevant. The Chicago Health Atlas will give crucial information for each neighborhood, including overall health status, uninsured rate, poverty rate, walkability index, life expectancy, racial demographics, and more. The Chicago Transit database, especially the ‘L’ line stops and bus stop location databases, are also useful as they will give us information on which neighborhoods have limited access to public transport. We decided we will use the Latitude and longitude of the stop locations, connect them to their corresponding Chicago neighborhoods (from the Boundaries- Neighborhoods database) to compare. Therefore, we will merge datasets by Neighborhood Name.

https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9
https://www.transitchicago.com/data/
https://chicagohealthatlas.org/

**Timeline:**

The following is a list of the tasks, dates, and contributors for Milestone 3 (Status Report) 
By October 23rd: 
Update used datasets for current state project: Maggie
Contribute to exporting datasets with relevant columns: Maggie, Panth, Fiona
Update challenges and constraints with merging datasets: Tina
Create a GitHub file for the Status Report (StatusReport.md): Fiona  
Assess current state of research/business questions: each member
By Nov. 9th
Cleaning Grocery Store dataset (Openrefine): Fiona 
Cleaning CTA dataset for merging: Panth
Cleaning Chicago Health Atlas dataset (Openrefine): Maggie
Cleaning Neighborhood dataset: Maggie
By Nov. 16th
Merging datasets: Panth, Maggie, Fiona
Each team member provides a summary of what they contributed for this milestone: each member

**Gaps:**

Some of the old gaps were filled as we learned about using OpenRefine to clean datasets. A new gap was encountered with a changed dataset. Most other gaps have not changed. 

- The grocery store dataset includes every single latitude and longitude for each observation. One gap we encountered was trying to figure out the possibilities of how to map grocery store locations to the neighborhoods while considering this unexpected data format presented.
- Unknown if our 4th research question can be answered. 
- Unknown if GeoPandas must be utilized.
- Unknown how to currently handle the_geom column from the neighborhood boundaries dataset.
- Currently unable to independently produce a significant amount of the artifacts and tools listed in the course project examples (documenting a reproducible analysis, meaningful or complex visualizations, utilization of DCAT or Box for large data files, etc.)
- May lack the sufficient experience to seamlessly integrate all chosen datasets utilizing SQL in addition to the multiple different file formats including GeoJSON, JSON, CSV, XML, and KML/KMZ.

**Constraints:**

A few changes have been made to our constraints. For the ease of this project, we have changed to working with CSV formats for most of our chosen datasets. Constraints of the past inaccessible food nutrition dataset have been deleted. New constraints have been added among exploring the four datasets along with our process of dataset integration. New challenges were also found and resolved.

- We found how large food corporations have inconsistent naming principles in the grocery store dataset. For example, ALDI has either ‘ALDI’S’, ‘ALDI’, or “ALDI #x” (x being whatever number was chosen for that address). A challenge we encountered was needing to find the best case naming principle for our project. Two solutions are having the names be the same across all addresses because they are uniquely identified by their address, or having the stores be individually named.
- One of the challenges we encountered throughout the beginning of this project has been finding a more relevant grocery store dataset for Chicago. As mentioned in the “Datasets” section, after looking into the dataset we chose, we found that it is much more focused than products over grocery store locations, and is not relevant to our project. Therefore, we found a much more relevant dataset on the number of Chicago grocery stores per neighborhood area.
- Another challenge we had was the grocery store dataset not having a way to count the number of stores in the same neighborhood. We decided to add another column to be able to match this to the neighborhood boundary dataset and get an accurate count of how many grocery store options people have, given they are in a certain neighborhood. 
- The grocery store dataset’s License ID and Square Feet columns include a minimal amount of missing values, although we do not believe this will significantly impact our research and conclusions.
- All data sources are being compared in a reasonably similar time period (2010-2026), although some of the data from Chicago Grocery Stores, Chicago Health Atlas, and Chicago Transit Authority are not as up to date (last updated in 2019, 2023, and 2024,  respectively) compared to the City of Chicago Neighborhood data.
- Bus and subway transit is the main form of transportation represented in this project for simplicity. Ubers, e-Bikes, and other forms of transportation included would result in more accurate conclusions.
- Neighborhood boundaries may differ across multiple datasets, possibly making comparisons more difficult. In addition, neighborhood-level analysis may hide differences in accessibility to healthy nutritious food among highly segregated areas included in a single neighborhood.
- Measuring the distances of bus stops to grocery stores does not capture the full picture of grocery accessibility, as other factors, such as bus frequency and schedules, grocery store hours, and food affordability also influence residents’ ability to access nutritional and healthy food or groceries.
- Chicago Transit Authority’s KMZ/KML file on bus stops may not be feasible to utilize for an integrated tabular dataset.

**Contributions:**

Maggie - For this current milestone, I reached out to our team members for a meeting to discuss our progress so far, and to discuss next steps. I also discovered the irrelevance of the original healthy product dataset we chose, and found the updated Grocery store By Neighborhood dataset for use instead, noting key differences and how we can link our datasets together more effectively. Me and Fiona collaborated on choosing indicators for the Chicago Health Atlas dataset, finding the most relevant data to look into for the project. I also noticed that this dataset had a “Grocery Store Count” column, which I determined would be interesting to compare to our other grocery story by neighborhood dataset. Since both of these datasets are reliable, I asserted to our group that we will discuss how we will handle any differences in values for these columns. I also asserted that all of our datasets chosen can definitely be merged using multiple key indicators (primarily by neighborhood name, but potentially latitude and longitude if necessary). I then cleaned the Chicago Health Atlas Dataset as well as checked if the Number of Grocery Stores by Neighborhood dataset needed cleaning and prepared it for merging. Then, in collaboration with Panth and Fiona, we began the process of merging the three datasets together.

Fiona - For this current milestone, I assisted Maggie in choosing the relevant indicators from the Chicago Health Atlas dataset that we want to include in the project. We chose indicators like 'Walkability Index,' 'Grocery Store Count,' and ‘Overall Health Score' that will provide substantial insights into our research questions. We discussed how these columns can align with our other datasets, like looking at the rail lines, neighborhood grocery store accessibility, and how public transportation factors into our analysis. I also looked into utilizing 'GeoPandas' in order to find a way to clean the neighborhood datasets' latitude and longitude coordinates so that we can find a way to merge them into the ‘L’ line public transportation dataset. As a group we discussed reasonable ways to merge the datasets on the neighborhood name. I also updated the timeline in accordance with the group's new tasks that were completed during our first group meeting on October 23rd and continued to update this as we received instructor feedback and gained progress in tasks. On November 11th, Maggie and I began to download and clean the datasets in OpenRefine. I specifically cleaned the “Grocery Stores” CSV, where I was able to identify a gap of not having a grocery store count for a certain neighborhood and utilize the methods in class to add another column with this information. Maggie and I discussed merging the neighborhoods dataset and grocery store dataset on the neighborhood name, as they are both present and have all uppercase entries, which aligns for a clear match. 

Tina - For this current milestone, I discussed with our team about the accessibility and relevancy of the food nutrition dataset that we ultimately decided to replace with the neighborhood boundaries dataset. I helped ensure a neighborhood key was present in the datasets we wanted to work with. In addition, I pointed out the multiple file formats we were approached with and the feasibility of integrating them with our current skills. We mostly stuck with CSV formatting when possible. For written changes, I helped document all the issues and problems encountered from all members handling the technical side of the project. Specifically, I was responsible for the constraints and gaps section. For the gaps section, our previous gaps with OpenRefine were deleted while new gaps were found among exploration of the four datasets. For the constraints section, new challenges we encountered were added in and some incompleteness was discovered with new missing values. I also evaluated and updated the data currency with the neighborhood boundaries dataset.

