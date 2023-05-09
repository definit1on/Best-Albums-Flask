import sqlite3

DB_NAME = 'besteveralbums_m2m.sqlite3'

QUERY1 = '''
SELECT artists.name as name,
COUNT(albums.id) as count_albums,
SUM(albums.charts) as sum_charts,
artists.id as id,
artists.img as img 
FROM artists
INNER JOIN albums
ON albums.artist_id = artists.id
GROUP BY artists.id
ORDER BY artists.name DESC;
'''

def get_artists_for_index():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        data = cur.execute(QUERY1).fetchall()
        data = [dict(row) for row in data]
        return data

QUERY2 = '''
SELECT artists.name as name,
artists.id as id,
artists.img as img
FROM artists
WHERE artists.id == ?;
'''

QUERY3 = '''
SELECT albums.name as name,
albums.charts as charts,
albums.year as year
FROM albums	
WHERE albums.artist_id == ?
ORDER BY year;
'''

QUERY7 = '''
SELECT genres.name as name,
genres.id as id
FROM artists_genres
INNER JOIN genres
ON artists_genres.genre_id == genres.id
INNER JOIN artists
ON artists_genres.artist_id == artists.id
WHERE artists.id == ?
ORDER BY name;
'''

def get_artist_albums_genres_for_artist_detail(pk):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        data1 = cur.execute(QUERY2, (pk,)).fetchone()
        data1 = dict(data1)
        data2 = cur.execute(QUERY3, (pk,)).fetchall()
        data2 = [dict(row) for row in data2]
        data3 = cur.execute(QUERY7, (pk,)).fetchall()
        data3 = [dict(row) for row in data3]
        return data1, data2, data3

QUERY4 = '''
SELECT genres.name as name,
genres.id as id,
COUNT(artists.id) as count_artists
FROM artists_genres
INNER JOIN genres
ON artists_genres.genre_id == genres.id
INNER JOIN artists
ON artists_genres.artist_id == artists.id
GROUP BY genres.id
ORDER BY name;
'''

def get_genres_for_index():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        data = cur.execute(QUERY4).fetchall()
        data = [dict(row) for row in data]
        return data

QUERY5 = '''
SELECT genres.name as name,
genres.id as id
FROM genres
WHERE genres.id == ?;
'''

QUERY6 = '''
SELECT artists.name as name,
artists.id as id,
artists.img as img
FROM artists_genres
INNER JOIN genres
ON artists_genres.genre_id == genres.id
INNER JOIN artists
ON artists_genres.artist_id == artists.id
WHERE genres.id == ?
ORDER BY name;
'''

def get_genre_artist_for_genre_detail(pk):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        data1 = cur.execute(QUERY5, (pk,)).fetchone()
        data1 = dict(data1)
        data2 = cur.execute(QUERY6, (pk,)).fetchall()
        data2 = [dict(row) for row in data2]
        return data1, data2

QUERY8 = '''
INSERT INTO albums (name, artist_id, year, charts)
VALUES 
(?, ?, ?, ?)
'''

def insert_new_album(name, artist_id, year, charts):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(QUERY8, (name, artist_id, year, charts))
        conn.commit()

if __name__ == '__main__':
    # print(get_artists_for_index())
    # print(get_artist_albums_for_artist_detail(pk=9))
    # print(get_genres_for_index())
    print(get_artist_albums_genres_for_artist_detail(pk=7))