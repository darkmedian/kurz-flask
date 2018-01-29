# shortner/app/api/models.py


from app import db


class Shortner(db.Model):
    __tablename__ = "shortner"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(128), nullable=False)
    digest = db.Column(db.String(128), nullable=False)

    def __init__(self, url, digest):
        self.url = url
        self.digest = digest

    def to_json(self):
        return {
            'id': self.id,
            'url': self.url,
            'digest': self.digest,
        }
