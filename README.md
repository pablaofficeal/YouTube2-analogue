# 🎬 RhythmyMD — YouTube2-Style Видеохостинг на Flask

**RhythmyMD** — это аналог YouTube, разработанный на Python с использованием Flask, SQLAlchemy и Flask-Login.  
Проект создан в прямом эфире на YouTube — для кайфа, опыта и прокачки 🔥

---

## 🚀 Быстрый старт

### 📦 Зависимости

Перед запуском убедись, что установлен Python версии `3.12.9` или совместимой.

Установи необходимые библиотеки:

```bash
pip install flask flask_sqlalchemy flask_login python-dotenv
```
▶️ Запуск приложения
```bash
python3 app.py
```

📁 Структура проекта
```markdown
Free59/
├── models/
│   ├── main_start_db.py
│   ├── users/
│   │   └── main_user_db.py
│   └── video/
│       └── main_video_db.py
├── router/
│   ├── home_routers.py
│   └── uploads_routers.py
├── shemas/
│   └── main.txt
├── static/
│   └── css/
│       ├── app.css
│       ├── index.css
│       └── main.css
├── templates/
│   ├── index.html
│   ├── upload.html
│   └── watch.html
├── .gitignore
├── all_imports.py
├── app.py
├── extensions.py
├── main_router.py
└── README.md
```

✅ Что реализовано
- База данных на SQLAlchemy

- Модели пользователей и видео

- Авторизация с Flask-Login

- Формы загрузки и отображения видео

- Подключённые стили для фронта

- Роутинг с разными модулями Flask

- Стриминг и отображение видеофайлов


🔴 YouTube стрим
Проект разрабатывался вживую на стриме:
```📺 Смотреть запись
https://youtube.com/live/RiXmMTFoyk0?feature=share
```

Лицензия: MIT
Автор: @Павло (с YouTube стрима 😎)