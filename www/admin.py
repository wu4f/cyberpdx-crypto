import flask, flask.views
from utils import admin_required
from users import Users
from werkzeug.utils import secure_filename
import os

class Admin(flask.views.MethodView):
    @admin_required
    def get(self):
        return flask.render_template('admin.html')

    @admin_required
    def post(self):
        from app import app
        myusers = Users()
        if 'Upload' in flask.request.form['action']:
            f = flask.request.files['file']
            filename = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))
            if filename.endswith('.csv'):
                f.save(filename)
                myusers.importUsers(filename)
                flask.flash("Finished import.","ok")
            else:
                flask.flash("Error: CSV file is required.","err")
        elif 'Reset' in flask.request.form['action']:
            myusers.resetCTF()
            flask.flash("CTF reset. Admin account set to default.","ok")
        elif 'Change' in flask.request.form['action']:
            myusers = Users()
            username = flask.request.form['username']
            password = flask.request.form['password']
            myusers.changeUser(username, password)
            flask.flash(f"{username} password is now {password}","ok")
        return flask.render_template('admin.html')
