'''
FUNCTION SET metrics.py

A function set containing metrics to measure the performance of countries at
the Olypmics.

Stephen M. February, 2022
'''

#################################### IMPORTS ###################################

import numpy as np

#################################### METRICS ###################################

# Weighted-medal total (Gold=3, Silver=2, Bronze=1)
def weighted_total(medals):
  G = medals[:,0]
  S = medals[:,1]
  B = medals[:,2]
  return (G*3 + S*2 + B*1)

# May add more metrics later.
