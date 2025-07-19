# Use a Python base image
FROM python:3.11-slim

# Install system dependencies for TensorFlow and Ollama
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull the LLaMA model
RUN ollama pull llama3.2:latest

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start Ollama server in the background and run Streamlit
CMD ["sh", "-c", "ollama serve & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]