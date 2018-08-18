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
This agent have an CES utility(Tresch, 2014) and Cobb–Douglas technology.

Specifically, I use the Cobb-Douglas technology described in Turnovsky & 
Monteiro(2007).
This production function incorporates the production externality of capital, 
which could be positive or negative. 
As more and more capital is accumulated,the agent would have more knowledge of 
how to fully utilize it. It would boost the productivity of captital.
On the other hand, the usage of capital could produce pollution that would 
exacerbate the productivity of capital as more and more capital is used(e.g. 
increasing water temperature for machines that need to be cooled down 
periodically)
'''
import numpy as np
import sympy as sp

class Agent(object):
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
    def __init__(self, g = 1.1, a = 1.2, t = 1.9, c_k = 0.6, c_l = 0.4,\
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
    Define the utility function.
    The output_lst consists of three arguments: g, k and l.
    g: number of goods consumed
    k: number of capital supplied
    l: number of labor supplied
    '''
    def Util(self, eq):
        eq = np.array(eq)
        g = eq[0]
        k = eq[1]
        l = eq[2]
        utility = (0.5*g**self.g)**(self.a/self.g)-(self.c_k*(k**self.t)+self.c_l*(l**self.t))/self.t
        return utility
    def Prod(self, eq):
        eq = np.array(eq)
        g = eq[0]
        k = eq[1]
        l = eq[2]
        return (k**(self.a_k+self.PE)*l**self.a_l)
    '''
    Solve for the Pareto optimum.
    '''
    def Equi(self):
    
    '''
    Sys_PE defines FOCs for the social planner.
    '''
    def Sys_PE(self, x):
        g, k, l, L = x
        return ((1-self.a)*(0.5*(g**2)**(self.g))**((1-self.a-self.g)/self.g)*(g**2)**(self.g-1)+L,\
                -self.c_k*(k**2)**(self.t-1)-L*(self.a_k+self/PE)*(k**2)**(self.a_k+self.PE-1)*(l**2)**self.a_l,\
                -self.c_l*(l**2)**(self.t-1)-L*self.a_l*(l**2)**(self.a_l-1)*(k**2)**(self.a_k+self.PE),\
                g**2-(k**2)**(self.a_k+self.PE)*(l**2)**self.a_l)
    '''
    Sys defines FOCs for individual who cannot observe the production
    externality when making his/her decision.
    '''
    def Sys(self):
        
    '''
    Comp is a callable function that tells the users
    1. The difference of utility level between two allocation
    2. The amount of capital that is underinvested(overinvested) by the individual.
    '''
    def Comp(self):
    
    '''
    Pig is a callable function that returns
    1.
    2.
    3.
    '''
    def Pig(self):
