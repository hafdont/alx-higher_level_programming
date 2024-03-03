-- Select all cities of California from the cities table
SELECT cities.*
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
