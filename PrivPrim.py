#!/usr/bin/env python

"""
Author:  Robin Ankele <robin.ankele@cs.ox.ac.uk>
         http://users.ox.ac.uk/~kell4062
         
Copyright (c) 2017, University of Oxford
All rights reserved.
"""

import sys
import os
from random import uniform, randint
from math import log
import itertools

class PrivPrim():

  def __init__(self):
    pass

  def __finialize__(self):
    pass

  ''' privacy primitives (i.e. pi_phi) '''
  def identity(self, x):
    x_ = []
    for i in range(0, len(x)):
      x_.append(x[i].value())
    return x_
    
  def perturbUnif(self, x, lower_bound=0, upper_bound=1):
    x_ = []
    for i in range(0, len(x)):
      x_.append(x[i].value() + uniform(lower_bound, upper_bound))
    return x_
  
  def perturbLap(self, x, lower_bound=0, upper_bound=1, mue=0, b=1):
    x_ = []
    for i in range(0, len(x)):
      noise_uniform = uniform(-0.5, 0.5)
      x_.append(x[i].value() + (mue - b * cmp(noise_uniform, 0) * log(1.0 - 2.0 * abs(noise_uniform))))
    return x_
  
  def permutate(self, x):
    x_ = []
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            x_.append(x[i][j])
    perm = list(itertools.permutations(x_))
    i = randint(0, len(perm))
    return perm[i]
  
  ''' data mining algorithms (i.e. pi_q) '''
  def sum(self, x):
    y = 0
    for i in range(0, len(x)):
      y = y + x[i].value()
    return [y]

  ''' concatination algorithms (i.e. op_1, op_2) '''
  ''' Methods of result-degree n (vector value) '''
  def none_(self, x):
    return [x]

  def aggregation(self, x):
    x_ = []
    for i in range(0, len(x)):
      x_.append(x[i])
    return x_

  ''' Methods of result-degree 1 (single value) '''
  def none(self, x):
    return x

  def average(self, x):
    y = 0
    c = 0
    for i in range(0, len(x)):
      for j in range(0, len(x[i])):
        y = y + x[i][j]
        c = c + 1
    return y / c

if __name__ == '__main__':
  print >> sys.stderr, "This is a library and should not be executed standalone"
  sys.exit(1)
