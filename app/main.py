import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print("🚀 Servidor Flask iniciado con logging de visitantes")
    app.run(debug=True)
