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

#get the solutions to mini urban challenges 1 and 2
s1=c.mu1s
s2=c.mu2s

class StdOutListener(StreamListener):
    def send_intro_message(self,dmsender):
        time.sleep(3)
        msg="I'm glad my message it to you.  The thief who stole the candy didn't realize it was bad karma. It turns out someone on the inside made him steal it to keep the sugar away from you. He has a plan to get it back, but first, to prove you are not the insider, what is key one?"
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
            msg = "Not it.  You have 9 more incorrect guesses left."
        elif (newlives == 8):
            msg = "Wrong again.  Only 8 more left."
        elif (newlives == 7):
            msg = "That wasn't it.  7 to go..."
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
            msg = "You must not be who I was looking for.  Stop messaging me!  Signing off now..."
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
                    self.send_msg(dmsender,"AutoResponse: Blocked.")
                    return True
            if os.path.exists(dmsender+"/"+s2):
                self.send_msg(dmsender,"Good luck!")
                return True
            if os.path.exists(dmsender+"/"+s1):
                if s2 in dmtext:
                    open(dmsender+"/"+s2, 'w').close()
                    self.send_msg(dmsender,"Ok. You're legit.  The thief did not catch the insider's name, but the guy was wearing a cap with a block M on it when they met on Monday.")
                    time.sleep(2)
                    if not os.path.exists(s2):
                        open(s2, 'w').close()
                        time.sleep(2)
                        self.send_msg(dmsender,dmsender+", Find Lois and ask for the microphone.  Tell her Four sent you.  Then, figure out who the insider is.  I will send more students to you to help.  When you have a group of at least 6 students and are sure of the insider's identity, go up as a group and ask for your candy back.")
                    else:
                        self.send_msg(dmsender,"Find the student who has the microphone and figure out who the insider is.  Then, as a group, ask the insider for your candy back!")
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
