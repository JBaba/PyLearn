# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:34:52 2015

@author: nviradia
"""

class person:
    def __init__(self,age,name):
        print("Person name is",name,"and age",age)
        self.name=name
        self.age=age        
        
    def tell(self):
        print("Name:",self.name,"age:",self.age,end=" ")
        
class student(person):
    def __init__(self,age,name,marks):
        person.__init__(self,age,name)
        self.marks=marks
        
    def tell(self):
        person.tell(self)
        print("marks:",self.marks)
        
class teacher(person):
    def __init__(self,age,name,sal):
        person.__init__(self,age,name)
        self.sal=sal
        
    def tell(self):
        person.tell(self)        
        print("salary:",self.sal)      
        
t = teacher(35,'Ajay',20000)
s = student(19,"Ram",90)

items = [t,s]

for item in items:
    item.tell()

t.tell()
s.tell()