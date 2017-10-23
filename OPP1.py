#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:17:24 2017

@author: tomlavigne
"""
import numpy as np
import pylab as plt

def OPP(x, t, c0, f, A):
    """
    Solution analytique de l'equation des ondes en 2D
    
    u(x, t) = exp(j(k * x - w * t )
              
    -------------------------------------------------------------------------
    ENTREE
    ------
    x    [numpy array] (Nx)
    k    [float]  fonction de w, ici k= w / c0 (relatif à la propagation d'une OPP)
    w    [float]  scalaire de la pulsation, dépend de la fréquence (à implémenter en fonction pour la suite)
    t    [float]  scalaire  temps auquel on calcul la solution
    c0   [float]  scalaire  célérité de l'onde  

"""
    w = 2 * np.pi * f
    k = w / c0
    sol = np.zeros_like(x)   
    
    for i in range(len(x)):
        sol[i] = A * np.exp((k * x[i] - w * t))
    return sol

R = np.linspace(1e-8, 10, 100)
T = np.linspace(0, 10, 50)
C_0 = 1

# calcul de la solution analytique a t choisi avec c0=1
n = 30
SOL = OPP(R, T[n], 1, 10, 10)

plt.plot(R, SOL, lw=2)
plt.axis([0, 5, -0.5, 1])
plt.xlabel('r')
plt.ylabel(r'$p(r,t)')
plt.title(u'profil temporel à t=' + str(T[n]))
plt.grid()
