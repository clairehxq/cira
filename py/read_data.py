# -*- coding: utf-8 -*-
"""
Created on Apr 4 23:45:49 2017

@author: ch
"""

import os
from os.path import dirname

import numpy as np

def get_frame(number):
    '''
    read in frame of a time in (0, 708)
    number = int()
    e.g: get_frame(450)
    '''
    cwd = os.getcwd()

    framename = 'frame_{}.png'.format(number)
    cwd_frame = os.path.join(dirname(dirname(cwd)),'data', 'gf_frame_0403_1_5', framename)
    display(Image(filename = cwd_frame))

def get_res(number):
    '''
    read in result from gaussian filtered npy array
    e.g: get_res(5)
    '''
    cwd = os.getcwd()
    resname = 'res_{}.npy'.format(number)
    resfile = os.path.join(dirname(dirname(cwd)), 'data', 'res', resname)
    return np.load(resfile)