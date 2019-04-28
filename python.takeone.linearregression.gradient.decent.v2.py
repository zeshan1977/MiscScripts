#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:32:32 2018

"""
import numpy as np
#y=mx+c

def compute_error_for_given_points(b,m,points):
    totalError=0
    for i in range(0,len(points)):
        x = points[i,0]
        y= points [i,1]
        totalError += (y-(m*x+b)) **2
    return totalError/float(len(points))

def step_gradient(b_current,m_current,points,learningrate):
    #Gradient decent
    b_gradient=0
    m_gradient=0
    N = float(len(points))
    for i in range(0,len(points)):
        # Calculating partial derivative of b and m with respet to all the points
        #new _b and m are the updated 
        x = points[i,0]
        y = points[i,1]
        b_gradient += -(2/N)*(y-((m_current*x)+b_current))
        m_gradient += -(2/N) * x * (y-((m_current*x)+b_current))
    new_b = b_current - (learningrate * b_gradient)
    new_m = m_current - (learningrate * m_gradient)
    return [new_b,new_m]

def gradient_decent_runner(point,initial_b,initial_m,learningrate,numiterations):
    b= initial_b
    m= initial_m
    for i in range(numiterations):
        b,m=step_gradient(b,m,np.array(points),learningrate)
    return [b,m]
def run():
    points=np.genfromtxt('data.csv',delimiter=',')
    #import hyper parameter
    learningrate=0.0001
    
    #y=Mx+b
    
    initial_b=0
    initial_m=0
    
    numiterations=1000 # we have a smaller datas
    
    [b,m]=gradient_decent_runner(points,initial_b,initial_m,learningrate,numiterations)
    print "b,m "+ b+","+m
    
    
if __name__ == '__main__':
    run()
    