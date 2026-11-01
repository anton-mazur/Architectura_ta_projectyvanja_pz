.PHONY: migrate test

migrate:
	docker compose run --rm api alembic upgrade head

test:
	pytest -q
