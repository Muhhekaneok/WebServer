from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("form.html", name=name)


if __name__ == "__main__":
    app.run()
