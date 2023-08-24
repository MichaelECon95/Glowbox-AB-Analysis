DROP VIEW IF EXISTS
test_data;
-- Create a view named 'test_data'

CREATE VIEW test_data AS

- Start with a Common Table Expression (CTE) to aggregate the activity dataset to get total spending per user

WITH agg_activity AS (
SELECT
uid,
SUM(spent) AS total_spent -- Calculate total spending for each user
FROM activity
GROUP BY uid -- Group the activity data by user ID
)

-- Main query to join users, groups, and aggregated activity datasets

SELECT
u.id AS user_id, -- Select user ID from users table
u.country, -- Select country from users table
u.gender, -- Select gender from users table
g.device, -- Select device from groups table
g."group", -- Select test group from groups table (using double quotes since 'group' is a reserved keyword)
CASE
WHEN COALESCE(a.total_spent, 0) > 0 THEN 1 -- Check if the user made a purchase
ELSE 0
END AS converted, -- Create a binary 'converted' column indicating if the user converted or not
COALESCE(a.total_spent, 0) AS total_spent -- Get total spending for each user, set to 0 if no purchases were made
FROM users u
INNER JOIN groups g ON u.id = g.uid -- Join users and groups tables on user ID
LEFT JOIN agg_activity a ON u.id = a.uid -- Left join with aggregated activity data to get spending details
