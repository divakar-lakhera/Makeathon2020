"""
Routes and views for the flask application.
"""
import os
import subprocess
import shutil
from datetime import datetime
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
from Makeathon2020 import app
from Makeathon2020.scrapers import *
from Makeathon2020.pdfParser import parsePdf as ppar

# init
"""
newparser = ppar.pdfParser("Makeathon2020/server/test2.pdf","Pankaj Kumar","https://github.com/Pankajcoder1",None,"https://www.linkedin.com/in/pankaj-kumar-795b48198/")
newparser.loadLinks()
newparser.processCV()
"""
"""
gitAcc=gits.gitScraper()
gitAcc.loadProfile("https://github.com/divakar-lakhera")
print(gitAcc.gitGetUserName())
print(gitAcc.gitGetAllLanguages())
print(gitAcc.gitGetAllProjects())
print(gitAcc.gitGetLocation())
# end init
"""


@app.route("/")
def index():
    return render_template("file_uploading.html")

@app.route("/result",methods=["POST"])
def result():
    name = request.form.get("name")
    
    linkedin_url = request.form.get("linkedin_url")

    github_url = request.form.get("github_url")

    stackoverflow_url = request.form.get("stackoverflow_url")

    if request.method == 'POST':
        if 'resume' not in request.files:
            return redirect(request.url)
        resume = request.files['resume']
        if resume:
            filename = secure_filename(resume.filename)
            resume.filename = "test.pdf"
            resume.save(resume.filename)
            
            subprocess.call("mv %s %s" % (os.getcwd() + "/test.pdf", os.getcwd() + "/Makeathon2020/server/"), shell=True)
            return redirect('/')
    else:
        return redirect(request.url)

