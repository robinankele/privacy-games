#!/usr/bin/env python

"""
Author:  Robin Ankele <robin.ankele@cs.ox.ac.uk>
         http://users.ox.ac.uk/~kell4062
         
Copyright (c) 2017, University of Oxford
All rights reserved.
"""

from gameBasic import G

class G_WU(G):
  def __init__(self):
    G.__init__(self)
  
  def __finialize__(self):
    G.__finialize__(self)
  
  def oracle_U_f(self):
    return G._U_f(self)
  
  def oracle_Q_f(self):
    return G._Q_f(self)

  def WU(self, u_x, a_x, p_x):
    G.input(self, u_x, a_x, p_x)
    e_x_, b_x = G.view(self)
    
    """ Perform adversarial magic to break notion """
    e_x = 0
    e_y = 0
    u_x = u_x
    
    return validate(e_x, e_y, u_x)

  def validate(self, e_x, e_y, u_x):
    if G._f(self, e_x, u_x) and G._f(self, e_y, u_x):
      return true
    return false


if __name__ == '__main__':
  print >> sys.stderr, "This is a library and should not be executed standalone"
  sys.exit(1)