from flask import Flask, render_template
import subprocess, sys
import os
import time
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

if __name__ == "__main__":
  app.run(debug=True)
