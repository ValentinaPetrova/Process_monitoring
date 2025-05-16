# 1. Use a lightweight Python base image
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /process_monitoring

# 3. Copy your app code into the container
COPY . /process_monitoring/

# 4. Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose port 5000 for Flask API
EXPOSE 5000

# 6. Set the command to run your Flask app
CMD ["python", "restapi.py"]
