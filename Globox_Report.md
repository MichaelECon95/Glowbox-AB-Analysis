# GloBox A/B Test Analysis

**Author:** Eric Contreras, Data Analyst  
**Date:** August 15, 2023

---

## Summary

GloBox's initiative to highlight its burgeoning food and drink category via a banner on its mobile website has yielded promising results. The A/B test data indicates a noticeable uplift in conversion rate, while the average expenditure per user remains unaltered. Given the simplicity of introducing the banner and its potential to elevate user engagement, a wider rollout is endorsed.

---

## Context and Motivation

In its ascent as a distinguished e-commerce entity, GloBox continually adapts to dynamic user preferences. With the food and drink segment demonstrating growth, it was selected for promotional endeavors. The A/B test divided users into a control group (without a banner) and a test group (with a banner), focusing on metrics like conversion rate and average spend.


---

## Recommendation and Justification

### Launch the Experiment

The surge in conversion rates, coupled with the banner's minimal operational overhead, makes a compelling case for its wider deployment. It not only highlights GloBox's evolving product portfolio but is also expected to enrich the user's browsing journey.

### Statistical Criteria

A significant p-value and a confidence interval lying entirely above zero validate the recommendation.

### Business Factors

- **Operational Cost**: The seamless integration and upkeep of the banner bolster the recommendation.
- **User Experience**: The banner, emphasizing the food and drink category, is projected to enhance the browsing experience, fostering deeper user engagement.

---

## Analysis

 1. Conduct a hypothesis test to determine whether there's a significant difference in the conversion rate between the two groups. Using the pooled proportion for the standard error and test at a 5% significance level. 
(3.8643, 0.0001)

- Given that the p-value is much less than the significance level of 0.05, we reject the null hypothesis. This means there is a statistically significant difference in the conversion rates between the two groups.

2. Calculate the 95% confidence interval for the difference in the conversion rate between the treatment and control groups (treatment - control). We'll use the normal distribution and unpooled proportions for the standard error. (0.0035, 0.0107)

- The 95% confidence interval for the difference in the conversion rate between the treatment and control groups (treatment - control) is: (0.00349,0.01065)

- This means that we are 95% confident that the difference in conversion rates between the test group (with the banner) and the control group (without the banner) lies within this interval.

3. Conduct a hypothesis test to determine if there's a significant difference in the average amount spent per user between the two groups. We'll use the t-distribution and assume unequal variances.

- The results of the hypothesis test for the difference in average amount spent per user between the control and test groups are:

    T-statistic: 0.0682

  P-value: 0.95

- Given that the p-value is much greater than the significance level of 0.05, we fail to reject the null hypothesis. This indicates that there isn't a statistically significant difference in the average amount spent per user between the two groups.

4. Calculate the 95% confidence interval for the difference in the average amount spent per user between the treatment and control groups (treatment - control). We'll use the t-distribution and assume unequal variances.

- The 95% confidence interval for the difference in the average amount spent per user between the treatment and control groups (treatment - control) is: (-0.439, 0.4708)

- This means that we are 95% confident that the difference in average amounts spent by users between the test group (with the banner) and the control group (without the banner) lies within this interval.


---

## Detailed Results

### 1. Conversion Rate

- **Test Group (B)**: Evidenced a marginally higher conversion rate over the Control Group (A).
- **Statistical Analysis**: A p-value less than 0.05 suggests a significant difference in conversion rates.
- **Confidence Interval**: Ranges between 0.00349 and 0.01065 for the conversion rate difference.

### 2. Average Amount Spent

- **Observation**: Spend patterns are consistent across groups.
- **Statistical Analysis**: P-value greater than 0.05 indicates no significant difference in average spend.
- **Confidence Interval**: Difference in average spend lies between $0.0 and $0.0317.


### 3. User Segmentation Analysis

#### Device

- iOS users consistently outshine Android counterparts in conversion rates and average spend.


#### Gender

- Male users marginally lead in conversion rates and spend.


#### Country

- Conversion and spend showcase variability across countries, but trends remain consistent within countries for test and control groups.


---

## Appendix

- **Code**: Employed Python for the analysis, with code excerpts available upon request.
- **Data Sources**:  
    - User Demographics: `users.csv`
    - A/B Test Group Assignment: `groups.csv`
    - Purchase Activity: `activity.csv`
- **Visualization**: Visual aids like bar graphs, distribution plots, and segmented analyses were pivotal in the analytical process.
    - Visualization Guide: Tableau ( https://public.tableau.com/views/GloBoxABTestAnalysisforFoodDrinkBanner/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link )
    -	Additional Resources: Gupta, Shivam Sen. “A/B Testing in Excel: What Should You Use?” Scaler Topics, 22 May 2023, www.scaler.com/topics/statistical-significance-calculator-excel/. Accessed 16 Aug. 2023.
