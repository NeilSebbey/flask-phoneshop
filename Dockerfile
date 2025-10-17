FROM python:3.12-slim

# Set work directory
WORKDIR /ns-cad-fonexpert-demo

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask app folder into container
COPY . .

# Run Gunicorn
CMD ["gunicorn", "app:app", \
     "--workers=3", "--threads=2", \
     "--worker-class=gthread", "--timeout=120", \
     "--graceful-timeout=30", "--keep-alive=5", \
     "--preload", "--bind", "0.0.0.0:8001"]
