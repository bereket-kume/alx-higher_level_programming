-- 8-cities_of_california_subquery.sql
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities
WHERE state_id =(
    SELECT id FROM states
    WHERE name="California")
ORDER BY id;