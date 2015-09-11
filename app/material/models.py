from app import db

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matnr = db.Column(db.String(15), unique=True)
    matdb = db.Column(db.String(255))
    bun = db.Column(db.String(3))

    def __init__(self, matnr, matdb, bun):
        self.matnr = matnr
        self.matdb = matdb
        self.bun = bun

    def __repr__(self):
        return 'Material %s' % self.matnr
