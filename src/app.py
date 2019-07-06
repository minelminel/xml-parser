import os
from glob import glob
from time import sleep
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    flash,
    url_for,
    send_from_directory,
    abort,
)
from util import xml_to_list, list_to_csv, make_name


app = Flask(__name__)
app.config['BASE_DIR'] = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.config['BASE_DIR'], 'uploads')
app.config['ALLOWED_EXTENSIONS'] = set(['xml'])
app.config['MAX_CONTENT_SIZE'] = 16 * 1024 * 1024 # 16 megabytes


def verify_upload(filename):
    if '.' not in filename:
        return False
    if filename.split('.')[-1] not in app.config['ALLOWED_EXTENSIONS']:
        return False
    return True


def verify_filesize(cookies):
    fsize = int(cookies.get('filesize', app.config['MAX_CONTENT_SIZE']+1))
    if fsize <= app.config['MAX_CONTENT_SIZE']:
        return True
    else:
        return False


def process_document(as_xml, as_csv):
    """ No error handling has to be done here
    since the function is wrapped in a try/except """
    # read xml file from directory
    # xml_to_list()
    # list_to_csv()
    # save generated csv
    # raise NotImplementedError()
    pass


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.files['doc'])
        if not request.files['doc']:
            flash('Please select a file', 'info')
            return redirect(url_for('index'))
        else:
            doc = request.files['doc']
            if not verify_upload(doc.filename) or not verify_filesize(request.cookies):
                flash('File must have a .xml extension and be less than 16 megabytes', 'danger')
                return redirect(url_for('index'))
            file_name, file_path = make_name(app.config['UPLOAD_FOLDER'])
            doc.save(file_path + '.xml')
            print(f'[+] {file_path+".xml"} has been uploaded.') # # DEBUG
            try:
                process_document(file_path + '.xml', file_path + '.csv')
                return send_from_directory(app.config['UPLOAD_FOLDER'], filename=file_name + '.xml', as_attachment=True)
            except:
                flash('Unable to process file, check syntax and try again.', 'info')
                return redirect(url_for('index'))
            finally:
                for fl in glob(file_path + '.*'):
                    # os.remove(fl)
                    pass
    return render_template('index.html')


@app.route('/beta', methods=['GET'])
def beta():
    return render_template('beta.html')


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key = '1234567890'
    app.run(host='0.0.0.0', port=5000, debug=True)
