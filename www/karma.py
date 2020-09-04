import flask, flask.views
from utils import login_required
from login import users
from lockfile import locked
import os
import time

class Karma(flask.views.MethodView):
    @login_required
    def get(self):
        username = flask.session['username']
        userdir = "static/" + username + "/"
        if not os.path.exists(userdir):
            os.mkdir(userdir)
        if os.path.isfile(userdir+'karma.txt'):
            curteam = open(userdir+'karma.txt','r').readline().rstrip('\n')
            curteamname = users[curteam][1]
        else:
            curteamname = "Not set"
        allteams = [ [k,v[1]] for k,v in users.iteritems() if (k != username) ]
        return flask.render_template('karma.html', teams=allteams, curteam=curteamname)

    @login_required
    @locked("/tmp/mylock")
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('login'))
        required = ['team']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('karma'))
        path = "static/"
        username = flask.session['username']
        team = flask.request.form['team']
        if team not in users.keys():
            flask.flash("Invalid team " + team)
            return flask.redirect(flask.url_for('karma'))
        karmafile = open(path+username+"/karma.txt","w+")
        karmafile.write(team+"\n")
        karmafile.close()
        return flask.redirect(flask.url_for('karma'))
