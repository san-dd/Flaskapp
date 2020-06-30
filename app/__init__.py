from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return 'Index page'
from app import admin
from app import user