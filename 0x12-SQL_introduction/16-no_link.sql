-- SELECT rows with the same value.
SELECT score, name  FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
