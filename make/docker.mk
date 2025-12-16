
.PHONY: up
up:
	@echo "🚀 Starting all services..."
	docker compose -f docker/docker-compose.yml --project-directory . up -d --build
	@echo "✅ All services started!"

.PHONY: down
down:
	@echo "🛑 Stopping all services..."
	docker compose -f docker/docker-compose.yml --project-directory . down
	@echo "✅ All services stopped!"

.PHONY: logs
logs:
	@echo "📋 Showing logs..."
	docker compose -f docker/docker-compose.yml --project-directory . logs -f
	@echo "✅ Logs shown!"

.PHONY: restart
restart:
	@echo "🔄 Restarting all services..."
	docker compose -f docker/docker-compose.yml --project-directory . restart
	@echo "✅ All services restarted!"

.PHONY: rebuild
rebuild:
	@echo "🔄 Rebuilding all services..."
	docker compose -f docker/docker-compose.yml --project-directory . build --no-cache
	@echo "✅ All services rebuilt!"

.PHONY: remove-images
remove-images:
	@echo "🔄 Removing all images..."
	docker compose -f docker/docker-compose.yml --project-directory . down --rmi all
	@echo "✅ All images removed!"