from extensions import db


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)
    video_file = db.Column(db.String(120), unique=False, nullable=False)
    image_file = db.Column(db.String(120), unique=False, nullable=True)
    views = db.Column(db.Integer, unique=False, nullable=False, default=0)
    likes = db.Column(db.Integer, unique=False, nullable=False, default=0)
    dislikes = db.Column(db.Integer, unique=False, nullable=False, default=0)