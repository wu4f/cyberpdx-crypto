import flask, flask.views
from utils import login_required
from lockfile import locked
import os
import time

class Urban(flask.views.MethodView):
    @login_required
    def get(self):
        status=0
        userdir = "static/obj/" + flask.session['username'] + "/"
        if not os.path.exists(userdir):
            os.makedirs(userdir)
        if os.path.exists(userdir+"final.txt"):
            status=1
        return flask.render_template('urban.html', solved=status)

    @login_required
    @locked("/tmp/mylock",5)
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('login'))
        required = ['guess']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('urban'))
        path = "static/obj/"
        username = flask.session['username']
        guess = flask.request.form['guess']
        if os.path.isfile(path+username+"/final.txt"):
            flask.flash("You have already solved the final challenge")
            return flask.redirect(flask.url_for('urban'))
        wait_time = self.block_access(path+username+"/lockout")
        if wait_time > 0:
            flask.flash("You have " + str(wait_time) + " seconds left before you can submit another solution.\n")
            return flask.redirect(flask.url_for('urban'))
        numright = self.check_answer(guess)
        if (numright == 6):
            flask.flash("Correct.  Congratulations.  You have completed the race")
            if not os.path.exists(path+"logs/"):
                os.makedirs(path+"logs/")
            logfilename = path + "logs/final.log"
            logfile = open(logfilename,"ab+")
            rank=len(logfile.readlines())+1
            logentry = username + " " + guess + " : " + time.asctime() + " : " + flask.request.remote_addr + "\n"
            logfile.write(logentry)
            logfile.close()
            userfile = open(path+username+"/final.txt",'w')
            userfile.write(str(rank)+"\n")
            userfile.close()
        else:
            flask.flash("Incorrect guess. You will now need to wait 2 minutes before trying again.")
            self.penalize(path+username+"/lockout")
        return flask.redirect(flask.url_for('urban'))

    def check_answer(self,guess):
        newguess = ''.join(ch for ch in guess if ch.isalpha()).upper()
        parts = 0
        if 'TECOTOSH' in newguess:
            parts += 1
        if 'AUTZEN' in newguess:
            parts += 1
        if 'DANNY' in newguess:
            parts += 1
        if 'FREEDOM' in newguess:
            parts += 1
        if 'GREEN' in newguess:
            parts += 1
        if 'BLACKSTONE' in newguess:
            parts += 1
        flask.flash("You have " + str(parts) + " out of 6 parts correct.")
        return parts

    def block_access(self,userfile):
        if not os.path.exists(userfile):
            return 0
        else:
            f=open(userfile,"r")
            lockout_time=int(f.readline().rstrip("\n"))
            f.close()
            current_time=int(time.time())
            wait_time=current_time-lockout_time
            if wait_time > 120:
                return 0
            else:
                return 120-wait_time

    def penalize(self,userfile):
        f=open(userfile,"w+")
        f.write(str(int((time.time())))+"\n")
        f.close()
