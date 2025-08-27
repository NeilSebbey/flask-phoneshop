FROM python:3.12-slim

# Set work directory
WORKDIR /ns-cad-fonexpert-demo

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask app folder into container
COPY . .

# Run Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8001", "app:app"]
