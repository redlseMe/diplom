from app import app
from flask import request, url_for, redirect, render_template
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'src/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def upload_form():
    return render_template('hello.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('show'))


@app.route('/show', methods=['GET'])
def show():
    return render_template('file.html')
