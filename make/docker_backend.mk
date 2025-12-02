.PHONY: docker-build-backend
docker-build-backend:
	@echo "🔨 Building Backend image"
	docker build -t api -f docker/backend/Dockerfile .

.PHONY: docker-run-backend
docker-run-backend:
	@echo "🚀 Running Backend container"
	docker run -d --name api --publish 8000:8000 --env-file .env api

.PHONY: docker-restart-backend
docker-restart-backend:
	@echo "🔄 Restarting Backend container"
	docker restart vplay-backend

.PHONY: docker-stop-backend
docker-stop-backend:
	@echo "🛑 Stopping Backend container"
	docker stop api || true

.PHONY: docker-remove-backend
docker-remove-backend:
	@echo "🗑️ Removing Backend container"
	docker rm -f api || true

.PHONY: docker-logs-backend
docker-logs-backend:
	@echo "📋 Backend logs"
	docker logs -f api

.PHONY: docker-exec-backend
docker-exec-backend:
	@echo "🔧 Executing Backend container"
	docker exec -it api /bin/sh

.PHONY: docker-remove-image-backend
docker-remove-image-backend:
	@echo "🗑️ Removing Backend image"
	docker rmi -f api || true

.PHONY: docker-clear-backend
docker-clear-backend:
	@echo "🧹 Clearing Backend container"
	make docker-stop-backend
	make docker-remove-backend
	make docker-remove-image-backend

.PHONY: docker-view
docker-view:
	@echo "🧹 Clearing Docker cache"
	docker ps
	docker images

.PHONY: docker-clear-cache
docker-clear-cache:
	@echo "🧹 Clearing Docker cache"
	docker system prune

# # 1. Login
# docker login
# # 2. Build (đặt tên tạm)
# docker build -t my-web:latest .
# # 3. Tag (đổi tên chuẩn form user/repo)
# docker tag my-web:latest johndoe/my-web-server:v1.0.0
# # 4. Push
# docker push johndoe/my-web-server:v1.0.0