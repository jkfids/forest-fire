# forest-fire
The forest-fire model is a cellular automaton modeling the dynamical progression of forest fires. The particular model in this repository is the Drossel & Schwabi (1992) model, which is defined by the following rules:
1. Red site becomes black
2. Green site becomes red if one of its adjacent neighbours is red, otherwise it becomes red with probability f
3. Black site becomes green with probability p\
These rules are executed synchronously, where the forest is situated on a square lattice grid.

Reference(s):
https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.69.1629

Main ForestFire class located in forestfire.py
