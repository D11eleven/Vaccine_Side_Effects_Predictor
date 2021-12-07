from flask import Flask, render_template, redirect, request
# from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import pickle

# Create an instance of Flask
app = Flask(__name__)

# with open(f'modelfilename.pickle', "rb") as f:
#     model = pickle.load(f)

# feature_names = model.get_booster().feature_names

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html")

@app.route("/side-effects")
def effects():
    # Return template and data
    return render_template("side-effects.html")

@app.route("/dashboard")
def dashboard():
    # Return template and data
    return render_template("dashboard.html")

@app.route("/facts")
def facts():
    # Return template and data
    return render_template("facts.html")

@app.route("/data")
def data():
    # Return template and data
    return render_template("data.html")

@app.route("/sources")
def sources():
    # Return template and data
    return render_template("sources.html")


#main
if __name__ == "__main__":
    app.run(debug=True)