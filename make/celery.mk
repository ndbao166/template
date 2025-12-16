.PHONY: celery-worker
celery-worker:
	@echo "🚀 Starting Celery Worker..."
	export PYTHONPATH=./ && uv run celery -A app.server.celery_worker worker --loglevel=info --concurrency=4


.PHONY: celery-flower
celery-flower:
	@echo "🚀 Starting Celery Flower..."
	export PYTHONPATH=./ && uv run celery -A app.server.celery_worker flower --port=5555
