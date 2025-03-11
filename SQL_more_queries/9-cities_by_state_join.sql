-- Use a JOIN to get the name of the state for each city.

SELECT 
    c.id, 
    c.name AS name, 
    s.name AS name
FROM 
    cities c
JOIN 
    states s ON c.state_id = s.id
ORDER BY 
    c.id ASC;