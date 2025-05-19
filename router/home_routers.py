from all_imports import *
from flask import Blueprint
from werkzeug.utils import secure_filename
from flask import send_from_directory

host = Blueprint('host', __name__)

@host.route('/')
def index():
    video_path = os.path.join('uploads', 'videos')
    videos = []
    if os.path.exists(video_path):
        for filename in os.listdir(video_path):
            if filename.lower().endswith(('mp4', 'mkv', 'avi')):
                videos.append({'id': filename, 'title': filename})
    return render_template('index.html', videos=videos)

@host.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        video_file = request.files.get('video_file')
        image_file = request.files.get('image_file')

        # Пути
        video_path = os.path.join('uploads', 'videos')
        image_path = os.path.join('uploads', 'images')

        # Создаём папки, если их нет
        os.makedirs(video_path, exist_ok=True)
        os.makedirs(image_path, exist_ok=True)

        # Сохраняем видео
        if video_file and video_file.filename != '':
            video_filename = secure_filename(video_file.filename)
            video_file.save(os.path.join(video_path, video_filename))

        # Сохраняем обложку
        if image_file and image_file.filename != '':
            image_filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(image_path, image_filename))

        return 'Файл(ы) загружены!'

    return render_template('upload.html')

@host.route('/video/<filename>')
def video_stream(filename):
    # Стриминг видеофайла из папки uploads/videos
    return send_from_directory(os.path.join('uploads', 'videos'), filename)

@host.route('/watch/<video_id>')
def watch(video_id):
    # Передаём ссылку на видеофайл в шаблон
    video_url = url_for('host.video_stream', filename=video_id)
    return render_template('watch.html', video_id=video_id, videos=[{'id': video_id, 'url': video_url}])


# Добавляем стрименг видео

