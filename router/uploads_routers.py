from all_imports import *
from router.home_routers import host
from werkzeug.utils import secure_filename

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