# -*- coding:utf-8 -*-
__author__ = '凯'
#part6
x="There are %d types of people" %10
binary="binary"
do_not ="don't"
y="Those who know %s those who %s."%(binary,do_not)

print x
print y

print"I said: %r."%x
print "I also said:'%s'."%y

hilarious=False
joke_evaluation="Isn't that joke so funny?!%r"

print joke_evaluation%hilarious

w="This is the left side of ..."
e="a string with a right side."

print w+e,"\n"

#part7

print"Mary had a little lamb."
print"Its fleece was white as %s."%"snow"
print"And everywhere that Mary went."
print"."*10 #what'd that do?

end1="c"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

#watch that comma at the end.try removing it to see what happens.
print end1+end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12,"\n"

#part8

fomatter="%r %r %r %r"

print fomatter %(1,2,3,4)
print fomatter %("one","two","three","four")
print fomatter %(True,False,False,True)
print fomatter %(fomatter,fomatter,fomatter,fomatter)
print fomatter %("I had this thing",
                 "That you could type up right",
                 "but it didn't sing.",
                 "So I said goodnight.\n"
                 )


#part9
#Here's some new strange stuff,remember typeit exactly.

days="Mon Tue Wed Thu Fri Sat Sun"
months="\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nOct\nNov\nDec"

print "Here are the days:",days
print"Here are the months:",months

print """
There's somthing going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,or 5,or 6.
""","\n"

#part10
tabby_cat="\t I'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a\\ cat."

fat_cat='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


