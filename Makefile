.EXPORT_ALL_VARIABLES:
COMPOSE_FILE ?= docker-compose.yaml
TEST_COMPOSE_FILE ?= docker-compose.test.yaml

# билдим докер имейдж с Dockerfile
.PHONY: docker-build
docker-build:
	docker build --file=Dockerfile .

# запуск докер контейнеров из файла COMPOSE_FILE
.PHONY: docker-up
docker-up:
	docker-compose -f $(COMPOSE_FILE) --env-file=.env up -d --build
	docker-compose ps

# отображение логов
.PHONY: docker-logs
docker-logs:
	docker-compose logs --follow

# остановить контейнеры
.PHONY: docker-down
docker-down:
	docker-compose down

# чистить кэш контейнеров и вольюмов
.PHONY: docker-prune
docker-prune:
	docker container prune -f
	docker volume prune -f

# чистить кэш
.PHONY: docker-system-prune
docker-system-prune:
	docker system prune -f

# зайти в контейнер web
.PHONY: docker-bash
docker-bash:
	docker-compose -f $(COMPOSE_FILE) exec web bash

# cоздать файл миграций
.PHONY: makemigrations
makemigrations:
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py makemigrations

# применять миграции
.PHONY: migrate
migrate:
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py migrate

# создать и принять миграции
.PHONY: migrations
migrations: makemigrations migrate

# прогнать тесты
.PHONY: tests
tests:
	docker-compose -f $(TEST_COMPOSE_FILE) --env-file=.test_env up --build