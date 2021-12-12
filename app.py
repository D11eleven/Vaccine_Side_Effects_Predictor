from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/predict")
def about():
    # Return template and data
    return render_template("predict.html")

@app.route("/explorer")
def effects():
    # Return template and data
    #change this to dictionary
    #call function
    return render_template("explorer.html")

@app.route("/team")
def dashboard():
    # Return template and data
    return render_template("team.html")

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    print('postrequest')
    content = request.json["data"]

    # parse
    age_group = int(content["age_group"])
    sex = int(content["sex"])
    other_meds = int(content["other_meds"])
    history = int(content["history"])
    prior_vax = int(content["prior_vax"])
    allergies = int(content["allergies"])
    vax_name = int(content["vax_name"])
    vax_dose = int(content["vax_dose"])

    prediction = ModelHelper.makePredictions(age_group, sex, other_meds, history, prior_vax, allergies, vax_name, vax_dose)
    print(prediction)
    return(jsonify({"ok": True, "prediction": str(prediction)}))

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)