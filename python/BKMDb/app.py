from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre = db.Column(db.String(50), unique=False)
    starring = db.Column(db.String(200), unique=False)

    def __init__(self, title, year, rating, genre, starring):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre
        self.starring = starring


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('title', 'year', 'rating', 'genre', 'starring')


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# Endpoint for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to add new movie
@app.route('/movie/', methods=['POST'])
def add_movie():
    title = request.json['title']
    year = request.json['year']
    rating = request.json['rating']
    genre = request.json['genre']
    starring = request.json['starring']

    new_movie = Movie(title, year, rating, genre, starring)

    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.get(new_movie.id)

    return render_template('movies.html')

# Endpoint to query all movies
@app.route('/movies/', methods=['GET'])
def get_movies():
    all_movies = Movie.query.all()
    result = movies_schema.dump(all_movies)
    return render_template('movies.html', movies=result)

# Endpoint for querying a single movie
@app.route('/movie/<id>/', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    return movie_schema.jsonify(movie)

# Endpoint for updating a movie
@app.route('/movie/<id>/', methods=['PUT'])
def movie_update(id):
    movie = Movie.query.get(id)
    title = request.json['title']
    year = request.json['year']
    rating = request.json['rating']
    genre = request.json['genre']
    starring = request.json['starring']

    movie.title = title
    movie.year = year
    movie.rating = rating
    movie.genre = genre
    movie.starring = starring

    db.session.commit()
    return movie_schema.jsonify(movie)

# Endpoint for deleting a movie
@app.route('/movie/<id>/', methods=['DELETE'])
def movie_delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    return f'movie has been removed'


if __name__ == '__main__':
    app.run(debug=True)
