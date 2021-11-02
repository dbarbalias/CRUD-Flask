from app import db
from datetime import datetime


#create with db.create_all()
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)
    content = db.Column(db.String(200))

    def __repr__(self):
        return f'<Task {self.id}>'
