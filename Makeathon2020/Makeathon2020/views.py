"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Makeathon2020 import app
from Makeathon2020.scrapers import gitScraper as gits
from Makeathon2020.pdfParser import parsePdf as ppar
from Makeathon2020.scrapers import linkedinScraper as links
# init

newparser = ppar.pdfParser("Makeathon2020/server/test.pdf","Rahul Goswami","https://github.com/goswami-rahul",None,"https://www.linkedin.com/in/rahul101")
newparser.loadLinks()
newparser.processCV()
newparser.dumpStringPool()
newparser.checkPool()
"""
mod = links.linkedinScraper()
mod.loadProfile("https://www.linkedin.com/in/pankaj-kumar-795b48198/")
print(mod.getUserName())
mod.killDriver()
newparser.dumpContent()
"""

# Pause Switch
i=input()
#
"""


gitAcc=gits.gitScraper()
gitAcc.loadProfile("https://github.com/divakar-lakhera")
print(gitAcc.gitGetUserName())
print(gitAcc.gitGetAllLanguages())
print(gitAcc.gitGetAllProjects())
print(gitAcc.gitGetLocation())
# end init
"""
