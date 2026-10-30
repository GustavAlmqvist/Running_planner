import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from SQLAlchemy import text

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

db = SQLAlchemy(app)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    with db.engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "application": "ok",
        "databbase": "connected",
    }
