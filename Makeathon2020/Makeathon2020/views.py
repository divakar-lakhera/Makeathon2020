"""
Routes and views for the flask application.
"""

from datetime import datetime
from Makeathon2020 import app
from Makeathon2020.scrapers import *
from Makeathon2020.scrapers import gitScraper
from Makeathon2020.pdfParser import parsePdf as ppar
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os

@app.route("/")
def index():
    return render_template("file_uploading.html")

@app.route("/result",methods=["POST"])
def result():
   
    name = request.form.get("name")
    print(name)
    linkedin_url = request.form.get("linkedin")
    github_url = request.form.get("github")
    stackoverflow_url = request.form.get("stackoverflow")
    if stackoverflow_url == "None":
        stackoverflow_url=None
    f = request.files['file']
    f.save(secure_filename(f.filename))
    moduleMain = ppar.pdfParser(f.filename,name,github_url,stackoverflow_url,linkedin_url)
    moduleMain.loadLinks()
    moduleMain.processCV()
    ac=moduleMain.getScore()
    return render_template("file_uploading.html",acc=ac)
