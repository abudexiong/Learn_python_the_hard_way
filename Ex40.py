#-*- coding:utf-8 -*-
__author__ = '凯'

cities={'CA':'San F','MI':'Detroit','FL':'Jacksonville'}#create dictionary
cities['NY']='New York'
cities['OR']='Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "not found!"

cities['_find']=find_city

while True:
    print "State?(ENTER to quit",
    state=raw_input(">")
    if not state:break

    city_found=cities['_find'](cities,state)#调用函数
    print city_found


