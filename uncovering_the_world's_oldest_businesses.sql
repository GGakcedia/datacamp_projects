-- What is the oldest business on each continent?
SELECT bc.continent, bc.business, bc.year_founded, bc.country
FROM (
    SELECT business, year_founded, country, continent
    FROM businesses
    JOIN countries USING (country_code)
) bc
JOIN (SELECT continent, MIN(year_founded) AS year_founded
    FROM businesses
    JOIN countries 
    USING (country_code)
    GROUP BY continent
) c 
ON bc.continent = c.continent AND bc.year_founded = c.year_founded


-- How many countries per continent lack data on the oldest businesses
-- Does including the `new_businesses` data change this?
SELECT c.continent, COUNT(c.country_code) AS countries_without_businesses
FROM countries c
LEFT JOIN (
    SELECT * FROM businesses
    UNION ALL
    SELECT * FROM new_businesses
) b
ON c.country_code = b.country_code
WHERE b.business IS NULL
GROUP BY c.continent;

-- Which business categories are best suited to last over the course of centuries?
SELECT c.continent, cat.category, MIN(b.year_founded) AS year_founded
FROM businesses b
INNER JOIN categories cat ON b.category_code = cat.category_code
INNER JOIN countries c ON b.country_code = c.country_code
GROUP BY c.continent, cat.category
ORDER BY c.continent, cat.category;