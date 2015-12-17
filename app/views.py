from flask import send_file
from app import app, Settings

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/favicon.ico')
def favicon():
    return send_file(Settings('path:favicon.ico'), mimetype='image/gif')