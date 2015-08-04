#!/usr/bin/env python
import flask, flask.views
import os

users = {
        'cyberdiscoverypdx1': ['znuwha01', 'Team1'],
        'cyberdiscoverypdx2': ['rpibdf02', 'Team2'],
        'cyberdiscoverypdx3': ['ioknjl03', 'Team3'],
        'cyberdiscoverypdx4': ['alnqkc04', 'Team4'],
        'cyberdiscoverypdx5': ['fzwvsq05', 'Team5'],
        'cyberdiscoverypdx6': ['yxehal06', 'Team6'],
        'cyberdiscoverypdx7': ['okavsg07', 'Team7'],
        'cyberdiscoverypdx8': ['bvzghp08', 'Team8'],
        'cyberdiscoverypdx9': ['qrghpt09', 'Team9'],
        'cyberdiscoverypdx10': ['puxstq10', 'Team10'],
        'cyberdiscoverypdx11': ['kcwqgl11', 'Team11'],
        'cyberdiscoverypdx12': ['gciunv12', 'Team12']
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
