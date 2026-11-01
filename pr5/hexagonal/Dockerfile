FROM python:3.13-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.13-slim AS runtime
ENV PYTHONPATH=/app PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN addgroup --system app && adduser --system --ingroup app app
COPY --from=builder /install /usr/local
COPY core adapters config ./
USER app
EXPOSE 8081
CMD ["sh", "-c", "uvicorn config.app:app --host 0.0.0.0 --port ${PORT:-8081}"]
