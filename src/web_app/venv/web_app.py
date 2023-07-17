from flask import Flask
from flask import render_template
from ticers import Ticers
import pandas as pd

app = Flask(__name__)
#t = Ticers()

@app.route("/")
def chart():
    return render_template('index.html')

if __name__ == "__main__": 
    app.run('127.0.0.1', port=5001 ,debug=True)
