# -*- coding: utf-8 -*-
"""
take temperature data in
transfer time-based temperature of each pixel into smooth 
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter as gf

temp = np.array(map(lambda x: 63 - x, np.load('/Users/macbook/GH/cira/data/IR_temperature.npy')))
# record original shape
shape = temp.shape
def transfer(temp):
    temp = temp.reshape((shape[0], shape[1] * shape[2])).T
    return temp

temp1 = transfer(temp)

frame = np.load('/Users/macbook/GH/cira/data/IRTL_frames/IRTL_frame_0280.npy')

def transferback(ft):
    return ft.T.reshape(shape)

res = {}
tem = {}
for sigma in [1,2,3,4,5]:
    tem[sigma] = gf(temp1,sigma)
    # take a subtraction of filtered data by true temperature
    
    # each res[] shapes [696960, 708]
    res[sigma] = temp1 - tem[sigma]
    
    # save result 
    np.save('res_{}'.format(sigma), res[sigma])