# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:31:55 2018

@author: benson
"""
import numpy as np

class Agent(object):
    def __init__(self, g = 1.1, a = -0.5, t = 2.1, c_k = 0.5, c_l = 0.5,\
                 a_k = 0.7, a_l = 0.7, PE = 0, ):
        self.g = float(g)
        self.a = float(a)
        self.t = float(t)
        self.c_k = float(c_k)
        self.c_l = float(c_l)
        self.a_k = float(a_k)
        self.a_l = float(a_l)
        if PE == 0:
            self.PE = float(PE)
        elif PE > 0:
            self.PE = float(0.01)
        else:
            self.PE = float(-0.01)
        '''
    Define the utility function.
    The output_lst consists of three arguments: g, k and l.
    g: number of goods consumed
    k: number of capital supplied
    l: number of labor supplied
    '''
    def Util(self, eq):
        x_1 = eq[0]
        k = eq[1]
        l = eq[2]
        utility = (0.5*x_1**self.g)**((1-self.a)/self.g)-(self.c_k*(k**self.t)+\
                   self.c_l*(l**self.t))/self.t
        return utility
    '''
    Define the production function
    '''
    def Prod(self, eq):    
        k = eq[1]
        l = eq[2]
        return (k**(self.a_k+self.PE)*l**self.a_l)
    def IU(self, eq):
        k = eq[1]
        l = eq[2]
        return(1000*((0.5*k**((self.a_k+self.PE)*self.g)*l**(self.a_l*self.g))**((1-self.a)/self.g)-(self.c_k*k**self.t+self.c_l*l**self.t)/self.t))