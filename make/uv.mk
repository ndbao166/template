.PHONY: install_uv
install_uv:
	@echo "🚀 INSTALLING UV..."
	curl -LsSf https://astral.sh/uv/install.sh | sh

.PHONY: uninstall_uv
uninstall_uv:
	@echo "🚀 UNINSTALLING UV..."
	uv cache clean
	rm ~/.local/bin/uv ~/.local/bin/uv run

.PHONY: install
install:
	@echo "🚀 INSTALLING ENVIRONMENT..."
	uv lock
	uv sync --locked --all-extras --dev
