# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=80

# Expose the port that the FastAPI app will be listening on
EXPOSE ${PORT}

# Run the FastAPI app with Uvicorn when the container is started
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
