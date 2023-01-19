.ONESHELL:
py := poetry run
django := $(py) python manage.py


hello:
	@echo "Hello! Please look for doc and entry correct argument after 'make'."

# Make migrations and apply thay
.PHONY: migrate
migrate:
	@$(django) makemigrations app
	@$(django) migrate

# Run application
.PHONY: run
run:
	@$(django) runserver

# Flush database and than fill database with seed
.PHONY: seed
seed:
	@$(django) flush --no-input
	@$(django) seed

# Only flush database
.PHONY: flush
flush:
	@$(django) flush --no-input

# Only fill database
.PHONY: fill
fill:
	@$(django) seed

