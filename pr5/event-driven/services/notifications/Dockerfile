FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && adduser --system app
COPY app.py .
USER app
CMD ["python", "app.py"]
