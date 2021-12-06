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



#main
if __name__ == "__main__":
    app.run(debug=True)