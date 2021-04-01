# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:24:11 2021

@author: Fidel
"""
# Import standard libraries
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation
from time import time

# Import ForestFire class
from forestfire import ForestFire

# Create output directory if it does not exist
from pathlib import Path
Path('animations').mkdir(parents=True, exist_ok=True)
Path('plots').mkdir(parents=True, exist_ok=True)

def animate_forest(forest, interval=100, frames=100, name='forestfire.gif'):
    """Animate a forest fire for a given number of frames (i.e. timesteps)"""
    start = time()
    cmap = colors.ListedColormap(['red', 'black', 'green'])
    bounds = [-1, -0.5, 0.5, 1]
    norm = colors.BoundaryNorm(bounds,  cmap.N)
    
    fig, ax = plt.subplots()
    ax.axis('off')
    
    fig = plt.figure(frameon=False)
    fig.set_size_inches(12,12)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    def init_frame():
        ax.imshow(forest.grid, cmap=cmap, norm=norm, aspect='auto')
    
    def animate(i):
        plt.cla()
        ax.imshow(forest.grid, cmap=cmap, norm=norm, aspect='auto')
        forest.step()
        #print(f'frame {i}')
    
    anim = FuncAnimation(fig, animate, init_func=init_frame, interval=interval, frames=frames)
    anim.save('animations/' + name)
    end = time()
    print(f'Time elapsed: {round((end - start), 2)} seconds')
    
def plot_rgvt(forest, t_max):
    """Plot fraction of green and red vs t"""
    fig, ax = plt.subplots()
    ax.set_xlabel('Time')
    ax.set_ylabel('Total Red & Green')
    ax.grid(True)

    props = dict(boxstyle='square', facecolor='white')
    textbox = (
                f'L = {forest.height}\n'
                f'p = {forest.p}\n'
                f'f = {forest.f}'
    )
    ax.text(0.025, 0.965, textbox, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', bbox=props)
    
    forest.step(t_max)
    y1 = forest.s_history
    y2 = forest.g_history
    x = range(len(y1))
    
    ax.plot(x, y1, color='red')
    ax.plot(x, y2, color='green')

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
     
#%%
L = 200
high_grow_no_lightning = ForestFire([L,L], 0.2, 0.2)
plot_firesizepd(high_grow_no_lightning, 250, 1000)
    
#%%
L = 10
forest_100=ForestFire([L,L], 0.2, 0.2, spark=True)
plot_rgvt(forest_100, 200)

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