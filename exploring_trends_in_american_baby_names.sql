-- Use this table for the answer to question 1:
-- List the overall top five names in alphabetical order and find out if each name is "Classic" or "Trendy."
-- Select first_name, the sum of babies who have ever had that name, and popularity_type
SELECT first_name, SUM(num),
-- Classify first names as 'Classic' or 'Trendy'
    CASE WHEN COUNT(year) > 50 THEN 'Classic'
        ELSE 'Trendy' END AS popularity_type
FROM baby_names
-- Group by first_name to use aggregate functions
GROUP BY first_name
-- Order the results alphabetically by first_name
ORDER BY first_name
-- Limit to the first 5 names
LIMIT 5;

-- Use this table for the answer to question 2:
-- What were the top 20 male names overall, and how did the name Paul rank?
-- RANK names by the sum of babies who have ever had that name (descending), aliasing as name_rank
SELECT
    RANK() OVER(ORDER BY SUM(num) DESC) AS name_rank,
    first_name, SUM(num)
FROM baby_names
-- Filter the data for results where sex equals 'M'
WHERE sex = 'M'
-- Group by first name, oder by rank, and limit to the top 20 
GROUP BY first_name
ORDER BY name_rank
LIMIT 20;

-- Use this table for the answer to question 3:
-- Which female names appeared in both 1920 and 2020?
-- Select first name and total occurrences
SELECT a.first_name, (a.num + b.num) AS total_occurrences
FROM baby_names a
JOIN baby_names b
-- Join on first name
ON a.first_name = b.first_name
-- Filter for the years 1920 and 2020 and sex equals 'F'
WHERE a.year = 1920 AND a.sex = 'F'
AND b.year = 2020 AND b.sex = 'F';