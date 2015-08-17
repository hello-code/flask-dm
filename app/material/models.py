from app import db

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matnr = db.Column(db.String(10), unique=True)
    matdb = db.Column(db.String(255))

    def __init__(self, matnr, matdb):
        self.matnr = matnr
        self.matdb = matdb

    def __repr__(self):
        return 'Material %s' % self.matnr
