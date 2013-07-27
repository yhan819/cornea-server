from cornea import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    publisher = db.Column(db.String(64))
    time = db.Column(db.DateTime)
    data = db.Column(db.String, nullable=True, default='')
    uploaded = db.Column(db.Integer)

    def __init__(self, publisher, time, data):
        self.publisher = publisher
        self.time = time
        self.data = data

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    visit = db.Column(db.Integer)
    last_updated = db.Column(db.DateTime)

    def __init__(self, visit, last_updated):
        self.visit = visit
        self.last_updated = last_updated
