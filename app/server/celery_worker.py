from celery import Celery

from app.config import settings

REDIS_URL = settings.REDIS_URL_MESSAGE_BROKER

# Create Celery app
celery_app = Celery(
    "mas_eval",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

# Configure Celery
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Ho_Chi_Minh",
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes hard limit
    task_soft_time_limit=25 * 60,  # 25 minutes soft limit
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,
    task_acks_late=True,  # allow task to be acknowledged late
)
