class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/videos.db'
    Folder = 'uploads'
    UPLOAD_FOLDER = Folder
    ALLOWED_EXTENSIONS = set(['mp4', 'mkv', 'avi'])
    MAX_CONTENT_LENGTH = 1600 * 1024 * 1024