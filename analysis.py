# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:24:11 2021

@author: Fidel
"""
# Import standard libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import colors
from matplotlib.animation import FuncAnimation
from time import time

# Import ForestFire class
from forestfire import ForestFire

def animate_forest(forest, interval=100, frames=200, name='forestfire.gif'):
    """Animate a forest fire for a given number of frames (i.e. timesteps)"""
    start = time()
    cmap = colors.ListedColormap(['red', 'black', 'green'])
    bounds = [-1, -0.5, 0.5, 1]
    norm = colors.BoundaryNorm(bounds,  cmap.N)
    
    fig, ax = plt.subplots()
    ax.axis('off')
    fig = plt.figure(frameon=False)
    fig.set_size_inches(10,10)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
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
    
def plot_fractionvt(forest, t_max, green=True):
    """Plot fraction of green and red vs t"""
    fig, ax = plt.subplots()
    ax.set_xlabel('Time')
    ax.set_ylabel('Grid State Fractions')
    ax.grid(True)

    props = dict(boxstyle='square', facecolor='white')
    textbox = (
                f'L = {forest.height}\n'
                f'p = {forest.p}\n'
                f'f = {forest.f}'
    )
    ax.text(0.865, 0.965, textbox, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', bbox=props)
    
    forest.step(t_max)
    y1 = np.array(forest.s_history)/forest.size
    x = range(len(y1))
    ax.plot(x, y1, color='red')
    if green:
        y2 = np.array(forest.g_history)/forest.size
        ax.plot(x, y2, color='green')
        
def gaussian(x, a, b, sigma):
    return a*np.exp(-(x-b)**2/(2*sigma**2))

def plot_firesizepd(forest, t, N, p0):
    """"Constructs a histogram of probability vs. fire size after certain time"""
    start = time()
    forest.step(t+N)
    firesizes = forest.s_history[t:]

    bin_heights, bin_borders, _ = plt.hist(firesizes, density=True, bins='auto')
    bin_centers = bin_borders[:-1] + np.diff(bin_borders)/2
    popt, _ = curve_fit(gaussian, bin_centers, bin_heights, p0 = [1/200,7500,1000])
    X = np.linspace(bin_borders[0], bin_borders[-1], 10000)
    plt.plot(X, gaussian(X, *popt))
    
    plt.ylabel('Probability')
    plt.xlabel('Fire Size')
    plt.title('Fire Size Probability Distribution')
    end = time()
    print(f'Time elapsed: {round((end - start), 2)} seconds')
    print(f'Amplitude = {popt[0]}')
    print(f'Mean = {popt[1]}')
    print(f'Standard deviation = {popt[2]}')
    return popt

# Fire size pdf comparison
def plot_firesizepd_multi(forest1, forest2, forest3, t, N):
    start = time()
    forest1.step(t[0]+N)
    forest2.step(t[1]+N)
    forest3.step(t[2]+N)
    firesizes_history1 = forest1.s_history[t[0]:]
    firesizes_history2 = forest2.s_history[t[0]:]
    firesizes_history3 = forest3.s_history[t[0]:]
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4), dpi=144)
    weights1 = np.ones(len(firesizes_history1))/len(firesizes_history1)
    weights2 = np.ones(len(firesizes_history2))/len(firesizes_history2)
    weights3 = np.ones(len(firesizes_history3))/len(firesizes_history3)
    ax1.hist(firesizes_history1, weights=weights1, bins=100)
    ax2.hist(firesizes_history2, weights=weights2, bins=100)
    ax3.hist(firesizes_history3, weights=weights3, bins=100)
    
    end = time()
    fig.savefig('plots/' + 'firesizepds')
    print(f'Time elapsed: {round((end - start), 2)} seconds')
    
L = 200
forest1 = ForestFire([L,L], 0, 0.5, spark=True)
l = 0.01
forest2 = ForestFire([L,L], l, l**2, spark=False)
forest3 = ForestFire([L,L], l**2, l, spark=False)
t = [300, 300, 2000]
N = 10000
plot_firesizepd_multi(forest1, forest2, forest3, t, N)
