
FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/gitparthan/ci-cd-demo"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
