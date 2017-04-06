# -*- coding: utf-8 -*-
"""
Created on Apr 4 23:45:49 2017

@author: ch
"""

def pointer(node):
    '''
    points to its original pixel location
    temperature file is of shape: [708, 720, 968]
    with reshpe, we transfered that to [708, 720*968]
    while 720 refers to the length of y axis of the frame and 968 refers to that of x axis
    note that pixel location starts from 0
    '''
    return node[1]*720 + node[0]

def transferback(ft):
    '''transfer reshaped file of, e.g.: res 
    (696960, 708) to
    (708, 720, 968)
    '''
    shape = (708, 720, 968)
    return ft.T.reshape(shape)