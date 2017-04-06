# -*- coding: utf-8 -*-
"""
Created on Apr 4 23:45:49 2017

@author: ch
"""

import os
from os import dirname
import numpy as np

def get_frame(number):
    cwd = os.getcwd()

    framename = 'frame_{}.png'.format(number)
    cwd_frame = os.path.join(dirname(cwd), 'gf_frame_0403_1_5', framename)
    display(Image(filename = cwd_frame))

def get_res(number):
    
    cwd = os.getcwd()
    resname = 'res_{}.npy'.format(number)
    resfile = os.path.join(dirname(cwd), 'data', 'res', resname)
    return np.load(resfile)