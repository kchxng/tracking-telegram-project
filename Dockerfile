# Stage 1: Build environment (slim)
FROM python:3.9-slim AS builder

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Stage 2: Runtime environment (minimal)
FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /app/app .
CMD ["python", "app/main.py"]