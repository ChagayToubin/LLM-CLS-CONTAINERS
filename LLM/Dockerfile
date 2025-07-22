# Use Alpine Linux as base image
FROM python:3.11-slim
WORKDIR /app



COPY requirements.txt requirement.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8000

CMD ["uvicorn", "Server.App:app", "--host", "0.0.0.0", "--port", "8000"]
