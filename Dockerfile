# Use the official Python image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn

# Copy application code
COPY . .

# Set environment variables
ENV PORT=8080

# Configure container startup
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8080"]

# Note: When deploying to Cloud Run, set these environment variables:
# - PROJECT_ID
# - RESOURCE_NAME
# Also ensure the Cloud Run service account has access to Secret Manager
