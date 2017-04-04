# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:45:49 2017

@author: ch
"""
import os
import matplotlib.pyplot as plt
import numpy as np

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
threshold = {}

# getting clim values
for i in range(1,6):
    res[i] = np.load(os.path.join(cwd, 'res_{}.npy'.format(i)))
    # choose a frame in the middle of time 354

    temp_frame = res[i][: , 354]
    std = temp_frame.std()
    mean = temp_frame.mean()
    # creating a threshold for 3 std
    threshold[i] = (mean - 3 * std, mean + 3 * std)
    print threshold[i]

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def doplot(res):
    ''' 
    create png file and save in 'gf_frame' folder
    '''

    for j in range(1,len(res)+1):
        res_ = transferback(res[j])
        os.makedirs(cwd+'/gf_frame_0403_1_{}'.format(j))
        os.chdir(cwd+'/gf_frame_0403_1_{}'.format(j))
        for i in range(0, res_.shape[0]):
            plt.imsave('frame_{}.png'.format(i), res_[i,:,:], cmap = 'gist_heat', vmin = threshold[j][0], vmax = threshold[j][1])
        
        os.chdir(cwd)

doplot(res)    


