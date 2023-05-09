from flask import Flask, render_template, url_for, request, redirect
from database_tools import *

app = Flask(__name__)

@app.route('/')
def index():
    artists = get_artists_for_index()
    genres = get_genres_for_index()
    return render_template('index.html',
                           artists=artists,
                           genres=genres)

@app.route('/artist/<int:pk>')
def artist_detail(pk):
    artist, albums, genres = get_artist_albums_genres_for_artist_detail(pk=pk)
    return render_template('artist_detail.html',
                           artist=artist,
                           albums=albums,
                           genres=genres)

@app.route('/genre/<int:pk>')
def genre_detail(pk):
    genre, artists = get_genre_artist_for_genre_detail(pk=pk)
    return render_template('genre_detail.html',
                           genre=genre,
                           artists=artists)

@app.route('/add/album/<int:pk>')
def add_album(pk):
    name = request.form.get('name')
    year = request.form.get('year')
    charts = request.form.get('charts')
    if name and year and charts:
        insert_new_album(name=name,
                         artist_id=pk,
                         year=year,
                         charts=charts)
    return redirect(url_for('artist_detail', pk=pk))

if __name__ == '__main__':
    app.run(port=5001, debug=True)




































