# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:17:53 2020

@author: justm
"""

from itertools import cycle
from time import sleep

for frame in cycle(r'-\|/-\|/'):
    print('\r', frame, sep='', end='', flush=True)
    sleep(0.2)