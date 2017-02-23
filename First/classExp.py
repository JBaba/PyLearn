# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:56:09 2015

@author: nviradia
"""

class Robot:
    """ This is robot class """
    
    population = 0
    
    def __init__(self,name):
        """ Init the robot class """
        self.name = name
        print("class",self.name,"is initialized")
        Robot.population += 1
    
    def fakePop(self):
        self.population +=1        
        
    def die(self):
        """ destory robot """
        print(self.name,"robot is destroyed")
        Robot.population -= 1
        
    def greetings(self):
        print(self.name,"robot says hi")
        
    def selfCountRobots(self):
        print("we have",self.population,"self count robots.")
        
    @classmethod
    def countRobots(cls):
        print("we have",cls.population,"robots.")
        
    @classmethod
    def count2Robots(self):
        print("we have count2",self.population,"robots.")
        print("we have count2",Robot.population,"robots.")
        
        
droid1 = Robot("R2 d1")
droid1.greetings()
droid1.fakePop()
droid1.selfCountRobots()
droid1.countRobots()

droid2 = Robot("R2 d2")
droid2.greetings()
droid2.fakePop()
droid2.selfCountRobots()
droid2.countRobots()

print("do some work.")

droid1.die()
droid1.countRobots()
droid1.count2Robots()
droid2.die()
droid1.countRobots()
droid1.count2Robots()
droid2.countRobots()
Robot.countRobots()