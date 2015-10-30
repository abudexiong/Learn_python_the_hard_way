# -*-coding:utf-8 -*-
__author__ = '凯'
def add(a,b):
    print "adding %d + %d"%(a,b)
    return a+b

def substract(a,b):
    print "SUBSTRACTING %d - %d"%(a,b)
    return a-b

def multiply(a,b):
     print "MULTIPLYING %d * %d"%(a,b)
     return a*b

def divide(a,b):
     print "DIVIDING %d / %d"%(a,b)
     return a/b

print "Let's do some math with just functions"

age=add(30,5)
height=substract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d"%(age,height,weight,iq)#这他妈参数都是什么鬼 IQ50是弱智嘛？

#A puzzle for the extra credit,type it anyway

print "Here is a puzzle"
what=add(age,substract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand"


