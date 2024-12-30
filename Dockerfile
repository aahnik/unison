# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=temple_web.settings \
    DJANGO_DEBUG=False

WORKDIR /app

# Install system dependencies and clean up in one layer
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
# First upgrade pip
RUN pip install --upgrade pip && \
    # Then install requirements without hash checking
    pip install --no-cache-dir --no-deps -r requirements.txt && \
    # Finally install additional packages
    pip install --no-cache-dir gunicorn==21.2.0 psycopg2-binary==2.9.9

# Copy project files
COPY . .

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh


# Create a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app

# Create data directory with correct permissions
RUN mkdir -p /data && \
    chown -R appuser:appuser /data

# USER appuser

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

VOLUME ["/data"]

# Expose port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
