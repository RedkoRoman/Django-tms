from celery import Celery
from celery.schedules import crontab

celery_app = Celery('blog', broker='redis://redis:6379/0')

# Загружаем сеттинги из джанги
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживает и регистрирует задачи из всех файлов tasks.py
celery_app.autodiscover_tasks()

# конфиг для селери бит (запуск задач по расписанию)
celery_app.conf.beat_schedule = {
    'delete_deleted_books': {
        'task': 'rest.tasks.delete_deleted_books',
        'schedule': crontab(day_of_month='1', hour='0', minute='0'),  # в первый день месяца в 00:00
        # 'schedule': crontab(minute='*'),  # каждую минуту
    }
}
