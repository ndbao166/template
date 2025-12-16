.PHONY: run
run:
	@echo "🚀 STARTING APPLICATION..."
	@echo "🌐 Starting FastAPI server..."
	export PYTHONPATH=./ && uv run app/server/main.py

.PHONY: dev
dev:
	@echo "🚀 RUNNING THE APPLICATION IN DEVELOPMENT MODE..."
	export PYTHONPATH=./ && uvicorn app.server.main:app --reload --host 0.0.0.0 --port 8000
	@echo "🎉 APPLICATION RUNNING SUCCESSFULLY IN DEVELOPMENT MODE!"
