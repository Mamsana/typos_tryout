from flask import Flask, request, render_template
import requests
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/correct-typo', methods=['GET', 'POST'])
def correct_typo():
    if request.method == 'POST':
        text = request.form['text']

        endpoint = "https://api.openai.com/v1/engines/davinci/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}"
        }

        data = {
            "prompt": text,
            "max_tokens": 100,
            "temperature": 0.5
        }
    
        response = requests.post(endpoint, headers=headers, json=data)

        corrected_text = response.json()['choices'][0]['text']

        return corrected_text

    return render_template("index.html", corrected_text=corrected_text)

if __name__ == "__main__":
   i app.run()
