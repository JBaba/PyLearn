# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:45:07 2015

@author: nviradia
"""

class MynameException(Exception):
    def __init__(self,name):
        Exception.__init__(self)        
        self.name = name
        
        
try:
    inName = input('Enter name:')
    
    if(inName != 'Naimish'):
        raise MynameException('Naimish')
        
except MynameException as ex:
    print(ex.__class__,'Name has to be',ex.name)
else:
    print('No exp raised')