-- Display the max temperature of each state ordered by state name
SELECT State, MAX(temperature) AS max_temperature
FROM tablename
GROUP BY State
ORDER BY State;
