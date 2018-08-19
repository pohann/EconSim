# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:55:59 2018

@author: benson
"""



class SOE(object):
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
    Sys_PE defines FOCs for the social planner.
    '''
    def SP(self, x):
        g, k, l, L = x
        return ((1-self.a)*(0.5*(g**2)**(self.g))**((1-self.a-self.g)/self.g)*(0.5*g**2)**(self.g-1)+L,\
                -self.c_k*(k**2)**(self.t-1)-L*(self.a_k+self.PE)*(k**2)**(self.a_k+self.PE-1)*(l**2)**self.a_l,\
                -self.c_l*(l**2)**(self.t-1)-L*self.a_l*(l**2)**(self.a_l-1)*(k**2)**(self.a_k+self.PE),\
                g**2-(k**2)**(self.a_k+self.PE)*(l**2)**self.a_l)
    '''
    Sys defines FOCs for individual who cannot observe the production
    externality when making his/her decision.
    '''
    def Ind(self, x):
        g, k, l, L = x
        return ((1-self.a)*(0.5*(g**2)**(self.g))**((1-self.a-self.g)/self.g)*(0.5*g**2)**(self.g-1)+L,\
                -self.c_k*(k**2)**(self.t-1)-L*self.a_k*(k**2)**(self.a_k-1)*(l**2)**self.a_l,\
                -self.c_l*(l**2)**(self.t-1)-L*self.a_l*(l**2)**(self.a_l-1)*(k**2)**self.a_k,\
                g**2-(k**2)**self.a_k*(l**2)**self.a_l)
    