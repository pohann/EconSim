# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:55:59 2018

@author: benson
"""



class SOE(object):
    def __init__(self, g = 1.1, a = -0.5, t = 2.1, c_k = 0.4, c_l = 0.6,\
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
            self.PE = float(0.02)
        else:
            self.PE = float(-0.02)
    '''
    Sys_PE defines FOCs for the social planner.
    '''
    def SP(self, x):
        x1, k, l, L = x
        return ((1-self.a)*(0.5*(x1**2)**(self.g))**((1-self.a-self.g)/self.g)*(0.5*x1**2)**(self.g-1)+L,\
                -self.c_k*(k**2)**(self.t-1)-L*(self.a_k+self.PE)*(k**2)**(self.a_k+self.PE-1)*(l**2)**self.a_l,\
                -self.c_l*(l**2)**(self.t-1)-L*self.a_l*(l**2)**(self.a_l-1)*(k**2)**(self.a_k+self.PE),\
                x1**2-(k**2)**(self.a_k+self.PE)*(l**2)**self.a_l)
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
    
    def KL(self, x):
        k,l = x
        return(0.5**((1-self.a)/self.g)*self.a_k*(1-self.a)*(self.a_k*(1-self.a)-1)*(k**2)**(self.a_k*(1-self.a)-1)\
               *(l**2)**(self.a_l*(1-self.a))-self.c_k*(k**2)**(self.t-1),\
               0.5**((1-self.a)/self.g)*self.a_l*(1-self.a)*(self.a_l*(1-self.a)-1)*(k**2)**(self.a_k*(1-self.a))\
               *(l**2)**(self.a_l*(1-self.a)-1)-self.c_l*(l**2)**(self.t-1)
               )
    def KL_PE(self, x):
        k,l = x
        return(0.5**((1-self.a)/self.g)*(self.a_k+self.PE)*(1-self.a)*((self.a_k+self.PE)*(1-self.a)-1)*(k**2)**((self.a_k+self.PE)*(1-self.a)-1)\
               *(l**2)**(self.a_l*(1-self.a))-self.c_k*(k**2)**(self.t-1),\
               0.5**((1-self.a)/self.g)*self.a_l*(1-self.a)*(self.a_l*(1-self.a)-1)*(k**2)**((self.a_k+self.PE)*(1-self.a))\
               *(l**2)**(self.a_l*(1-self.a)-1)-self.c_l*(l**2)**(self.t-1)
               )
        
    