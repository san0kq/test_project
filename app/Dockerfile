FROM python:3.12-alpine as requirements_stage

ENV PYTHONUNBUFFERED=1

WORKDIR /tmp

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN pip install poetry && poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-alpine as builder

RUN apk add --no-cache gcc musl-dev linux-headers

COPY --from=requirements_stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /app/requirements.txt

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /wheels /wheels

RUN pip install --no-cache /wheels/* \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]
