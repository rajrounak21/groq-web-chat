# groq-web-chat
A Groq-powered chatbot built using Flask, providing some  real-time conversational AI experiences with dynamic web integration.

## Features
- Real-time AI responses powered by the Groq API.
- Built with Flask for easy web deployment.
- Simple, user-friendly interface for chatting with the AI.

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/groq-web-chat.git
cd groq-web-chat

2. Install dependencies
Ensure you have Python 3.7 or higher installed. Then, create a virtual environment and install the required dependencies:

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt




3. Get a Groq API Key
To access the Groq API, you will need an API key. Follow these steps:

Visit the Groq website.

Sign up or log in to your Groq account.
Navigate to the API Keys section in your Groq dashboard.
Generate a new API key and copy it.

4. Set your Groq API Key
Create a .env file in the root directory of the project and add your API key like so:

GROQ_API_KEY=your-api-key-here
Make sure to replace your-api-key-here with the actual key you got from Groq.

5. Run the Flask app
Now that everything is set up, you can start the Flask web app by running:

python app.py

