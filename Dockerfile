# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Run the application
CMD ["python", "import2.py"]
