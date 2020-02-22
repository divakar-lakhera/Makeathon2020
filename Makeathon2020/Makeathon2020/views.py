"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Makeathon2020 import app
from Makeathon2020.scrapers import gitScraper as gits
from Makeathon2020.scrapers import linkedinScraper as linkin
from Makeathon2020.pdfParser import parsePdf as ppar

# init

newparser = ppar.pdfParser("Makeathon2020/server/test2.pdf","Pankaj Kumar","https://github.com/Pankajcoder1",None,"https://www.linkedin.com/in/pankaj-kumar-795b48198/")
newparser.loadLinks()
newparser.processCV()

"""
gitAcc=gits.gitScraper()
gitAcc.loadProfile("https://github.com/divakar-lakhera")
print(gitAcc.gitGetUserName())
print(gitAcc.gitGetAllLanguages())
print(gitAcc.gitGetAllProjects())
print(gitAcc.gitGetLocation())
# end init
"""
