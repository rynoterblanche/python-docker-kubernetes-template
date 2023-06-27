POETRY_VERSION=1.5.1

.PHONY: setup
setup:
	@echo "== setup"
	# see: https://python-poetry.org/docs/#installation
	curl -sSL "https://install.python-poetry.org" | python3 - --version $(POETRY_VERSION)

.PHONY: install
install:
	@echo "== install"
	poetry install

.PHONY: unit-test
unit-test:
	@echo "== run unit tests"
	APP_ENV=unit-test poetry run pytest tests/unit

.PHONY: test
test: unit-test

.PHONY: run-product-service
run-product-service:
	@echo "== running product service"
	poetry run python ./src/product_service/app.py --config config.yml


