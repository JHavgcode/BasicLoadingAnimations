# -*- coding: utf-8 -*-
"""
@author: justm
"""

#imports necessary libraries and functions
from time import sleep
import math

#function to determine number of equal signs in progress bar 
def numequals(current_prog):
    #calculates number of characters
    numeq = math.floor(current_prog/10)
    #actually creates the correct string
    eq = ('=' * numeq) + '>'
    if(numeq == 10):
        eq = '=' * 11
    return eq

#function to determine number of spaces in progress bar
def numspace(current_prog):
    #calculates number of spaces
    numsp = 10- math.floor(current_prog/10)
    #actually creates the string with correct spaces
    eq = ' ' * numsp
    return eq

#function that prints updated progress bar info
#Takes in current progress, assumes 1-100 value
def updateprogress(current_prog):
    """\r makes the cursor return to the beginning
        Then you have to put in everything you want to 
        be printed over in the same print statement
        set sep and end to '' so that it won't automatically
        print a newline everytime. Then set flush to True so
        it creates the line as buffered.  
    """
    
    print('\r','[', numequals(current_prog), numspace(current_prog), '] ', current_prog, '%',  sep = '', end = '', flush = True)
    return

#creates a flag for when to stop the loop
check = True
#arbitrary progress value for bar
progress = 0
#Progress bar loop
while(check):
    #function call to update progress
    updateprogress(progress)
    #time pause for meaningful view of progress
    #glitches out for values less than 0.1
    sleep(.1)
    #updates progress
    progress = progress + 1
    #condition to set flag to false and stop loop
    if(progress >= 101):
        check = False