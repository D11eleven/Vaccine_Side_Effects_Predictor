from flask import Flask, render_template, jsonify, send_from_directory, redirect, url_for, request
import json
import pandas as pd
import numpy as np
import os
# from modelHelper import modelHelper

#init app and class
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# modelHelper = ModelHelper()

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