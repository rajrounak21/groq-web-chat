import os
from flask import Flask, request, render_template
from groq import Groq

# Get API key from environment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Initialize Groq client
client = Groq()

# Create Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = None
    if request.method == 'POST':
        question = request.form['question'].strip()
        if question:
            response = client.chat.completions.create(
                model="compound-beta",
                messages=[{"role": "user", "content": question}]
            )
            response_text = response.choices[0].message.content
    return render_template("index.html", response=response_text)

if __name__ == '__main__':
    app.run(debug=True)
