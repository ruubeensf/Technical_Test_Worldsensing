# Use Python 3.10 image as the base image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Change the working directory to /app
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application with Uvicorn server on 0.0.0.0:80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]