#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, sys, json, os
import key as k
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import challenges as c

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = k.CONSUMER_KEY
CONSUMER_SECRET = k.CONSUMER_SECRET
ACCESS_KEY = k.ACCESS_KEY
ACCESS_SECRET = k.ACCESS_SECRET

#get the solutions to urban challenges and url for final image
s1=c.u1s
s2=c.u2s
s3=c.u3s
s4=c.u4s
s5=c.u5s
s6=c.u6s

class StdOutListener(StreamListener):
    def send_intro_message(self,dmsender):
        time.sleep(3)
        msg="Thanks for the help. To get into the control room, I need the keys in the challenges I had Tris give you. Only Erudite are meant to solve them since it requires knowledge of the campus. The system only allows 10 incorrect guesses so be careful.  What is key one?"
        self.send_msg(dmsender,msg)
        return True

    def send_msg(self,dmsender,msg):
        time.sleep(2)
        msg = "@"+dmsender+" "+msg
        print("Sending " + dmsender + " the message " + msg)
        api.send_direct_message(screen_name=dmsender,text=msg)
        print("Done sending")
        return True

    def get_incorrect_message(self,dmsender,lives):
        newlives = lives - 1
        if (newlives > 9):
            newlives = 9
        f=open(dmsender+"/LIVES",'w+')
        f.write(str(newlives)+"\n")
        f.close()
        if (newlives == 9):
            msg = "Not it.  You have 9 more incorrect guesses left.  Let's not make wrong guesses a habit."
        elif (newlives == 8):
            msg = "Wrong again.  Only 8 more left."
        elif (newlives == 7):
            msg = "That key didn't work either.  I know we're in a rush, but wrong answers aren't going to do us any good.  7 to go..."
        elif (newlives == 6):
            msg = "Incorrect again.  Hey, if you're not really sure, maybe you should ask for help.  Only 6 incorrect guesses left."
        elif (newlives == 5):
            msg = "That key was wrong as well.  You've gone through half of your guesses.  I think you might want to change strategies."
        elif (newlives == 4):
            msg = "That was incorrect.  You have 4 more incorrect guesses left."
        elif (newlives == 3):
            msg = "That was wrong again.  Only 3 more left now.  This is not looking good."
        elif (newlives == 2):
            msg = "That's not it.  Two incorrect guesses left.  You're really making me nervous.  Can you ask for help before guessing again?"
        elif (newlives == 1):
            msg = "Last chance.  There is no more margin for error.  They all have to be correct from now on."
        else:
            msg = "It locked me out.  Looks like I'll have to stop the Erudite the old fashioned way.  Signing off now..."
        return msg

    def on_data(self, data):
        decoded = json.loads(data)
        if 'direct_message' in decoded.keys():
            dm = decoded['direct_message']
            dmsender = dm['sender_screen_name']
            rawtext = dm['text'].upper().replace(" ","")
            dmtext = ''.join(ch for ch in rawtext if ch.isalpha())
            if "CDFour" in dmsender:
                return True
            else:
                print("dmsender: " + dmsender + "   text: " + dmtext)
            if not os.path.exists(dmsender):
                os.mkdir(dmsender)
            if not os.path.exists(dmsender+"/LIVES"):
                f=open(dmsender+"/LIVES",'w+')
                f.write("10\n")
                f.close()
                self.send_intro_message(dmsender)
                return True
            else:
                f=open(dmsender+"/LIVES",'r')
                lives=int(f.readline().rstrip('\n'))
                f.close()
                if (lives == 0):
                    self.send_msg(dmsender,"AutoResponse: Off pursuing Plan B.  Thanks for your help.")
                    return True
            if os.path.exists(dmsender+"/"+s6):
                self.send_msg(dmsender,"AutoResponse: Thanks again.  I'm busy escaping now!")
                return True
            if os.path.exists(dmsender+"/"+s5):
                if s6 in dmtext:
                    open(dmsender+"/"+s6, 'w').close()
                    self.send_msg(dmsender,"You did it! It's unlocked. I'm shutting it down.  Thank you for all of your help!")
                    if not os.path.exists(s6):
                        open(s6, 'w').close()
                        time.sleep(3)
                        self.send_msg(dmsender,"I'm leaving you a little something as a thank you.  I think you can figure out where to get it! " + " http://goo.gl/N5Fd80 ")
                else:
                    msg = self.get_incorrect_message(dmsender,lives) + "  Key six?"
                    self.send_msg(dmsender,msg)
                return True
            if os.path.exists(dmsender+"/"+s4):
                if s5 in dmtext:
                    self.send_msg(dmsender,"Got it.  One more key to go!  So close now.  Send me the sixth key.")
                    open(dmsender+"/"+s5, 'w').close()
                else:
                    msg = self.get_incorrect_message(dmsender,lives) + "  Key five? "
                    self.send_msg(dmsender,msg)
                return True
            if os.path.exists(dmsender+"/"+s3):
                if s4 in dmtext:
                    self.send_msg(dmsender,"Correct.  Two more keys left.  What is key five?")
                    open(dmsender+"/"+s4, 'w').close()
                else:
                    msg = self.get_incorrect_message(dmsender,lives) + "  Key four?"
                    self.send_msg(dmsender,msg)
                return True
            if os.path.exists(dmsender+"/"+s2):
                if s3 in dmtext:
                    self.send_msg(dmsender,"Yes!  That worked.  Halfway there.  What is key four?")
                    open(dmsender+"/"+s3, 'w').close()
                else:
                    msg = self.get_incorrect_message(dmsender,lives) + "  Key three?"
                    self.send_msg(dmsender,msg)
                return True
            if os.path.exists(dmsender+"/"+s1):
                if s2 in dmtext:
                    self.send_msg(dmsender,"Right!  On to the third key.")
                    open(dmsender+"/"+s2, 'w').close()
                else:
                    msg = self.get_incorrect_message(dmsender,lives) + "  Key two?"
                    self.send_msg(dmsender,msg)
                return True
            else:
                if s1 in dmtext:
                    self.send_msg(dmsender,"You got it.  Now give me the second key.")
                    open(dmsender+"/"+s1, 'w').close()
                else:
                    msg = self.get_incorrect_message(dmsender,lives) + "  Key one?"
                    self.send_msg(dmsender,msg)
                return True
            return True
        return True

    def on_error(self,status):
        print("Error: "+str(status))
        return True

while True:
        l = StdOutListener()
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        stream = Stream(auth,l)
        stream.userstream()
