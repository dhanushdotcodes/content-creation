# Makefile for managing the project services

.PHONY: db-up db-down db-logs db-shell db-clear docker-clear db-init db-migrate db-generate help

# Default target
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  db-up         Spin up the PostgreSQL database in the background"
	@echo "  db-down       Stop and remove the PostgreSQL container"
	@echo "  db-logs       View logs from the PostgreSQL container"
	@echo "  db-shell      Open a psql shell inside the database container"
	@echo "  db-clear      Stop and remove containers, networks, and volumes"
	@echo "  docker-clear  Alias for db-clear"
	@echo "  db-init       Initialize Prisma"
	@echo "  db-migrate    Generate and apply migrations"
	@echo "  db-generate   Generate the Prisma client"

db-up:
	docker compose up -d

db-down:
	docker compose down

db-logs:
	docker compose logs -f

db-shell:
	docker compose exec postgres psql -U postgres -d faker_db

db-clear:
	docker compose down -v --remove-orphans

docker-clear: db-clear

db-init:
	bunx --bun prisma init

db-migrate:
	bunx --bun prisma migrate dev --name init

db-generate:
	bunx --bun prisma generate

db-push:
	bunx --bun prisma db push

db-seed:
	bunx --bun prisma db seed



