from app import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Title: {self.title}, Description: {self.description}"