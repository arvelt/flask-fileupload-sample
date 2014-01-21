# -*- coding: utf-8 -*-
import os
from flask import Flask, request, redirect, render_template, url_for, send_from_directory

UPLOAD_FOLDER = '/files'
PHISICAL_ROOT = os.path.dirname( os.path.abspath( __file__ ) )
ALLOWED_EXTENSIONS = set(['PNG', 'png', 'JPG', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PHISICAL_ROOT + UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        app.logger.info("Uploaded filename is "+file.filename)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('upload_file'))

    if request.method == 'GET':
        file_list = os.listdir( app.config['UPLOAD_FOLDER'] )
        files = []
        for one_file in file_list:
            if one_file == '.gitkeep':
                continue
            dic_file = {}
            link = 'fileupload/files/' + one_file
            dic_file['url'] = link
            dic_file['file_name'] = one_file
            print dic_file
            files.append( dic_file )

    return render_template('index.html',files=files)

@app.route('/files/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
