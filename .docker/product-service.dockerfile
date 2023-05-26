FROM python:3.11.3-alpine3.17 as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.4.2

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM base as development

COPY --from=builder /venv /venv
COPY src/  .
COPY .docker/config/product-service.development.yml /config/config.yml
COPY .docker/product_service_scripts/entrypoint.sh .
CMD ["./entrypoint.sh"]


# Possible start for production image
#FROM base as production
#
#COPY --from=builder /venv /venv
#COPY src/  .
#COPY deploy/web-app/product-service/entrypoint.sh .
#CMD ["./entrypoint.sh"]