import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm
from scipy.stats import ttest_ind

# Loading the CSV files


# Merging the users and groups dataframes on user ID
merged_df = users_df.merge(groups_df, left_on='id', right_on='uid', how='left')

# Merging the activity data to calculate total spend and conversion for each user
user_spent = activity_df.groupby('uid').agg({'spent': 'sum'}).reset_index()
user_spent['converted'] = (user_spent['spent'] > 0).astype(int)

# Merging the calculated data with the main dataframe
merged_df = merged_df.merge(user_spent, on='uid', how='left').fillna(0)

# Dropping redundant columns
merged_df.drop(columns=['id'], inplace=True)

# Display the first few rows of the merged dataframe
merged_df.head()

"""
Each row now represents a unique user, and we have the following columns:

country: ISO 3166 alpha-3 country code.

gender: The user's gender (M = male, F = female, O = other).

uid: The user ID.

group: The users test group.

join_dt: The date the user joined the test (visited the page).

device: The device the user visited the page on (I = iOS, A = android).

spent: Total amount spent by the user in USD.

converted: Whether the user made a purchase (1 if they made a purchase, 0 otherwise).

"""

# Part 2 Testing the Data

# 1. Conduct a hypothesis test to determine whether there's a significant difference in the conversion rate between the two groups. We'll use the pooled proportion for the standard error and test at a 5% significance level.

# Separating the data for control and test groups
control_group = merged_df[merged_df['group'] == 'A']
test_group = merged_df[merged_df['group'] == 'B']

# Calculate conversion rates for control and test groups
p_control = control_group['converted'].mean()
p_test = test_group['converted'].mean()

# Calculate pooled proportion
p_pooled = (control_group['converted'].sum() + test_group['converted'].sum()) / (len(control_group) + len(test_group))

# Calculate standard error using pooled proportion
se_pooled = (p_pooled * (1 - p_pooled) * (1/len(control_group) + 1/len(test_group))) ** 0.5

# Calculate z-score for the difference in proportions
z = (p_test - p_control) / se_pooled

# Calculate p-value
p_value = 2 * (1 - norm.cdf(abs(z)))

z, p_value

"""
Given that the p-value is much less than the significance level of 0.05, we reject the null hypothesis. This means there is a statistically significant difference in the conversion rates between the two groups.
"""

# 2. Calculate the 95% confidence interval for the difference in the conversion rate between the treatment and control groups (treatment - control). We'll use the normal distribution and unpooled proportions for the standard error.

# Calculate standard error using unpooled proportions
se_unpooled = ((p_control * (1 - p_control) / len(control_group)) + (p_test * (1 - p_test) / len(test_group))) ** 0.5

# Calculate the 95% confidence interval for the difference in proportions
diff = p_test - p_control
margin_of_error = norm.ppf(0.975) * se_unpooled

confidence_interval = (diff - margin_of_error, diff + margin_of_error)

confidence_interval

"""
The 95% confidence interval for the difference in the conversion rate between the treatment and control groups (treatment - control) is: (0.00349,0.01065)
This means that we are 95% confident that the difference in conversion rates between the test group (with the banner) and the control group (without the banner) lies within this interval.
"""

# 3. Conduct a hypothesis test to determine if there's a significant difference in the average amount spent per user between the two groups. We'll use the t-distribution and assume unequal variances.

# Conduct a t-test for the difference in average amount spent per user between the two groups
t_stat, p_value_spent = ttest_ind(test_group['spent'], control_group['spent'], equal_var=False)

t_stat, p_value_spent

"""
The results of the hypothesis test for the difference in average amount spent per user between the control and test groups are:

T-statistic: 0.0682
P-value: 0.9456

Given that the p-value is much greater than the significance level of 0.05, we fail to reject the null hypothesis. This indicates that there isn't a statistically significant difference in the average amount spent per user between the two groups.
"""

# 4. Calculate the 95% confidence interval for the difference in the average amount spent per user between the treatment and control groups (treatment - control). We'll use the t-distribution and assume unequal variances.


# Calculate means and standard deviations for the two groups
mean_control = control_group['spent'].mean()
mean_test = test_group['spent'].mean()
std_control = control_group['spent'].std(ddof=1)
std_test = test_group['spent'].std(ddof=1)

# Calculate the standard error for the difference in means
se_diff = np.sqrt((std_control**2 / len(control_group)) + (std_test**2 / len(test_group)))

# Calculate the degrees of freedom for the t-distribution
df = ((std_control**2 / len(control_group) + std_test**2 / len(test_group))**2) / \
     ((std_control**2 / len(control_group))**2 / (len(control_group) - 1) + 
      (std_test**2 / len(test_group))**2 / (len(test_group) - 1))

# Calculate the 95% confidence interval for the difference in means using the t-distribution
diff_means = mean_test - mean_control
margin_of_error_spent = se_diff * ttest_ind(test_group['spent'], control_group['spent'], equal_var=False)[0]

confidence_interval_spent = (diff_means - margin_of_error_spent, diff_means + margin_of_error_spent)

confidence_interval_spent

"""
The 95% confidence interval for the difference in the average amount spent per user between the treatment and control groups (treatment - control) is:

( 0.0 , 0.0317 )

This means that we are 95% confident that the difference in average amounts spent by users between the test group (with the banner) and the control group (without the banner) lies within this interval.
"""

# Part 3 Visualizing the Statistics

# Visual 1
#Comparing the conversion rate and average amount spent between the test groups

# Set the aesthetics for the plots
sns.set_style("whitegrid")

# Create a visualization to compare the conversion rate and average amount spent between the test groups
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Plot for conversion rate
sns.barplot(x='group', y='converted', data=merged_df, ax=axes[0], errorbar=None)
axes[0].set_title('Conversion Rate by Group')
axes[0].set_ylabel('Conversion Rate')
axes[0].set_xlabel('Group')

# Plot for average amount spent
sns.barplot(x='group', y='spent', data=merged_df, ax=axes[1], errorbar=None)
axes[1].set_title('Average Amount Spent by Group')
axes[1].set_ylabel('Average Amount Spent ($)')
axes[1].set_xlabel('Group')

plt.tight_layout()
plt.show()

"""
The visualizations provide the following insights:

Conversion Rate by Group:
Both the control (A) and test (B) groups show similar conversion rates. However, the test group has a slightly higher conversion rate than the control group.

Average Amount Spent by Group:
The average amount spent by users in both groups appears to be nearly identical, with no noticeable difference between the control and test groups.

"""

# Visual 2
# Visualize the distribution of the amount spent per user for each group
# Create a visualization for the distribution of the amount spent per user for each group
plt.figure(figsize=(12, 6))
sns.histplot(merged_df, x='spent', hue='group', element='step', stat='probability', common_norm=False, kde=True)
plt.title('Distribution of Amount Spent per User by Group')
plt.xlabel('Amount Spent ($)')
plt.ylabel('Probability Density')
plt.show()

""" 
The distribution plot shows the amount spent per user for both groups:

For the majority of users, the amount spent is close to $0, indicating that many users do not make a purchase.

Both the control (A) and test (B) groups show a similar distribution for the amount spent by users, with only slight variations.

There are a few users who spent higher amounts, but these instances are rare.

"""

# Visual 3
# Test Metrics (Conversion rate, Average amount spent) and the user’s device

# Create visualizations to explore the relationship between the test metrics and the user’s device
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Plot for conversion rate by device
sns.barplot(x='device', y='converted', hue='group', data=merged_df, ax=axes[0], errorbar=None)
axes[0].set_title('Conversion Rate by Device')
axes[0].set_ylabel('Conversion Rate')
axes[0].set_xlabel('Device')

# Plot for average amount spent by device
sns.barplot(x='device', y='spent', hue='group', data=merged_df, ax=axes[1], errorbar=None)
axes[1].set_title('Average Amount Spent by Device')
axes[1].set_ylabel('Average Amount Spent ($)')
axes[1].set_xlabel('Device')

plt.tight_layout()
plt.show()

""" 
The visualizations provide insights into the relationship between test metrics and the user's device:

Conversion Rate by Device:

    Both iOS (I) and Android (A) users in the test group (B) show a slightly higher conversion rate than their counterparts in the control group (A).

    iOS users have a higher conversion rate than Android users in both the control and test groups.

Average Amount Spent by Device:

    The average amount spent by users is slightly higher for iOS users in both groups compared to Android users.

    The difference in average amount spent between the control and test groups is minimal for both device types.
"""

# Visual 4
# Test Metrics by Gender
# Create visualizations to explore the relationship between the test metrics and the user’s gender

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Plot for conversion rate by gender
sns.barplot(x='gender', y='converted', hue='group', data=merged_df, ax=axes[0], errorbar=None)
axes[0].set_title('Conversion Rate by Gender')
axes[0].set_ylabel('Conversion Rate')
axes[0].set_xlabel('Gender')

# Plot for average amount spent by gender
sns.barplot(x='gender', y='spent', hue='group', data=merged_df, ax=axes[1], errorbar=None)
axes[1].set_title('Average Amount Spent by Gender')
axes[1].set_ylabel('Average Amount Spent ($)')
axes[1].set_xlabel('Gender')

plt.tight_layout()
plt.show()


""" 
The visualizations provide insights into the relationship between test metrics and the user's gender:

Conversion Rate by Gender:

    Males (M) in both the control and test groups have a slightly higher conversion rate than females (F).

    The difference in conversion rate between the control (A) and test (B) groups is marginal across genders.

    Users who identify as "other" (O) have a conversion rate in between that of males and females.

Average Amount Spent by Gender:

    Males tend to spend a bit more on average than females in both the control and test groups.

    The difference in average amount spent between the control and test groups is minimal across all gender categories.
"""

# Visual 5
# Test Metrics and the User's Country
# Create visualizations to explore the relationship between the test metrics and the user’s country

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 12))

# Plot for conversion rate by country
sns.barplot(x='country', y='converted', hue='group', data=merged_df, ax=axes[0], errorbar=None)
axes[0].set_title('Conversion Rate by Country')
axes[0].set_ylabel('Conversion Rate')
axes[0].set_xlabel('Country')

# Plot for average amount spent by country
sns.barplot(x='country', y='spent', hue='group', data=merged_df, ax=axes[1], errorbar=None)
axes[1].set_title('Average Amount Spent by Country')
axes[1].set_ylabel('Average Amount Spent ($)')
axes[1].set_xlabel('Country')

plt.tight_layout()
plt.show()

""" 
The visualizations provide insights into the relationship between test metrics and the user's country:

Conversion Rate by Country:

    The conversion rate varies across countries.

    For most countries, the test group (B) has a higher conversion rate than the control group (A), with notable differences observed for countries like BEL, BRA, and DEU.

    However, for some countries like CAN and USA, the control group has a slightly higher conversion rate than the test group.

Average Amount Spent by Country:

    The average amount spent by users varies significantly across countries.

    Countries like AUS, BRA, and CAN have users who spend more on average compared to users from other countries.

    The difference in average amount spent between the control and test groups across countries is minimal, with some exceptions such as CAN.
"""

# Visual 6
# Confidence intervals for the difference in conversion rate and the difference in average amount spent
# Visualize the Confidence Intervals

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Confidence interval for conversion rate
axes[0].errorbar(x=['Conversion Rate'], y=[diff], yerr=[margin_of_error], fmt='o', color='blue', capsize=5)
axes[0].hlines(0, xmin=-0.5, xmax=0.5, colors='red', linestyles='--')
axes[0].set_xlim(-0.5, 0.5)
axes[0].set_title('95% CI for Difference in Conversion Rate')
axes[0].set_ylabel('Difference (Test - Control)')

# Confidence interval for average amount spent
axes[1].errorbar(x=['Average Amount Spent'], y=[diff_means], yerr=[margin_of_error_spent], fmt='o', color='blue', capsize=5)
axes[1].hlines(0, xmin=-0.5, xmax=0.5, colors='red', linestyles='--')
axes[1].set_xlim(-0.5, 0.5)
axes[1].set_title('95% CI for Difference in Average Amount Spent')
axes[1].set_ylabel('Difference ($, Test - Control)')

plt.tight_layout()
plt.show()

""" 
The visualizations depict the 95% confidence intervals for the difference in metrics between the test and control groups:

95% CI for Difference in Conversion Rate:

    The blue dot represents the observed difference in conversion rates between the test and control groups.

    The blue lines depict the 95% confidence interval for this difference.

    The red dashed line at 0 represents no difference. Since the entire confidence interval is above this line, it suggests a positive difference in conversion rates in favor of the test group.

95% CI for Difference in Average Amount Spent:

    The blue dot represents the observed difference in average amounts spent between the test and control groups.

    The blue lines depict the 95% confidence interval for this difference.

    The red dashed line at 0 represents no difference. The confidence interval straddles this line, suggesting that there may not be a significant difference in average amounts spent between the groups.
"""



