from my_app import db

class Serie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255))
  genre = db.Column(db.String(255))
  seasons = db.Column(db.Integer)
  imdbRating = db.Column(db.Float(asdecimal=True))
  isActive = db.Column(db.Boolean())

  def __init__(self,title,genre,seasons,imdbRating,isActive):
    self.title = title
    self.genre = genre
    self.seasons = seasons
    self.imdbRating = imdbRating
    self.isActive = isActive

  def __repr_(self):
    return 'Serie {0}'.format(self.id)

