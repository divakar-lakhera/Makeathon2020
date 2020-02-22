"""
The flask application package.
"""

UPLOAD_FOLDER = 'server/'

from flask import Flask
app = Flask(__name__)


import Makeathon2020.views
