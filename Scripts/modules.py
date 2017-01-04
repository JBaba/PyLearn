# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:33:00 2015

@author: nviradia
"""

from math import sqrt
print(sqrt(16))
print(.1 + .2)

import functions
functions.say_hallo()

from functions import say_hallo, __version__
say_hallo()
print(__version__)

from os import time
print(time)