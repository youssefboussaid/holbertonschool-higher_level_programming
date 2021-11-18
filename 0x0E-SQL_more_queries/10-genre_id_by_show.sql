-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_show.title, tv_show.genres.genre_id
FROM tv_show_genres INNER JOIN tv_show ON tv_show_genres.show_id = tv_show.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;