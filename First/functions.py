# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:07:09 2015

@author: nviradia
"""

def say_hallo():
    print('Hello')
    
say_hallo()
say_hallo()

def say_hallo(a,b):
    print(a,b)
    
say_hallo(3,4)

a = 9

def say_hallo():
    global a    
    print('a is',a)
    a = 2    
    print('a is',a)
    
say_hallo()
print('a is',a)

def say_hallo(a=1,b=1,c=2):
    print('a:',a,'b:',b,'c:',c)
    
say_hallo()
say_hallo(2,c=8)
say_hallo(2,3)

def total(*nums,**keys):
    total=0
    for num in nums:
        total += num
    for key in keys:
        total += keys[key]
    print(total)

total(1,2,3,4,a=10,b=20)

def retEx():
    return 5
print(retEx())

__version__ = '0.1'
        
    