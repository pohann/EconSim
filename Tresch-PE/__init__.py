# -*- coding: utf-8 -*-

"""
Created on Mon Jul 23 21:14:50 2018

@author: Pohan
"""

'''
The goal of this module is to solve for a consumer's problem with production 
externality.
In this model, we have an agent who consumes what s/he could produce.
There is only one good and two factors:labor and capital.
This agent have an CES utility(Tresch, 2014) and Cobb–Douglas technology(
Turnovsky & Monteiro, 2007).

The production function incorporates the production externality of capital, 
which could be positive or negative. 
As more and more capital is accumulated,the agent would have more knowledge of 
how to fully utilize it. It would boost the productivity of captital.
On the other hand, the usage of capital could produce pollution that would 
exacerbate the productivity of capital as more and more capital is used(e.g. 
increasing water temperature for machines that need to be cooled down 
periodically)
'''
import numpy as np
from scipy.optimize import fsolve
from SOE import SOE
from Agent import Agent
import random

class Tres(object):
    '''
    This class define the utility and technology.
    PE: the parameter for production technology.
    PE = 0(default): no externality from capital.
    PE > 0 : positive externality from capital.
    PE < 0 : negative externality from capital.
    Users could assign any value to the rest of the parameters. But for the 
    existence and uniqueness of solution, please carefully check for the 
    concavity of the objective function.
    '''
    def __init__(self, g = 1.1, a = -0.2, t = 2.1, c_k = 0.6, c_l = 0.4,\
                 a_k = 0.3, a_l = 0.7, PE = 0, ):
        self.g = g
        self.a = a
        self.t = t
        self.c_k = c_k
        self.c_l = c_l
        self.a_k = a_k
        self.a_l = a_l
        if PE == 0:
            self.PE = PE
        elif PE > 0:
            self.PE = 0.2
        else:
            self.PE = -0.2
    '''
    Solve for the Pareto optimum.
    '''
    def Equi(self):
        sys = SOE(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE)
        x =  fsolve(sys.SP, ((random.uniform(0.1,1),)*4))
        while x[0]<=1e-8:
            x =  fsolve(sys.SP, ((random.uniform(1,10),)*4))
        y = np.array([])
        for b in range(3):
            y = np.append(y,x[b]**2)
        y = np.append(y,x[3])
        print y
    '''
    Comp is a callable function that tells the users
    1. The difference of utility level between two allocation
    2. The amount of capital that is underinvested(overinvested) by the individual.
    '''
    def Comp(self):
        sys = SOE(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE)
        x =  fsolve(sys.SP, ((random.uniform(-1,1),)*4))
        while x[0]<=1e-8:
            x =  fsolve(sys.SP, ((random.uniform(-1,1),)*4))
        y_1 = np.array([])
        for b in range(3):
            y_1 = np.append(y_1,x[b]**2)
        y_1 = np.append(y_1,x[3])
        
        x =  fsolve(sys.Ind, ((random.uniform(-1,1),)*4))
        while x[0]<=1e-8:
            x =  fsolve(sys.Ind, ((random.uniform(-1,1),)*4))
        y_2 = np.array([])
        for b in range(3):
            y_2 = np.append(y_2,x[b]**2)
        y_2 = np.append(y_2,x[3])
        a = Agent(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE) 
        y_2[0] = a.Prod(y_2)
        u_1 = a.Util(y_1)
        u_2 = a.Util(y_2)
        print y_1 
        print y_2
        print u_1
        print u_2
    '''
    Pig is a callable function that returns
    1.
    2.
    3.
    '''
    #def Pig(self):
