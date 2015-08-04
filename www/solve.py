import flask, flask.views
from utils import login_required
from lockfile import locked
import os
import time

challenges = {
    '6-07':'SHOULDERSURFING',
    '6-08':'NETCAT',
    '6-09':'SNORT',
    '6-10':'FTEPROXY',
    '6-11':'METASPLOIT',
    '6-12':'SYBILS',
    '6-13':'STEPPINGSTONES',
    '6-14':'ROOTKIT',
    '6-15':'ECBMODE',
    '6-16':'DICTIONARYATTACK',
    '6-17':'WIRESHARK',
    '6-18':'TROJAN',
    '6-19':'CHROMIUM',
    '6-20':'ANONYMOUSE',
    '6-21':'PHISHING',
    '6-22':'LASTPASS',
    '6-23':'SESSIONHIJACKING',
    '6-24':'REFLECTED',
    '6-25':'FIREWALL',
    '6-26':'NESSUS',
    '6-27':'SQLINJECTION',
    '6-28':'PRIVILEGEESCALATION',
    '6-29':'HEARTBLEED',
    '6-30':'PHYSICALACCESS'
}

class Solve(flask.views.MethodView):
    @login_required
    def get(self):
	userdir = "static/" + flask.session['username'] + "/"
	if not os.path.exists(userdir):
	    os.mkdir(userdir)
        sols = [f for f in challenges.keys() if os.path.isfile(userdir+f)]
        nsol = [f for f in challenges.keys() if not (os.path.isfile(userdir+f))]
	return flask.render_template('solve.html', solved=sorted(sols), notsolved=sorted(nsol), challenges=sorted(challenges.keys()))

    @login_required
    @locked("/tmp/mylock",5)
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('login'))
        required = ['challenge', 'guess']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('solve'))
        path = "static/"
	username = flask.session['username']
	challenge = flask.request.form['challenge']
	guess = flask.request.form['guess'].upper().replace(" ","")
        if challenge not in challenges.keys():
            flask.flash("Invalid challenge: " + challenge)
            return flask.redirect(flask.url_for('solve'))
        if os.path.isfile(path+username+"/"+challenge):
            flask.flash("You have already solved " + challenge)
            return flask.redirect(flask.url_for('solve'))
        wait_time = self.block_access(path+username+"/lockout")
        if wait_time > 0:
            flask.flash("You have " + str(wait_time) + " seconds left before you can submit another solution.\n")
            return flask.redirect(flask.url_for('solve'))
        answer=challenges[challenge]
        if answer==guess:
            flask.flash("Correct.  You have solved " + challenge)
	    if not os.path.exists(path+"logs/"):
		os.mkdir(path+"logs/")
            logfilename = path + "logs/" + challenge + ".log"
            logfile = open(logfilename,"ab+")
            rank=len(logfile.readlines())+1
	    logentry = username + " " + guess + " : " + time.asctime() + " : " + flask.request.remote_addr + "\n"
	    logfile.write(logentry)
	    logfile.close()
            userfile = open(path+username+"/"+challenge,'w')
            userfile.write(str(rank)+"\n")
            userfile.close()
        else:
            flask.flash(guess + " is incorrect.  You will now need to wait 2 minutes before trying again.")
            self.penalize(path+username+"/lockout")
        return flask.redirect(flask.url_for('solve'))

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
