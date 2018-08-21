# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:31:55 2018

@author: benson
"""
import numpy as np

class Agent(object):
    def __init__(self, g = 1.1, a = -0.5, t = 2.1, c_k = 0.5, c_l = 0.5,\
                 a_k = 0.7, a_l = 0.7, PE = 0, ):
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
            self.PE = 0.05
        else:
            self.PE = -0.05
        '''
    Define the utility function.
    The output_lst consists of three arguments: g, k and l.
    g: number of goods consumed
    k: number of capital supplied
    l: number of labor supplied
    '''
    def Util(self, eq):
        x1 = eq[0]
        k = eq[1]
        l = eq[2]
        utility = (0.5*x1**self.g)**((1-self.a)/self.g)-(self.c_k*(k**self.t)+\
                   self.c_l*(l**self.t))/self.t
        return utility
    '''
    Define the production function
    '''
    def Prod(self, eq):    
        k = eq[1]
        l = eq[2]
        return (k**(self.a_k+self.PE)*l**self.a_l)