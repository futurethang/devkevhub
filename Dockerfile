# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
# COPY requirements.txt /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

ENV PYTHONPATH=/app

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the maintainer label
# LABEL maintainer="itskmyoo <itskmyoo@gmail.com>"

# Run main.py when the container launches
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
# CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 80"]
