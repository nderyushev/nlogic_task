FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    g++ \
    libpq-dev \
    && apt-get clean \
    && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]