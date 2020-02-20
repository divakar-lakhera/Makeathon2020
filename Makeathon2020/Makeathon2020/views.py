"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Makeathon2020 import app
from Makeathon2020.scrapers import gitScraper as gits
# init
gitAcc=gits.gitScraper()
gitAcc.loadProfile("https://github.com/lalinsky")
print(gitAcc.gitGetUserName())
print(gitAcc.gitGetAllLanguages())
print(gitAcc.gitGetAllProjects())
# end init

