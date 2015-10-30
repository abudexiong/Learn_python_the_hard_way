# -*- coding:utf-8 -*-
__author__ = '凯'
print"You enter a dark room with two doors.Do you go through #1 or door #2"

door=raw_input(">")

if door=="1":
    print"""
    There's a giant bear here eating a cheese cake.What do you do?
    1.Take the cake.
    2.Scream at the bear.
    """
    bear=raw_input(">")

    if bear=="1":
        print"The bear eats your face off.Good jobs!"
    elif bear=="2":
        print "The bear eats your legs off.Good jobs!"
    else:
        print"Well,doing %s is probably better.Bear runs away."%bear#作者是个变态→_→

elif door=="2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print"1.Bluberries."
    print"2.Yellow jacket clothespins."
    print"3.Understanding revolvers yelling melodies"

    insanity=raw_input(">")
    if insanity=="1"or insanity=="2":
        print "your body survive powered by a mind of jello.Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.Good job!"
else:
    print"You stumble around and fall on a knife and die,Good job!"
