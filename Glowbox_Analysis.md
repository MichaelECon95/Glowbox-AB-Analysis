# Overview

You are a Data Analyst for an e-commerce company called GloBox. GloBox is an online marketplace that specializes in sourcing unique and high-quality products from around the world.

“*We believe that shopping should be an adventure, and we want to bring the world to your doorstep. From exotic spices and rare teas to handmade jewelry and textiles, we have a curated selection of products that you won't find anywhere else.*”

GloBox is primarily known amongst its customer base for boutique fashion items and high-end decor products. However, their food and drink offerings have grown tremendously in the last few months, and the company wants to bring awareness to this product category to increase revenue.

**A/B Test Setup**

The Growth team decides to run an A/B test that highlights key products in the food and drink category as a banner at the top of the website. The control group does not see the banner, and the test group sees it.

The setup of the A/B test is as follows:

1. The experiment is only being run on the mobile website.
2. A user visits the GloBox main page and is randomly assigned to either the control or test group. This is the join date for the user.
3. The page loads the banner if the user is assigned to the test group, and does not load the banner if the user is assigned to the control group.
4. The user subsequently may or may not purchase products from the website. It could be on the same day they join the experiment, or days later. If they do make one or more purchases, this is considered a “conversion”.

## Stakeholders

Your task is to analyze the results of the A/B test and provide a recommendation to your stakeholders about whether GloBox should launch the experience to all users. The group that you will be presenting to includes the following:

- **Growth Product & Engineering Team**: This is the team that you work with at GloBox. The team is made up of a product manager, a user experience designer, an engineering manager and several software engineers, and you, the data analyst. The team develops features for the GloBox website that drive growth in users and revenue.

- **Leila Al-Farsi, Product Manager, Growth**: Leila is the product manager for the Growth product and engineering team. Alongside Alejandro, she leads the Growth team by deciding their goals and projects, measuring their success against defined KPIs, and communicating results to other company leaders like Mei.

- **Alejandro Gonzalez, User Experience Designer, Growth**: Alejandro is the designer for the Growth product and engineering team. He conducts user research and designed the experience that the A/B test is evaluating.

- **Mei Kim, Head of Marketing**: Mei oversees the Marketing team, which works on targeting audiences with effective marketing campaigns to drive customers to the GloBox website. She collaborates frequently with Leila and Alejandro to design website experiences that will align well with the current marketing efforts.

Together, Leila, Alejandro, and Mei will decide whether or not to launch the experiment based on the results.

### _You can find a description of each table and its columns below._

- **users**: user demographic information
    - **id**: the user ID
    - **country**: ISO 3166 alpha-3 country code
    - **gender**: the user's gender (M = male, F = female, O = other)
- **groups**: user A/B test group assignment
    - **uid**: the user ID
    - **group**: the user’s test group
    - **join_dt**: the date the user joined the test (visited the page)
    - **device**: the device the user visited the page on (I = iOS, A = android)
- **activity**: user purchase activity, containing 1 row per day that a user made a purchase
    - **uid**: the user ID
    - **dt**: date of purchase activity
    - **device**: the device type the user purchased on (I = iOS, A = android)
    - **spent**: the purchase amount in USD
    
Key things to note:    
   1. All users should be assigned to one A/B test group
   2. Not all users make a purchase
   3. Purchase activity is for all product categories, not just food and drink

### Criteria: 
1. Use inferential statistics methods to justify a recommendation to launch or not launch the experience.
	Specification - Include a hypothesis test and a confidence interval calculation comparing the groups for the metrics of interest: conversion rate and avgerage amount spent per user.
2. Interpret confidence interval and hypothesis test results correctly. 
	Specification - Each confidence interval and hypothesis test include a valid conclusion/interpretation using statistically precise language.
3. Include visualizations to communicate the results
	Specification - Provide simplicit interpretations of the charts in the context of the A/B test.

## Phase 1 Filtering and Extracting the Data

1. Write a query that returns: the user ID, the user’s country, the user’s gender, the user’s device type, the user’s test group, whether or not they converted (spent > $0), and how much they spent in total ($0+). You’ll need to ensure that you end up with a dataset that has one row per user. If a user appears more than once in any table, you will need to summarize all of their purchases (if any) into one row.

2. Download the data as a CSV. This is what you will use in the next phase of analysis during the second sprint.

## Phase 2 Analyze Data

1. **Calculate A/B test statistics**
    - Conduct a hypothesis test to see whether there is a difference in the conversion rate between the two groups. What are the resulting p-value and conclusion?
    - Use the normal distribution and a 5% significance level. Use the pooled proportion for the standard error.
2. What is the 95% confidence interval for the difference in the conversion rate between the treatment and control (treatment-control)?
    - Use the normal distribution and unpooled proportions for the standard error.
3. Conduct a hypothesis test to see whether there is a difference in the average amount spent per user between the two groups. 
    - What are the resulting p-value and conclusion?
    - Use the t distribution and a 5% significance level. Assume unequal variance.
4. What is the 95% confidence interval for the difference in the average amount spent per user between the treatment and the control (treatment-control)?
    - Use the t distribution and assume unequal variance.

## Phase 3 Visual the Results

1. Create a visualization to compare the conversion rate and average amount spent between the test groups.
2. Visualize the distribution of the amount spent per user for each group.
3. Create visualizations to explore the relationship between the test metrics (conversion rate and average amount spent) and the user’s device.
4. Create visualizations to explore the relationship between the test metrics (conversion rate and average amount spent) and the user’s gender.
5. Create visualizations to explore the relationship between the test metrics (conversion rate and average amount spent) and the user’s country.
6. Visualize the Confidence Intervals. Plot the confidence intervals for the difference in conversion rate and the difference in the average amount spent between the two groups.

## Phase 4 Present the A/B Test Results "Written" Report

There is no right or wrong answer. You can choose any recommendation as long as you are able to justify it using the results and any assumptions about the company’s priorities.
Once you have decided on what action you want to recommend to the stakeholders and how you will justify it, you should craft your story in a compelling but straightforward way. This should be the key message communicated in the report and slides.
The audience for this report would be another Data Analyst or teammate that wants to know the complete details about your analysis. You may think of it like a scientific paper, where the goal is that anyone reading it could perfectly replicate your results.

### Technical guidelines:
1. There is no strict minimum or maximum for the length, but 3-5 pages would be reasonable.
2. You may use any preferred text type, markdown, script, etc. to create the report. 
### Content guidelines:
1. Include clear headers to make it easy to navigate a longer document.
2. You should use complete sentences and include as much technical detail as required, but also simple for non-technical readers to understand, to explain your process fully.
3. Use grammar and spell-checking to ensure your writing is free of errors.
### Recommended Structure (Optional but not limited to):
1. Header: Title, author, date, etc.
2. Summary: A short paragraph describing the TL;DR of your analysis, including the key result(s) and the recommendation.
3. Context: Everything necessary to give someone the context around the experiment, including the motivation, the parameters of the test, a light overview of the dataset, etc.
4. Results: All your analysis results, including those that don’t make it into the presentation. Include charts and explanations, details of any data cleaning, etc.
5. Recommendation: Should we launch or not? Do we have enough information to decide? Should we iterate on this experience and test it again?
6. Appendix: Code (links or include directly), links to any Tableau dashboards and spreadsheets.


### Make sure to include the following:
- **The recommendation clearly stated**
    - Should we launch it?
    - e.g. “I recommend that we launch this experiment.”
- **The statistical criteria you used to determine the recommendation**
    - Based on one or more of the choices above
    - e.g. “Since we saw a statistically significant increase in both success metrics, we can feel confident that the banner will lead to more revenue.”
- **Any business factors that you may have considered**
    - What is the monetary or operational cost of launching the feature?
        - e.g. “The banner is not difficult to launch and maintain, and so it is worth launching even if only one success metric increased significantly.”
    - What is the impact to the user or customer experience?
        - e.g. “The banner takes up high-value real estate on the main page, so we should only be comfortable launching it if it leads to more than an X% increase in revenue per user.”

### Recommendation Options
_Here are the possible recommendations you can make:_

1. **Launch the experiment**

We saw enough improvement in our success metrics that we feel confident in releasing the banner to all users. The perceived cost of launching the feature is worth the benefits that we saw in the A/B test.

2. **Do not launch the experiment**

We didn’t see enough improvement in our metrics of success, so it’s not a good idea to release the banner to all users. The perceived cost of launching the feature is **not** worth it based on the results of the A/B test.

3. **Continue iterating**

We didn’t see enough improvement in our success metrics to be confident in releasing the feature in its current state. However, perhaps there were some promising results that show we could possibly make changes to the banner experience and get better improvement next time. Maybe we could do some further data analysis to understand this better, or we need a larger sample size to make a confident recommendation.