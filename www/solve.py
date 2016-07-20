import flask, flask.views
from utils import login_required
from lockfile import locked
import os
import time

challenges = {
    '01':'SHOULDERSURFING',
    '02':'NETCAT',
    '03':'SNORT',
    '04':'SENSEPOST',
    '05':'SYBILS',
    '06':'TOR',
    '07':'ROOTKIT',
    '08':'ECBMODE',
    '09':'DICTIONARYATTACK',
    '10':'WIRESHARK',
    '11':'TROJAN',
    '12':'CHROME',
    '13':'PHISHING',
    '14':'LASTPASS',
    '15':'CLICKJACKING',
    '16':'FIRESHEEP',
    '17':'REFLECTED',
    '18':'FIREWALL',
    '19':'NESSUS',
    '20':'METASPLOIT',
    '21':'SQLINJECTION',
    '22':'PRIVILEGEESCALATION',
    '23':'HEARTBLEED',
    '24':'PHYSICALACCESS'
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
