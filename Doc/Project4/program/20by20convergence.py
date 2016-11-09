# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:37:40 2016

@author: sindrerb
"""
cols = [0,6,7]
import matplotlib.pyplot as plt
import numpy as np

labels=np.loadtxt("./benchmarks/convergence20R",dtype='string', usecols=cols)[0,:]
rnd = np.loadtxt("./benchmarks/convergence40R",dtype='float', skiprows=1,usecols=cols)
#rnd = np.loadtxt("./benchmarks/convergence20G",dtype='float', skiprows=1,usecols=cols)

fig = plt.figure()
plt.title("Calculations from a random state at T=1")
for i in range(1,len(labels)):
    plt.subplot(len(labels)-1,1,i)
    plt.ylabel(labels[i])
    plt.xscale('log')
    plt.ylim(min(rnd[:,i])-abs(min(rnd[:,i]))*0.01,max(rnd[:,i])+abs(max(rnd[:,i]))*0.01)
    plt.plot(rnd[:,0],rnd[:,i])
plt.xlabel(labels[0])