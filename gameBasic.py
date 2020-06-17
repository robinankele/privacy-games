#!/usr/bin/env python

"""
Author:  Robin Ankele <robin.ankele@cs.ox.ac.uk>
         http://users.ox.ac.uk/~kell4062
         
Copyright (c) 2017, University of Oxford
All rights reserved.
"""

import sys
import os

""" Helper Classes """
class Parameter():
  def __init__(self, u_i, a_i):
    self.u_i = u_i
    self.a_i = a_i

  def identifier(self):
    return self.u_i

  def value(self):
    return self.a_i


class Party():
  def __init__(self, p_i):
    self.db = []
    self.p_i = p_i

  def add(self, u_i, a_i):
    self.db.append(Parameter(u_i, a_i))
  
  def get(self, u_i):
    a_ = []
    for i in range(0, len(self.db)):
      if self.db[i].identifer() == u_i:
        a_.append(self.db[i].value())
    return a_
    
  def validate(self, e_x, u_x):
    if len(e_x) > 1:
      e_x = e_x[0]
  
    for i in range(0, len(self.db)):
      if self.db[i].value() == e_x and self.db[i].identifier() == u_x:
        return true
    return false

  def corrupt(self):
    for i in range(0, len(self.db)):
        print("a_i: " + str(self.db[i].value()) + ", u_i: " + str(self.db[i].identifier()))
    return self.db


""" Basic class: Game G """
class G():
  def __init__(self):
    self.c = 0
    self.n = 0
    self.p = []
    self.__q_f = dict()
    self.__p_f = dict()
  
  def __finialize__(self):
    pass
  
  def initialise(self, n):
    self.c = 0
    self.n = n
    
    for i in range(0, self.n):
      self.p.append(Party(i))

  def input(self, u_i, a_i, p_i):
    self.p[p_i].add(u_i, a_i)
    self.c = self.c + 1
    
    if self.__q_f.get(u_i) == None:
      self.__q_f[u_i] = 1
    else:
      self.__q_f[u_i] = self.__q_f[u_i] + 1

    if self.__p_f.get(u_i) == None:
      self.__p_f[u_i] = []
    self.__p_f[u_i].append(a_i)

  def view(self, pi_phi, pi_q, op_1, op_2):
    e_ = []
    b_ = []
    
    for i in range(0, self.n):
      e_.append(pi_phi(self.p[i].db))
      b_.append(pi_q(self.p[i].db))
    
    return op_1(e_), op_2(b_)

  def corrupt(self, p_i):
    return self.p[p_i].corrupt()

  """ This should be a private function. """
  def _f(self, e_x, u_x):
    for i in range(0, self.n):
      if self.p[i].validate(e_x, u_x):
        return true
    return false

  """ This is a protected function, only accessible by inherited classes. """
  def _U_f(self):
    return self.__q_f.keys()
  
  """ This is a protected function, only accessible by inherited classes.  """
  def _size_U_f(self):
    return len(self.__q_f)

  """ This is a protected function, only accessible by inherited classes.  """
  def _Q_f(self):
    return self.__q_f.items()

  """ TThis is a protected function, only accessible by inherited classes.  """
  def _P_f(self):
    return self.__p_f.values()

if __name__ == '__main__':
  print >> sys.stderr, "This is a library and should not be executed standalone"
  sys.exit(1)
