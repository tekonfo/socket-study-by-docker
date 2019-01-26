PROJECT = socket
COMPOSE_FILE = docker-compose.yml

.PHONY: start
start:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT) up -d --build

.PHONY: kill
kill:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT) kill
