from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        result = {
            "original": text,
            "uppercase": text.upper(),
            "word_count": len(text.split()),
            "char_count": len(text)
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)