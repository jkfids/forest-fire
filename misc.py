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
from analysis import *

# Create output directory if it does not exist
from pathlib import Path
Path('animations').mkdir(parents=True, exist_ok=True)
Path('plots').mkdir(parents=True, exist_ok=True)

#%%
L = 200
forest200_pd = ForestFire([L,L], 0, 0.5, spark=True)
p0 = [1/L, L**2/5, 100] # Initial guess for gaussian parameters
popt = plot_firesizepd(forest200_pd, 300, 10000, p0)

#%%
L = 200
forest200_pd = ForestFire([L,L], 0.01, 0.01**2, spark=False)
p0 = [1, 4, 1] # Initial guess for gaussian parameters
popt = plot_firesizepd(forest200_pd, 1000, 10000, p0)

#%%
L = 200
forest200_pd = ForestFire([L,L], 0.001**2, 0.001, spark=False)
p0 = [1/L, 200, 100] # Initial guess for gaussian parameters
popt = plot_firesizepd(forest200_pd, 2000, 10000, p0)

#%%
L = 200
forest200_pd = ForestFire([L,L], 0.01**2, 0.01, spark=False)
p0 = [1/L, 200, 100] # Initial guess for gaussian parameters
popt = plot_firesizepd(forest200_pd, 2000, 10000, p0)

#%%
L = 200
forest = ForestFire([L,L], 0.01, 0.01**2, spark=False)
plot_fractionvt(forest, 1000, green=False)

#%%
L = 200
forest = ForestFire([L,L], 0.01**2, 0.001, spark=False)
plot_fractionvt(forest, 10000, green=True)

#%%
L = 200
forest = ForestFire([L,L], 0.001**2, 0.001, spark=False)
plot_fractionvt(forest, 10000, green=False)

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