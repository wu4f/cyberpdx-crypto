#!/usr/bin/env python
import flask, flask.views
import os
from users import Users

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
        myusers = Users()
        if myusers.checkUser(username, passwd):
            flask.session['username'] = username
            userdir = "static/obj/" + flask.session['username']
            if not os.path.exists(userdir):
                os.makedirs(userdir)
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('main'))
