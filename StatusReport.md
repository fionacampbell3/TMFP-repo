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

**Constraints:**

**Contributions:**

Maggie - For this current milestone, I reached out to our team members for a meeting to discuss our progress so far, and to discuss next steps. I also discovered the irrelevance of the original healthy product dataset we chose, and found the updated Grocery store By Neighborhood dataset for use instead, noting key differences and how we can link our datasets together more effectively. Me and Fiona collaborated on choosing indicators for the Chicago Health Atlas dataset, finding the most relevant data to look into for the project. I also noticed that this dataset had a “Grocery Store Count” column, which I determined would be interesting to compare to our other grocery story by neighborhood dataset. Since both of these datasets are reliable, I asserted to our group that we will discuss how we will handle any differences in values for these columns. I also asserted that all of our datasets chosen can definitely be merged using multiple key indicators (primarily by neighborhood name, but potentially latitude and longitude if necessary). I then cleaned the Chicago Health Atlas Dataset as well as checked if the Number of Grocery Stores by Neighborhood dataset needed cleaning and prepared it for merging. Then, in collaboration with Panth and Fiona, we began the process of merging the three datasets together.

Fiona - For this current milestone, I assisted Maggie in choosing the relevant indicators from the Chicago Health Atlas dataset that we want to include in the project. We chose indicators like 'Walkability Index,' 'Grocery Store Count,' and ‘Overall Health Score' that will provide substantial insights into our research questions. We discussed how these columns can align with our other datasets, like looking at the rail lines, neighborhood grocery store accessibility, and how public transportation factors into our analysis. I also looked into utilizing 'GeoPandas' in order to find a way to clean the neighborhood datasets' latitude and longitude coordinates so that we can find a way to merge them into the ‘L’ line public transportation dataset. As a group we discussed reasonable ways to merge the datasets on the neighborhood name. I also updated the timeline in accordance with the group's new tasks that were completed during our first group meeting on October 23rd and continued to update this as we received instructor feedback and gained progress in tasks. On November 11th, Maggie and I began to download and clean the datasets in OpenRefine. I specifically cleaned the “Grocery Stores” CSV, where I was able to identify a gap of not having a grocery store count for a certain neighborhood and utilize the methods in class to add another column with this information. Maggie and I discussed merging the neighborhoods dataset and grocery store dataset on the neighborhood name, as they are both present and have all uppercase entries, which aligns for a clear match. 

