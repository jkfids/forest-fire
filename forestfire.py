# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:58:30 2021

@author: Fidel
"""

# Import standard libraries
import numpy as np

class ForestFire:
    """
    Construct a forest fire model consisting of a two-dimensional square lattice 
    with periodic boundary conditions. Each site can occupy one of three states: 
    Black (empty), green (trees), red (fire). At each timestep, the grid updates
    according the following rules:
        1. Red site becomes black
        2. Green site becomes red if one of its adjacent neighbours is red, 
           otherwise it becomes red with probability f
        3. Black site becomes green with probability p
    """
    def __init__(self, shape=[50,50], f=0.01, p=0.5, spark=False):
        self.width = shape[1]
        self.height = shape[0]
        self.f = f
        self.p = p
        
        self.grid = np.random.randint(0, 2, size=[self.height, self.width])
        if spark:
            self.grid[round(self.height/2)][round(self.width/2)] = -1
        self.grid
        self.size = self.width*self.height
        
        self.time = 0
        
        self.g = self.count(1)
        self.g_history = [self.g]
        self.s = 0
        self.s_history = [self.s]
    
    def step(self, steps=1):
        """Timestep the forest fire by the number of steps"""
        for step in range(steps):
            
            rand = np.random.rand(self.height, self.width)
            burnt = self.grid == -1
            regrow = (self.grid == 0)&(rand < self.p)
            spread = -2*((self.grid == 1)&self.spread_grid())
            lightning = -2*((self.grid == 1)&(rand < self.f))
            
            self.grid += spread + burnt + regrow + lightning
    
            self.g = self.count(1)
            self.g_history.append(self.g)
            self.s = self.count(-1)
            self.s_history.append(self.s)
            self.time += 1
    
    def spread_grid(self):
        """Constructs a spread grid with np.roll"""
        fire = self.grid == -1
        spread = np.roll(fire, 1, 0)|np.roll(fire, -1, 0)|np.roll(fire, 1, 1)|np.roll(fire, -1, 1)
        return spread
    
    def count(self, x):
        return np.sum(self.grid==x)
    
    def fraction(self, x):
        return self.count(x)/(self.size)