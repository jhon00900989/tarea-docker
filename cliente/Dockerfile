FROM python:3.9-slim

WORKDIR /app

COPY cliente.py .

ENV SERVICE_URL=http://servidor-api:5000

CMD ["python", "cliente.py"]

