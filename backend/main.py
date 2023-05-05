
import os
from flask import Flask, flash, request,render_template, Response, redirect, url_for, session
from flask_cors import CORS, cross_origin
from findRestobyGroceries import findRestobyGroceries

app = Flask(__name__, template_folder="../frontend/build", static_folder="../frontend/build/static")

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/api/FindResto')
def video_feed():
    return findRestobyGroceries("Test")

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

CORS(app, expose_headers='Authorization')