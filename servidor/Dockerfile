# Usamos python slim que funciona nativo en M1 (ARM64)
FROM python:3.9-slim

WORKDIR /app

# Instalamos Flask
RUN pip install flask

# Copiamos el archivo servidor.py al contenedor
COPY servidor.py .

# Ejecutamos
CMD ["python", "servidor.py"]
