from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)