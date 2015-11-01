# -*- coding:utf-8 -*-
__author__ = '凯'
from sys import exit
from random import randint

class Game(object):
    def __init__(self,start):
        self.quips=["you died.You kinda suck at this.",
                    "Your mom would be proud.If she were smarter",
                    "Such a luser",
                    "I have a  small puppy tha't better at this."]
        self.start=start

    def play(self):
        next=self.start

        while True:
            print "\n----------"
            room=getattr(self,next)
            next=room()

    def death(self):
        print self.quips[randint(0,len(self.quips)-1)]
        exit(1)

    def central_corridor(self):
        print"central_corridor"

        action=raw_input(">")

        if action=="shoot!":
            print "shoot!"
        elif action=="dodge!":
            print "dodge!"
        elif action=="tell a joke":
            print "tell a joke"
        else:
            print "Does not compute"
            return 'central_corridor'

    def laser_weapon_armony(self):
        print "laser weapon armony"
        code="&d&d&d"%(randint(1,9),randint(1,9),randint(1,9))
        guess=raw_input("[keypad]>")
        guesses=0

        while guess!=code and guesses<10:
            print "BZZZZEDDD"
            guesses+=1
            guess=raw_input("[keypad]>")

        if guess==code:
            print "equal"
            return 'the_bridge'
        else:
            print "not equal"
            return 'death'

    def the_bridge(self):
        print "the bridge"

        action=raw_input(">")

        if action=="throw the bomb":
            return'death'
        elif action=="slowly place the bomb":
            return 'escape_pod'
        else:
            print "Does not compute!"
        return 'the_bridge'

    def escape_pod(self):

        print "escape pod"
        good_pod=randint(1,5)
        guess = raw_input("[pod#]>")

        if int(guess)!=good_pod:
            return 'death'
        else:
            print "time.you won"
            exit(0)



a_game=Game("central_corridor")
a_game.play()

