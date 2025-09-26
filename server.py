"""Simple Flask app to search record inventory."""

from __future__ import annotations

import os
from flask import Flask, request, render_template

import records_db

app = Flask(__name__)
DB_PATH = os.environ.get("DB_PATH", "records.db")


@app.route("/", methods=["GET"])
def index():
    query = request.args.get("q", "")
    results = records_db.search_records(query, DB_PATH) if query else []
    return render_template("index.html", query=query, results=results)


if __name__ == "__main__":
    app.run(debug=True)
