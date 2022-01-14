from flask import Flask,jsonify,request
import csv

all_movies = []

with open('movies.csv',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_movies = data[1:]

liked_movies = []
unliked_movies = []
unwatched_movies = []

app = Flask(__name__)

@app.route('/get-movies')
def get_movies():
 return jsonify({
      "data" : all_movies[0],
      'status' : "Success"
  }),201

@app.route('/liked-movies',methods=['POST'])
def liked_movie():
    movies = all_movies[0]
    all_movie = all_movies[1:]
    liked_movies.append(movies)
    return jsonify({
        'status' : "Success"
    })

@app.route('/unliked-movies',methods=['POST'])
def unliked_movie():
    movies = all_movies[0]
    all_movie = all_movies[1:]
    unliked_movies.append(movies)
    return jsonify({
        'status' : 'Success'
    }),201

@app.route('/unwatched-movies',methods=['POST'])
def unwatched_movie():
    movies = all_movies[0]
    all_movie = all_movies[1:]
    unliked_movies.append(movies)
    return jsonify({
        'status' : 'Success'
    }),201

if __name__ == "__main__":
    app.run()
