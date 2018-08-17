# -*- coding: utf-8 -*-

"""
Created on Mon Jul 23 21:54:06 2018

@author: Pohan
"""

import sympy as sp
import numpy as np
from scipy.optimize import fsolve
from C import Agent
import random

g, k, l, L = sp.symbols('g k l L')
a = Agent(0.2)  
print sp.diff(a.larg_PE(),g)
print sp.diff(a.larg_PE(),k)
print sp.diff(a.larg_PE(),l)
print sp.diff(a.larg_PE(),L)
a = Agent(0)  
print sp.diff(a.larg_PE(),g)
print sp.diff(a.larg_PE(),k)
print sp.diff(a.larg_PE(),l)
print sp.diff(a.larg_PE(),L)
'''
Solver for the quilibrium when PE=0.2(positive production externality)
'''
def seq_PE(x):
    g, k, l, L = x
    return(L + 0.563358546397024*(g**2)**(-1.0)*((g**2)**1.1)**1.09090909090909,\
           -0.5*L*(k**2)**(-0.5)*(l**2)**0.7 - 0.6*(k**2)**0.9,\
           -0.7*L*(k**2)**0.5*(l**2)**(-0.3) - 0.4*(l**2)**0.9,\
           (g**2) - (k**2)**0.5*(l**2)**0.7)

x =  fsolve(seq_PE, ((random.uniform(1,10),)*4))
while x[0]<=1e-8:
    x =  fsolve(seq_PE, ((random.uniform(1,10),)*4))
y = np.array([])
for b in range(3):
    y = np.append(y,x[b]**2)
y = np.append(y,x[3])
print y
u_1=a.Utility(y)

'''
Solver for the equilibriym when PE=0.2 but the agent can't see the positive
externality when making his decision.
'''
def seq_NE(x):
    g, k, l, L = x
    return(L + 0.563358546397024*(g**2)**(-1.0)*((g**2)**1.1)**1.09090909090909,\
           -0.3*L*(k**2)**(-0.7)*(l**2)**0.7 - 0.6*(k**2)**0.9,\
           -0.7*L*(k**2)**0.3*(l**2)**(-0.3) - 0.4*(l**2)**0.9,\
           (g**2) - (k**2)**0.3*(l**2)**0.7)

x =  fsolve(seq_NE, ((random.uniform(1,10),)*4))
while abs(x[0])<=1e-8:
    x =  fsolve(seq_NE, ((random.uniform(1,10),)*4))
y = np.array([])
for b in range(3):
    y = np.append(y,x[b]**2)
y = np.append(y,x[3])
'''
Calculate the actual production given the amount of factors chosen by the agent.
'''
y[0] = a.Production(y)
print y
'''
Calculate the actual utility level
'''
u_2=a.Utility(y)
'''
Compare the utility level of two scenarios
'''
print u_1,u_2




