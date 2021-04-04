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

