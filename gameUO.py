#!/usr/bin/env python

"""
Author:  Robin Ankele <robin.ankele@cs.ox.ac.uk>
         http://users.ox.ac.uk/~kell4062
         
Copyright (c) 2017, University of Oxford
All rights reserved.
"""

from gameBasic import G
from random import randint

class G_UO(G):
  def __init__(self):
    G.__init__(self)
    self.b = 0
  
  def __finialize__(self):
    G.__finialize__(self)
  
  def oracle_U_f(self):
    return G._U_f(self)
  
  def oracle_Q_f(self):
    return G._Q_f(self)
  
  def oracle_P_f(self):
    return G._P_f(self)
  
  def view_refutable(self, pi_phi, pi_q, op_1=None, op_2=None):
    self.b = randint(0,1)
  
    e_ = []
    b = 0
    
    for i in range(0, G.n):
      if self.b == 0:
        op_1(e_, pi_phi(G.p[i]))
        op_2(b_, pi_q(G.p[i]))
  
    return e_, b

  def UO(self, u_x, a_x, p_x):
    G.input(self, u_x, a_x, p_x)
    e_x_, b_x = view_refutable()
    
    """ Perform adversarial magic to break notion """

    return validate(g)

  def validate(self, g):
    if g == self.b:
      return true
    return false


if __name__ == '__main__':
  print >> sys.stderr, "This is a library and should not be executed standalone"
  sys.exit(1)
