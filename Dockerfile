# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application
COPY app.py .

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
