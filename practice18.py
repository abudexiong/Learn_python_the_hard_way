# -*-coding:utf-8 -*-
__author__ = '凯'
#this one is like your scripts with argv
def print_two(*args):
    arg1,arg2=args
    print"arg1: %r,arg2: %r"%(arg1,arg2)#参数

#ok that*args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
    print "arg1: %r,arg2: %r"%(arg1,arg2)

#this just takes one arguement
def print_one(arg1):
    print"arg1:%r"%(arg1)

#this one takes no arguements
def print_none():
    print"I got nothing"

print_two_again("Zed","Yasoo")
print_two_again("Zed","Yasso")
print_one("Zed")
print_none()

