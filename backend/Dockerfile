# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose any required port (if your application uses one)
EXPOSE 5000

# Define the command to run your application (update this as per your app's entry point)
CMD ["python", "main.py"]

