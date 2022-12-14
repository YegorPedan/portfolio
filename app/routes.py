from app import app


from flask import render_template


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")