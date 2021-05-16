import flask, flask.views
from utils import login_required
from solve import challenges
from users import Users
import os
import time

class Score(flask.views.MethodView):
    @login_required
    def get(self):
        scores = {}
        myusers = Users()
        for user in myusers.dumpUsers():
            if user is 'wuchang':
                continue
            userdir = "static/obj/" + user + "/";
            if not os.path.exists(userdir):
                os.makedirs(userdir)
            scores[user] = []
            for c in sorted(challenges.keys()):
                if os.path.isfile(userdir+c):
                    place = int(open(userdir+c,"r").readline().rstrip("\n"))
                    if place < 3:
                       levelscore = 13 - place
                    else:
                       levelscore = 10
                    scores[user].append(levelscore)
                else:
                    scores[user].append(0)
#        Re-purpose old Urban Race entry for Graph Homework
            if os.path.exists(userdir+"final.txt"):
                scores[user].append(10)
            else:
                scores[user].append(0)
        return flask.render_template('score.html', scores=scores, challenges=sorted(challenges.keys()))
