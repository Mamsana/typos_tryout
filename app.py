from flask import Flask, request, render_template
import requests
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/complete_text", methods=["POST"])
def complete_text():
    prompt=f"Correct typos in the following text;\n {text}\n",
    text = request.form['prompt']
    model_engine = "text-davinci-003"
    completion_params = {
        "model": model_engine,
        "prompt": prompt,
        "temperature": 0,
        "max_tokens": 60,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = openai.Completion.create(
        model=completion_params["model"],
        prompt=completion_params["prompt"],
        temperature=completion_params["temperature"],
        max_tokens=completion_params["max_tokens"],
        top_p=completion_params["top_p"],
        frequency_penalty=completion_params["frequency_penalty"],
        presence_penalty=completion_params["presence_penalty"],
    )
    return render_template('complete_text.html', completed_text=response["choices"][0]["text"])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
