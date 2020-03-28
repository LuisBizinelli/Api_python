import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.serie.models import Serie
from my_app import api, db

serie = Blueprint('serie',__name__)

parser = reqparse.RequestParser()
parser.add_argument('title',type=str)
parser.add_argument('genre',type=str)
parser.add_argument('seasons',type=int)
parser.add_argument('imdbRating',type=float)
parser.add_argument('isActive',type=bool)

@serie.route("/")
@serie.route("/home")
def home():
  return "Catálogo de Séries"

class SerieAPI(Resource):
  def get(self,id=None,page=1):
    if not id:
      series = Serie.query.paginate(page,10).items
    else:
      series = [Serie.query.get(id)]
    if not series:
      abort(404)
    res = {}
    for s in series:
      res[s.id] = {
        'title': s.title,
        'genre': s.genre,
        'seasons': s.seasons,
        'imdbRating': str(s.imdbRating),
        'isActive': s.isActive,
      }
    return json.dumps(res)

  def post(self):
    args = parser.parse_args()
    title = args['title']
    genre = args['genre']
    seasons = args['seasons']
    imdbRating = args['imdbRating']
    isActive = args['isActive']

    s = Serie(title,genre,seasons,imdbRating,isActive)
    db.session.add(s)
    db.session.commit()
    res = {}
    res[s.id] = {
        'title': s.title,
        'genre': s.genre,
        'seasons': s.seasons,
        'imdbRating': str(s.imdbRating),
        'isActive': s.isActive,
      }
    return json.dumps(res)

api.add_resource(
  SerieAPI,
  '/api/serie',
  '/api/serie/<int:id>',
  '/api/serie/<int:id>/<int:page>'
)
