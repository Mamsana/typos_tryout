from flask import Flask, request, render_template
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
            prompt=f"Correct typos in the following text\n\n{text}",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        corrected_text = response["choices"][0]["text"]
        return render_template("index.html", corrected_text=corrected_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
