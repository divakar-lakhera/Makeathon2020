"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect
from Makeathon2020 import app
from Makeathon2020.scrapers import *
from Makeathon2020.scrapers import gitScraper
from Makeathon2020.pdfParser import parsePdf as ppar


newparser = ppar.pdfParser("Makeathon2020/server/test.pdf","Rahul Goswami","https://github.com/goswami-rahul",None,"https://www.linkedin.com/in/rahul101")
newparser.loadLinks()
newparser.processCV()
newparser.getScore()

# init
