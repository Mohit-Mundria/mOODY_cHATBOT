🌈 Moody Chatbot: Your Emotion-Sensing Companion 🤖
Welcome to Moody Chatbot, a heartwarming, AI-powered conversational buddy that not only listens to what you say but also feels your emotions! Built with love and a sprinkle of tech magic, this chatbot uses deep learning to detect your emotions and responds with thoughtful replies powered by LLaMA 3.2. Whether you’re feeling joyful, sad, or surprised, Moody Chatbot is here to chat, comfort, or celebrate with you. 🎉
This project is a unique blend of TensorFlow for emotion prediction, Streamlit for a slick web interface, and Ollama for generating empathetic responses, all wrapped in a Docker container for easy deployment. Ready to dive into the world of emotional AI? Let’s get started!

🚀 What is Moody Chatbot?
Moody Chatbot is a web-based chatbot that:

Reads Your Emotions: Analyzes your text input to predict emotions like joy, sadness, love, anger, fear, or surprise using a TensorFlow model.
Responds Thoughtfully: Crafts personalized, context-aware responses using LLaMA 3.2 via the Ollama server, tailored to your emotional state.
Runs Anywhere: Packaged in a Docker container for seamless deployment on any system, from your laptop to the cloud.

Think of it as a virtual friend who’s always ready to listen, understand, and respond with just the right vibe. Whether you’re sharing a happy moment or venting about a tough day, Moody Chatbot has your back! 😊

🎨 Features That Make Moody Special

Emotion Detection: Uses a pre-trained TensorFlow model (emotion_classifier.h5) to classify your text into one of six emotions: sad, joy, love, anger, fear, surprise.
Dynamic Responses: Leverages LLaMA 3.2 (via Ollama) to generate empathetic, emotion-specific replies from a curated set of prompts.
Interactive UI: Built with Streamlit for a clean, chat-like interface accessible at http://localhost:8501.
Session Persistence: Remembers your conversation history using Streamlit’s session_state for a seamless chat experience.
Dockerized Deployment: Runs in a lightweight Docker container with all dependencies (Python, TensorFlow, Ollama) pre-configured.
Exit Gracefully: Type “exit,” “quit,” or “bye” to end the chat with a warm farewell message.


🛠️ Project Structure
Here’s how the project is organized in the mOODY_cHATBOT directory:
mOODY_cHATBOT/
├── app.py                  # The heart of the chatbot: Streamlit app logic
├── requirements.txt        # Python dependencies for the app
├── Dockerfile              # Docker configuration for building the container
├── .dockerignore           # Excludes unnecessary files from the Docker image
├── emotion_classifier.h5   # Pre-trained TensorFlow model for emotion prediction
├── emotion_tokenizer.pkl   # Tokenizer for text preprocessing


💻 Getting Started
Ready to chat with Moody? Follow these steps to set up and run the project locally or in a Docker container.
Prerequisites

Python 3.11: For running locally without Docker.
Docker Desktop: For building and running the Docker container (Windows, Mac, or Linux).
Ollama: To serve LLaMA 3.2 responses (included in the Docker setup).
System Resources: At least 16GB RAM recommended for LLaMA 3.2 and TensorFlow.
Internet: Needed to download the LLaMA 3.2 model and dependencies.

Option 1: Run Locally (Without Docker)

Clone the Repository (if hosted on GitHub, or copy the project folder):
git clone https://github.com/your-username/moody-chatbot.git
cd mOODY_cHATBOT


Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

This installs streamlit, tensorflow, joblib, numpy, and requests.

Install and Start Ollama:

Download and install Ollama from ollama.com.
Start the Ollama server:ollama serve


Pull the LLaMA 3.2 model:ollama pull llama3.2:latest




Run the Streamlit App:
streamlit run app.py


Open http://localhost:8501 in your browser.
Type a message (e.g., “I’m so happy!”) and see Moody respond with the predicted emotion and a tailored reply.



Option 2: Run with Docker

Ensure Docker Desktop Is Running:

Open Docker Desktop and confirm it’s set to Linux containers (Settings > General > Use WSL 2 based engine).
Update WSL 2 if needed:wsl --update




Build the Docker Image:
cd "D:\End to end project\Moody_Chatbot\mOODY_cHATBOT"
docker build -t moody-chatbot .

This builds the image with Python, TensorFlow, Ollama, and your app.

Run the Container:
docker run -p 8501:8501 --name moody-chatbot-container moody-chatbot


Access the app at http://localhost:8501.


Interact with Moody:

Type messages in the Streamlit interface.
Exit by typing “exit,” “quit,” or “bye” for a friendly goodbye.



Dockerfile Overview
The Dockerfile packages everything:

Base Image: python:3.11-slim for a lightweight Python environment.
Ollama Setup: Installs Ollama and pulls LLaMA 3.2 at runtime.
Dependencies: Installs Python packages from requirements.txt.
Port: Exposes 8501 for Streamlit.
Command: Runs ollama serve and streamlit run app.py.


🧠 How Moody Works

Emotion Prediction:

Your input text is processed using emotion_tokenizer.pkl to convert it into a format the TensorFlow model (emotion_classifier.h5) understands.
The model predicts one of six emotions: sad, joy, love, anger, fear, surprise.


Response Generation:

Based on the predicted emotion, a random prompt from a curated list (e.g., “User feels sad. Write a response that validates their feelings...”) is selected.
The prompt and your input are sent to the Ollama server (http://localhost:11434) running LLaMA 3.2, which generates a thoughtful response.


Streamlit Interface:

The chat interface displays your message, the predicted emotion, and the chatbot’s response.
Conversation history is stored in st.session_state for continuity.




🛠️ Troubleshooting

Docker Build Fails:

Ollama Server Error: If ollama pull llama3.2:latest fails, pre-pull the model locally (ollama pull llama3.2:latest) and remove the pull step from the Dockerfile.
File Not Found: Ensure emotion_classifier.h5 and emotion_tokenizer.pkl are in the project directory.
Resource Issues: Allocate more CPU/RAM in Docker Desktop (Settings > Resources).
Check logs: docker logs moody-chatbot-container.


Streamlit App Errors:

Model Loading: Verify emotion_classifier.h5 and emotion_tokenizer.pkl are accessible.
Ollama Not Responding: Ensure the Ollama server is running (ollama serve) and http://localhost:11434 is accessible.


WSL 2 Issues (Windows):

Update WSL: wsl --update.
Check WSL status: wsl --list --verbose.
Switch to Hyper-V if WSL fails (Docker Desktop Settings > General).




🌟 Contributing
Want to make Moody even cooler? Contributions are welcome! Here’s how:

Fork the Repo: If hosted on GitHub, fork it and make changes.
Add Features: Improve emotion detection, add new prompts, or enhance the UI.
Submit Pull Requests: Share your improvements with the community.


📜 License
[Insert License Here, e.g., MIT License]

Note: If you’d like a specific license, let me know, and I can update this section!


🙌 Acknowledgments

TensorFlow: For powering emotion detection.
Streamlit: For the slick, easy-to-use web interface.
Ollama: For making LLaMA 3.2 accessible.
You: For building this awesome project and bringing Moody to life!


❓ Need Help?
Got questions or stuck somewhere? Reach out:

Email: [Your email, if you provide one]
GitHub Issues: [Link to repo issues, if hosted]
Ollama Community: For LLaMA-related help.


Moody Chatbot is more than code—it’s a friend who listens with heart. Chat away, and let’s make the world a little more understood, one emotion at a time! 💖