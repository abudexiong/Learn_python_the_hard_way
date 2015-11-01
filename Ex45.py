# -*-coding:utf-8 -*-
__author__ = '凯'
##Animal is-a object(yes,sort of confusing)look at the extra credit
class Animal(object):
    pass

##??
class Dog(Animal):
    def __init__(self,name):
        ##??
        self.name=name

##??
class Cat(Animal):
    def __init__(self,name):
        ##??
        self.name=name

##??
class Person(object):
    def __init__(self,name):
        ##??
        self.name=name
        ##person has-a pet of some kind (I like dogs
        self.pet=None

class Employee(Person):
    def __init__(self,name,salary):
        ##??hmm what is this strange magic?
        super(Employee,self).__init__(name)
        ##??
        self.salary=salary

##??
class Fish(object):
    pass

class Salmon(Fish):
    pass
class Halibut(Fish):
    pass

rover=Dog("Rover")

satan=Cat("Satan")

mary=Person("mary")

mary.pet=satan

franl=Employee("franl",5000)

print franl.salary

flipper=Fish()

crouse=Salmon()

harry=Halibut()



