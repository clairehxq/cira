# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:45:49 2017

@author: ch
"""
import os
import matplotlib.pyplot as plt

# get current working directory
cwd = os.getcwd()

shape = (708, 720, 968)
def transferback(ft):
    '''transfer reshaped file of (696960, 708) to
    (708, 720, 968)
    '''
    return ft.T.reshape(shape)
    
# load in filtered data
res = {}
maxt = []
mint = []
for i in range(1,6):
    res[i] = np.load(cwd + 'data/res_{}.npy'.format(i))
    maxtt = res[i].max(axis = 1).max()
    mintt = res[i].min(axis = 1).min()
    maxt.append(maxtt)
    mint.append(mintt)
    
# find lowest value and highest value over time
maxtemp = maxt.max()
mintemp = mint.min()

def doplot(res):
    ''' 
    create png file and save in 'gf_frame' folder
    '''
    res_ = transferback(res)
    for j in range(0,len(res)):
        res_ = transferback(res[j])
        for i in range(0, res_.shape[0]):
            plt.imsave('/gf_frame_{}/frame_{}.png'.format(j,i),res_[i,:,:], cmap = 'gist_heat', vmin = mintemp, vmax = maxtemp)


doplot(res)    
