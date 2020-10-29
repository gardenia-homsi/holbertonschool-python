-- Select with where.
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_shows ts
JOIN tv_show_ratings tsr ON tsr.show_id = ts.id
GROUP BY ts.title ORDER BY rating DESC;
