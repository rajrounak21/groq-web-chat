# groq-web-chat
A Groq-powered chatbot built using Flask, providing some  real-time conversational AI experiences with dynamic web integration.

## Features
- Real-time AI responses powered by the Groq API.
- Built with Flask for easy web deployment.
- Simple, user-friendly interface for chatting with the AI.

## Setup Instructions

### Step 1. Clone the repository
```bash
git clone https://github.com/your-username/groq-web-chat.git
cd groq-web-chat


### Step 2: **Install Dependencies**
Ensure you have Python 3.7 or higher installed. Then, create a virtual environment and install the required dependencies:
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

### Step 3: **Get Your Groq API Key**
To access the Groq API, you need an API key. Follow these steps:
Visit the Groq website.
Sign up or log in to your Groq account.
Navigate to the API Keys section in your Groq dashboard.
Generate a new API key and copy it.

### Step 4: **Set Your Groq API Key**
Create a .env file in the root directory of the project.
Add the following content to the .env file:
GROQ_API_KEY=your-api-key-here
Make sure to replace your-api-key-here with the actual key you got from Groq.

### Step 5: **Run the Application**
Once everything is set up, you can run the Flask application by executing the following command:
python app.py
This will start the Flask server on http://localhost:5000.

### Step 6: **Access the Web Interface**
Open your browser and go to http://localhost:5000 to start interacting with the Groq-powered chatbot. Type your questions in the input field and get real-time AI responses.
