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

@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html")

@app.route("/side-effects")
def effects():
    # Return template and data
    #change this to dictionary
    #call function
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

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    print('postrequest')
    content = request.json["data"]

    # parse
    age_group = int(content["age_group"])
    sex = int(content["sex"])
    other_meds = int(content["other_meds"])
    cur_ill = int(content["cur_ill"])
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