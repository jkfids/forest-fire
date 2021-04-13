# forest-fire
Main ForestFire class in forestfire.py

The forest-fire model is a cellular automaton modeling the dynamical progression of forest fires. The particular model in this repository is the Drossel & Schwabi (1992) model, which is defined by the following rules executed synchronously:
1. Red site becomes black
2. Green site becomes red if one of its adjacent neighbours is red, otherwise it becomes red with probability f
3. Black site becomes green with probability p

Reference(s):
https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.69.1629
