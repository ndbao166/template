from typing import Any

from app.server.celery_worker import celery_app


@celery_app.task(bind=True, name="run_pipeline")
def run_pipeline(_: Any) -> str:
    return "Pipeline run successfully"
