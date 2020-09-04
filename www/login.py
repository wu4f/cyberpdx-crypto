#!/usr/bin/env python
import flask, flask.views
import os

users = {
        'wuchang': ['9999', 'Wu'],
        'cdpdx1': ['znuwha01', 'Capital'],
        'cdpdx2': ['rpibdf02', 'Cleveland'],
        'cdpdx3': ['ioknjl03', 'Lincoln'],
        'cdpdx4': ['alnqkc04', 'Madison'],
        'cdpdx5': ['fzwvsq05', 'Skyview'],
        'cdpdx6': ['yxehal06', 'St.Marys'],
        'cdpdx7': ['okavsg07', 'SST'],
        'cdpdx8': ['bvzghp08', 'Tigard'],
        'cdpdx9': ['qrghpt09', 'Tualatin'],
        'cdpdx10': ['puxstq10', 'Village']
}

class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('login.html')

    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('main'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('main'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if username in users and users[username][0] == passwd:
            flask.session['username'] = username
            userdir = "static/" + flask.session['username']
            if not os.path.exists(userdir):
                os.mkdir(userdir)
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('main'))
