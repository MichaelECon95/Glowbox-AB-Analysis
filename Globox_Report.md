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

## Detailed Results

### 1. Conversion Rate

- **Test Group (B)**: Evidenced a marginally higher conversion rate over the Control Group (A).
- **Statistical Analysis**: A p-value less than 0.05 suggests a significant difference in conversion rates.
- **Confidence Interval**: Ranges between 0.00349 and 0.01065 for the conversion rate difference.
- **Visualization**: ![Bar Graph of Conversion Rate by Group](path_to_image)

### 2. Average Amount Spent

- **Observation**: Spend patterns are consistent across groups.
- **Statistical Analysis**: P-value greater than 0.05 indicates no significant difference in average spend.
- **Confidence Interval**: Difference in average spend lies between $0.0 and $0.0317.
- **Visualization**: ![Distribution Plot of Amount Spent per User](path_to_image)

### 3. User Segmentation Analysis

#### Device

- iOS users consistently outshine Android counterparts in conversion rates and average spend.
- **Visualization**: ![Comparison by Device Type](path_to_image)

#### Gender

- Male users marginally lead in conversion rates and spend.
- **Visualization**: ![Gender-based Spending Patterns](path_to_image)

#### Country

- Conversion and spend showcase variability across countries, but trends remain consistent within countries for test and control groups.
- **Visualization**: ![Geographical Spending Analysis](path_to_image)

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

## Appendix

- **Code**: Employed Python for the analysis, with code excerpts available upon request.
- **Data Sources**:  
    - User Demographics: `users.csv`
    - A/B Test Group Assignment: `groups.csv`
    - Purchase Activity: `activity.csv`
- **Visualization**: Visual aids like bar graphs, distribution plots, and segmented analyses were pivotal in the analytical process.
    - **Visualization Guide**: ![Complete Visualization Catalog](path_to_catalog_image)

