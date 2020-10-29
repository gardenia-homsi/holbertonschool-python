-- Select with right Join and double order by.
SELECT tv_genres.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
