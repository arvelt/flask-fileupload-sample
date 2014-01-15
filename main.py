# -*- coding: utf-8 -*-
import os
from flask import Flask, request, redirect, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = './files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        app.logger.info("Uploaded filename is "+file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')

    if request.method == 'GET':
        dirlist = os.listdir( app.config['UPLOAD_FOLDER'] )
        for one_file in dirlist:
            print one_file

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
