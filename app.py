from flask import Flask, request, render_template
import requests
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Correct typos in the following text;\n {text}\n",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        corrected_text = response.text
        return corrected_text
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
