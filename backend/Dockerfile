# Python resmi image
FROM python:3.11-slim

# Çalışma klasörü
WORKDIR /app

# Kodları container içine kopyala
COPY app.py .

# Port (dokümantasyon için)
EXPOSE 8080

# Uygulamayı başlat
CMD ["python", "app.py"]