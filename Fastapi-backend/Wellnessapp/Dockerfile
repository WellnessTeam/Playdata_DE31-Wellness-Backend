# Dockerfile for Wellnessapp (main API)
FROM python:3.9-slim

# Set the working directory
WORKDIR /Fastapi-backend

# Copy the requirements.txt file
COPY requirements.txt /Fastapi-backend/

# Install app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-jose
RUN pip install PyJWT
RUN pip install pytz
RUN pip install asyncpg

# Copy the rest of the application code
COPY ./Wellnessapp/app /Fastapi-backend

# Create a directory for storing log files
RUN chmod -R 755 /Fastapi-backend/Wellnessapp/app/dailylogtxt

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
