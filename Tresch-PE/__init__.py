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
import datetime

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
    def __init__(self, g = 1.1, a = 0.2, t = 2.1, c_k = 0.4, c_l = 0.6,\
                 a_k = 0.1, a_l = 0.4, PE = 0, ):
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
            self.PE = float(0.1)
        else:
            self.PE = float(-0.1)
    '''
    Solve for the Pareto optimum.
    
    '''
    def equi(self):
        #random.seed(datetime.datetime.now())
        sys = SOE(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE)
        a = Agent(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE)
        x = fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
        while x[0]<=1e-2 or x[1]<=1e-2:
            x =  fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
        y = np.array([])
        for b in range(2):
            y = np.append(y,x[b]**2)
        ans = [0,0,0]
        ans[1] = y[0]
        ans[2] = y[1]
        ans[0] = a.Prod(ans)

        for i in range(1000):
            random.seed(datetime.datetime.now())
            x =  fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
            while x[0]< 1e-2 or x[1]< 1e-2:
                random.seed(datetime.datetime.now())
                x =  fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
            y = np.array([])
            for b in range(2):
                y = np.append(y,x[b]**2)
            comp = [0,0,0]
            comp[1] = y[0]
            comp[2] = y[1]
            comp[0] = a.Prod(comp)
            #print a.Util(comp)
            if a.Util(ans) < a.Util(comp):
                ans = comp
        print ans    
        print a.Util(ans)

    '''
    Comp is a callable function that tells the users
    1. The difference of utility level between two allocation
    2. The amount of capital that is underinvested(overinvested) by the individual.
    '''
    def Comp(self):
        random.seed(datetime.datetime.now())
        sys = SOE(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE)
        a = Agent(g = self.g, a = self.a, t = self.t, c_k = self.c_k, c_l = self.c_l,\
                  a_k = self.a_k, a_l = self.a_l, PE = self.PE)
        #fin the solution for the social planner

        x = fsolve(sys.KL, ((random.uniform(1,5),)*2),xtol=1.49012e-10,maxfev=10000)
        while x[0]<=1e-2 or x[1]<=1e-2:
            x =  fsolve(sys.KL, ((random.uniform(1,5),)*2),xtol=1.49012e-10,maxfev=10000)
        y = np.array([])
        for b in range(2):
            y = np.append(y,x[b]**2)
        ans = [0,0,0]
        ans[1] = y[0]
        ans[2] = y[1]
        ans[0] = a.Prod(ans)

        for i in range(1000):
            random.seed(datetime.datetime.now())
            x =  fsolve(sys.KL, ((random.uniform(1,5),)*2),xtol=1.49012e-10,maxfev=10000)
            while x[0]<=1e-2 or x[1]<=1e-2:
                random.seed(datetime.datetime.now())
                x =  fsolve(sys.KL, ((random.uniform(1,5),)*2),xtol=1.49012e-10,maxfev=10000)
            y = np.array([])
            for b in range(2):
                y = np.append(y,x[b]**2)
            comp = [0,0,0]
            comp[1] = y[0]
            comp[2] = y[1]
            comp[0] = a.Prod(comp)
            #print a.Util(comp)
            if a.Util(ans) < a.Util(comp):
                ans = comp
        ans1 = ans
        u1 = a.Util(ans1)
        x = fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
        while x[0]<=1e-2 or x[1]<=1e-2:
            x =  fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
        y = np.array([])
        for b in range(2):
            y = np.append(y,x[b]**2)
        ans = [0,0,0]
        ans[1] = y[0]
        ans[2] = y[1]
        ans[0] = a.Prod(ans)

        for i in range(1000):
            random.seed(datetime.datetime.now())
            x =  fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
            while x[0]< 1e-2 or x[1]< 1e-2:
                random.seed(datetime.datetime.now())
                x =  fsolve(sys.KL_PE, ((random.uniform(1,5),)*2),xtol=1.49012e-10)
            y = np.array([])
            for b in range(2):
                y = np.append(y,x[b]**2)
            comp = [0,0,0]
            comp[1] = y[0]
            comp[2] = y[1]
            comp[0] = a.Prod(comp)
            #print a.Util(comp)
            if a.Util(ans) < a.Util(comp):
                ans = comp
        ans2 = ans
        u2 = a.Util(ans2)
        d = u2-u1
        k1 = ans1[1]
        k2 = ans2[1]
        kd = k2-k1
        print "Individual utility level: %6.4f"%u1
        print "Optimal utility level: %6.4f"%u2
        print "There is a %6.4f difference"%d
        print "Capital is underinvested by %6.4f"%kd
    '''
    Pig is a callable function that returns
    1.
    2.
    3.
    '''
    #def Pig(self):
