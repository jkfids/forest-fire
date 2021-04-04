# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:44:43 2021

@author: Fidel
"""

import numpy as np
from time import time
from forestfire import ForestFire
from matplotlib import pyplot as plt

def plot_firesizepd(forest, t, N):
    """"Constructs a histogram of probability vs. fire size after certain time"""
    start = time()
    L = forest.width
    f = forest.f
    p = forest.p
    
    firesizes = []
    for i in range(N):
        forest = ForestFire([L,L], f, p, spark=True)
        forest.step(t)
        if forest.count(-1) != 0:
            firesizes.append(forest.count(-1))
        #print(i)
    plt.hist(firesizes, density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Fire Size')
    plt.title('Fire Size Probability Distribution')
    end = time()
    print(f'Time elapsed: {round((end - start), 2)} seconds')