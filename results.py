# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:36:16 2021

@author: Fidel
"""

# Import standard libraries
import numpy as np
from time import time

# Import local modules
from forestfire import ForestFire
from main import *

# Create output directory if it does not exist
from pathlib import Path
Path('animations').mkdir(parents=True, exist_ok=True)
Path('plots').mkdir(parents=True, exist_ok=True)

#%%
L = 720
forest = ForestFire([L,L], 0.0001, 0.01)
animate_forest(forest, interval=100, frames=200, name='forestfire720.gif')

L = 480
forest = ForestFire([L,L], 0.0001, 0.01)
animate_forest(forest, interval=100, frames=200, name='forestfire480.gif')

L = 360
forest = ForestFire([L,L], 0.0001, 0.01)
animate_forest(forest, interval=100, frames=200, name='forestfire360.gif')

#%%
L = 200
high_grow_no_lightning = ForestFire([L,L], 0.2, 0.2)
plot_firesizepd(high_grow_no_lightning, 250, 1000)
    
#%%
L = 200
forest_100=ForestFire([L,L], 0.00001, 0.01, spark=True)
plot_rgvt(forest_100, 5000)