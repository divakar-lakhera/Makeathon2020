"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Makeathon2020 import app
from Makeathon2020.scrapers import gitScraper as gits
# init
gitAcc=gits.gitScraper()
gitAcc.loadProfile("https://github.com/divakar-lakhera/")
print(gitAcc.gitGetUserName())
print(gitAcc.gitGetAllLanguages())
print(gitAcc.gitGetAllProjects())
print(gitAcc.gitGetLocation())
# end init

