-- Select with where.
SELECT t.title
FROM tv_shows t
LEFT JOIN (SELECT tv_shows.id
	FROM tv_genres
	JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
	JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_genres.name = 'Comedy') s1
ON t.id = s1.id
WHERE s1.id IS NULL
ORDER BY t.title ASC;
