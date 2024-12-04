FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY utilities.py utilities.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]