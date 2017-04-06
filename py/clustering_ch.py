# -*- coding: utf-8 -*-
"""
Created on Apr 4 23:45:49 2017

@author: ch
"""

import numpy as np
import pandas as pd
from sklearn import cluster
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans, hierarchical
from sklearn.metrics import silhouette_score
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.cluster.hierarchy import dendrogram, linkage


def best_clu_num(model, data):
    '''
    returns a table of cluster number and corresponding silouette score
    '''

    score = []
    clu_num = []
    if model == 'KMeans':
        for i in range(len(data))[1:]:
            try:
                score.append(silhouette_score(data, KMeans(n_clusters=i, random_state=123).fit(data).labels_))
                clu_num.append(i)
            except ValueError:
                continue
                
    elif model == 'GaussianMixture': 
        if len(data) <= 50:
            for i in range(len(data)):
                try:
                    score.append(silhouette_score(data, GaussianMixture(n_components=i).fit(data).predict(train)))
                    clu_num.append(i)
                except ValueError:
                    continue
        else:
            for i in range(50):
                try:
                    score.append(silhouette_score(data, GaussianMixture(n_components=i).fit(data).predict(train)))
                    clu_num.append(i)
                except ValueError:
                    continue

                
    elif model == 'single':
        hi_sin = hierarchy.linkage(data, method='single')
        for i in range(len(data)):
            try:
                score.append(silhouette_score(data, fcluster(hi_sin, i, criterion='maxclust')))
                clu_num.append(i)
            except ValueError:
                continue
                
    elif model == 'complete':
        hi_com = hierarchy.linkage(data, method='complete')
        for i in range(len(data)):
            try:
                score.append(silhouette_score(data, fcluster(hi_com, i, criterion='maxclust')))
                clu_num.append(i)
            except ValueError:
                continue
    temp = pd.DataFrame(score)
    temp.index = clu_num
    return temp


def num_in_clu(model, data):
    '''
    returns a table of cluster number and corresponding silouette score
    '''
    num_clu = best_clu_num.loc[model][0]
    num = []
    if model == 'KMeans':
        label = KMeans(n_clusters=num_clu, random_state=123).fit(data).labels_
        for i in range(num_clu):
            num.append(len(label[label == i]))
                
    elif model == 'GaussianMixture': 
        label = GaussianMixture(n_components=num_clu).fit(data).predict(train)
        for i in range(num_clu):
            num.append(len(label[label == i]))
                
    elif model == 'single':
        hi_sin = hierarchy.linkage(data, method='single')
        label = fcluster(hi_sin, num_clu, criterion='maxclust')
        for i in range(num_clu):
            num.append(len(label[label == i+1]))
                
    elif model == 'complete':
        hi_com = hierarchy.linkage(data, method='complete')
        label = fcluster(hi_com, num_clu, criterion='maxclust')
        for i in range(num_clu):
            num.append(len(label[label == i+1]))
            

    return num, label

