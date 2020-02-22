"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect
from Makeathon2020 import app
from Makeathon2020.scrapers import *
from Makeathon2020.scrapers import gitScraper as gitLab
from Makeathon2020.pdfParser import parsePdf as ppar


gitAcc=gitLab.gitScraper()
gitAcc.loadProfile("https://github.com/divakar-lakhera")
print(gitAcc.gitGetUserName())
print(gitAcc.gitGetAllLanguages())
print(gitAcc.gitGetAllProjects())
print(gitAcc.gitGetLocation())


# init
"""
newparser = ppar.pdfParser("Makeathon2020/server/test.pdf","Rahul Goswami","https://github.com/goswami-rahul",None,"https://www.linkedin.com/in/rahul101")
newparser.loadLinks()
newparser.processCV()
newparser.getScore()
"""

# end init

i=input()
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

    resume = request.files['resume']
    resume.filename = "test2.pdf"
    resume.save("Makeathon2020\server\test.pdf"+resume.filename)

    return render_template("file_uploading.html")
"""