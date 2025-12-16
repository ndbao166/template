# API Template

Base template chuẩn cho FastAPI + React + MongoDB + Redis + Celery

## 🚀 Development (Local)

### Setup
```bash
# Tạo file .env
PORT=8000
HOST=0.0.0.0
CONFIG_PATH=config/dev.yaml

MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_USERNAME=admin
MONGODB_PASSWORD=oneforall
MONGODB_DATABASE=db_app

REDIS_URL_MESSAGE_BROKER=redis://localhost:6379/0
VITE_API_BASE_URL=http://localhost:8000
```

### Run Services
```bash
make dev          # Backend FastAPI (dev mode)
make run_ui       # Frontend React
make celery-worker   # Celery worker
make celery-flower   # Celery monitor (port 5555)
```

## 🐳 Docker Compose (Production)

### Setup
```bash
# File .env cho Docker
REDIS_URL_MESSAGE_BROKER=redis://pi_redis:6379/0
VITE_API_BASE_URL=/api
```

### Commands
```bash
make up           # Start all (nginx proxy)
make down         # Stop all
make logs         # View logs
make restart      # Restart services
make rebuild      # Rebuild no cache
```

## 📝 Notes
- **Dev**: Run trực tiếp với makefile, connect localhost
- **Docker**: Nginx làm proxy, services connect qua container names

