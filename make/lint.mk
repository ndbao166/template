.PHONY: lint
lint:
	@echo "🔍 Checking uv.lock file integrity..."
	uv lock --check
	@echo "🔍 Running ruff linter..."
	uv run ruff check app
	@echo "🔍 Running pylint analysis..."
	uv run pylint app
	@echo "🔍 Running mypy type checking..."
	uv run mypy app
	@echo "🎉 ALL LINTING CHECKS PASSED SUCCESSFULLY!"

.PHONY: fix
fix:
	@echo "🚀 STARTING CODE FORMATTING AND FIXING..."
	uv run ruff format app
	uv run ruff check --fix app

.PHONY: clean
clean:
	@echo "🚀 CLEANING PROJECT FILES..."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . | grep -E '(\.mypy_cache|\.ruff_cache|__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf

